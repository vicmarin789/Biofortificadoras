# ? Analisador de Funções Biofortificadoras em Bactérias

Aplicativo interativo para análise de genes associados à síntese de nutrientes e compostos bioativos, com classificação baseada na presença e no percentual de genes detectados.

---

## ? Solicitação de uso oficial
Para acesso à base completa de dados e utilização da ferramenta em análises oficiais, entre em contato:  
**Victor Augustus Marin**  
? **Email:** victor.marin@unirio.br

---

## ? Descrição
Ferramenta para detecção e classificação de funções biofortificadoras bacterianas, baseada na presença de genes-chave para rotas metabólicas de produção de vitaminas, minerais, ácidos graxos, aminoácidos e outros compostos de interesse.  

Integra uma base manual curada com dados de literatura científica, permitindo identificar o potencial de biofortificação de diferentes espécies bacterianas.  

Desenvolvida para auxiliar em pesquisas de microbiologia aplicada, segurança alimentar, biotecnologia e estudos de microbiota.

---

## ? Principais Aplicações
- **MAPA** – Avaliação de microrganismos de interesse em alimentos e insumos agropecuários.  
- **Anvisa** – Apoio em análises de risco e estudos de impacto nutricional.  
- **Instituições de pesquisa** – Triagem de cepas com potencial probiótico ou biofortificador.  
- **Indústria de alimentos e suplementos** – Seleção de culturas iniciadoras e probióticos com funções nutricionais específicas.

---

## ? Estrutura da Ferramenta
- **Base manual:** curada por especialista, com lista de nutrientes/compostos e genes associados.  
- **Classificação:** baseada no percentual de genes detectados para cada função.  
- **Relatório:** lista de funções presentes e ausentes, com percentual de cobertura.

---

## ?? Como Testar
1. Baixe o modelo de entrada disponível no app.  
2. Preencha com os genes identificados no genoma anotado.  
3. Carregue o arquivo no aplicativo **Streamlit**.  
4. Defina o percentual mínimo de detecção (por exemplo, 80%).  
5. Visualize as funções biofortificadoras detectadas e seus percentuais.

---

?? **Atenção:** A versão pública não contém a base completa. Para uso oficial, solicite acesso conforme instruções no início deste documento.

---

## ? Exemplo de Saída

| Função | Percentual de Genes Detectados |
|--------|--------------------------------|
| Vitamina K2 (menaquinona) | 100% |
| Ferro (sideróforos) | 90% |
| PUFAs (DHA/EPA) | 80% |
| Poliaminas | 100% |

---

## ?? Pré-requisitos
- Python 3.9+  
- Streamlit  
- Arquivo CSV de entrada no formato:  
