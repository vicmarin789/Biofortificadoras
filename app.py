import streamlit as st
import pandas as pd
from Bio import SeqIO
from pathlib import Path
import io
import re

st.set_page_config(page_title="Analisador de Genes", layout="wide")
st.title("🧬 Analisador de Genes por Função Biofortificadora")

# Caminho relativo ao arquivo app.py
BASE_DIR = Path(__file__).parent
caminho_csv = BASE_DIR / "tabela_genes.csv"

df_ref = pd.read_csv(caminho_csv, encoding="utf-8")

# =========================
# Utilidades de normalização
# =========================
def normalize_gene_name(name: str) -> str:
    # lower, remove espaços, hífens e underscores
    n = name.strip().lower()
    n = n.replace(" ", "").replace("-", "").replace("_", "")
    # remove caracteres não alfanuméricos restantes
    n = re.sub(r"[^a-z0-9]", "", n)
    return n

def split_genes_field(text: str):
    # Divide por vírgula ou ponto e vírgula
    parts = [p.strip() for p in re.split(r"[;,]", str(text)) if p.strip()]
    return parts

# =========================
# Leitura da tabela de referência
# =========================
df_ref = pd.read_csv(caminho_csv, encoding="utf-8")
if "Genes" not in df_ref.columns:
    st.error("A coluna 'Genes' não foi encontrada no CSV de referência. Verifique o arquivo.")
    st.stop()

# Pré-processa a lista de genes de referência (mantendo original e normalizado)
df_ref["Genes"] = df_ref["Genes"].astype(str)

# Upload do genoma (agora aceita .genbank também)
uploaded_genome = st.file_uploader(
    "Envie um genoma (.gbk, .gb, .gbff, .genbank)",
    type=["gbk", "gb", "gbff", "genbank", "GENBANK"]
)

if uploaded_genome:
    # Slider para percentual mínimo
    percentual_minimo_slider = st.slider(
        "Percentual mínimo de genes para considerar detectada",
        min_value=0,
        max_value=100,
        value=60,
        step=5
    )
    percentual_minimo = percentual_minimo_slider / 100.0

    # Lê e converte para texto (corrige erro de modo binário)
    conteudo = uploaded_genome.read().decode("utf-8", errors="ignore")
    handle = io.StringIO(conteudo)

    # =========================
    # Extração abrangente de nomes de genes do genoma
    # =========================
    genome_genes_raw = set()

    for record in SeqIO.parse(handle, "genbank"):
        for feature in record.features:
            if feature.type in {"gene", "CDS"}:
                # Colete possíveis qualifiers de identificação de gene
                for key in ("gene", "locus_tag", "gene_synonym"):
                    vals = feature.qualifiers.get(key, [])
                    for v in vals:
                        v = v.strip()
                        if v:
                            # gene_synonym pode vir com múltiplos separados por ; ou ,
                            for cand in re.split(r"[;,]", v):
                                cand = cand.strip()
                                if cand:
                                    genome_genes_raw.add(cand)

    # Normaliza os nomes do genoma
    genome_genes = {normalize_gene_name(g) for g in genome_genes_raw if normalize_gene_name(g)}

    # -------------------------
    # Funções auxiliares de comparação
    # -------------------------
    def comparar_funcao(genes_ref_str: str):
        # Lista original de genes da função
        lista_orig = split_genes_field(genes_ref_str)
        # Normalizados
        lista_norm = [normalize_gene_name(g) for g in lista_orig if normalize_gene_name(g)]
        if not lista_norm:
            return False, 0, 0, []

        # Quais foram encontrados
        encontrados_norm = [g for g in lista_norm if g in genome_genes]
        # Para exibir, vamos mapear de volta nomes "originais" que bateram
        encontrados_exib = []
        norm_to_orig = {}
        for g in lista_orig:
            gn = normalize_gene_name(g)
            if gn and gn not in norm_to_orig:
                norm_to_orig[gn] = g

        for gn in encontrados_norm:
            encontrados_exib.append(norm_to_orig.get(gn, gn))

        total = len(lista_norm)
        achados = len(encontrados_norm)
        detectado = (achados / total) >= percentual_minimo
        return detectado, achados, total, sorted(set(encontrados_exib), key=str.lower)

    # Aplica comparação para cada linha
    resultados = df_ref["Genes"].apply(comparar_funcao)

    # Descompacta resultados em colunas
    df_ref["Detectado"] = resultados.apply(lambda x: x[0])
    df_ref["Genes_encontrados"] = resultados.apply(lambda x: ", ".join(x[3]) if x[3] else "")
    df_ref["Encontrados"] = resultados.apply(lambda x: x[1])
    df_ref["Total_ref"] = resultados.apply(lambda x: x[2])
    df_ref["Cobertura_%"] = ((df_ref["Encontrados"] / df_ref["Total_ref"]).fillna(0) * 100).round(1)

    # =========================
    # Exibição
    # =========================
    st.markdown("## 📊 Resultado da Análise")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Genes distintos no genoma", len(genome_genes))
    with col2:
        st.metric("Funções detectadas", int(df_ref["Detectado"].sum()))
    with col3:
        st.metric("Percentual mínimo", f"{int(percentual_minimo*100)}%")

    st.markdown("### Visualização da tabela")
    mostrar_detectados = st.checkbox("Mostrar apenas funções detectadas", value=False)
    colunas_exibir = ["Função", "Detectado", "Cobertura_%", "Encontrados", "Total_ref", "Genes", "Genes_encontrados"]

    if mostrar_detectados:
        st.dataframe(df_ref[df_ref["Detectado"]][colunas_exibir], use_container_width=True)
    else:
        st.dataframe(df_ref[colunas_exibir], use_container_width=True)

    # Download dos resultados
    csv_resultados = df_ref[colunas_exibir].to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Baixar resultados em CSV",
        data=csv_resultados,
        file_name="resultado_genes.csv",
        mime="text/csv"
    )

    # Debug opcional (expanda para ver alguns genes extraídos do genoma)
    with st.expander("Ver amostra de genes extraídos do genoma (debug)"):
        sample = sorted(list(genome_genes_raw))[:100]
        st.write(sample)
else:
    st.info("🧬 Envie um arquivo de genoma para prosseguir.")
