# ? Analisador de Fun��es Biofortificadoras em Bact�rias

Aplicativo interativo para an�lise de genes associados � s�ntese de nutrientes e compostos bioativos, com classifica��o baseada na presen�a e no percentual de genes detectados.

---

## ? Solicita��o de uso oficial
Para acesso � base completa de dados e utiliza��o da ferramenta em an�lises oficiais, entre em contato:  
**Victor Augustus Marin**  
? **Email:** victor.marin@unirio.br

---

## ? Descri��o
Ferramenta para detec��o e classifica��o de fun��es biofortificadoras bacterianas, baseada na presen�a de genes-chave para rotas metab�licas de produ��o de vitaminas, minerais, �cidos graxos, amino�cidos e outros compostos de interesse.  

Integra uma base manual curada com dados de literatura cient�fica, permitindo identificar o potencial de biofortifica��o de diferentes esp�cies bacterianas.  

Desenvolvida para auxiliar em pesquisas de microbiologia aplicada, seguran�a alimentar, biotecnologia e estudos de microbiota.

---

## ? Principais Aplica��es
- **MAPA** � Avalia��o de microrganismos de interesse em alimentos e insumos agropecu�rios.  
- **Anvisa** � Apoio em an�lises de risco e estudos de impacto nutricional.  
- **Institui��es de pesquisa** � Triagem de cepas com potencial probi�tico ou biofortificador.  
- **Ind�stria de alimentos e suplementos** � Sele��o de culturas iniciadoras e probi�ticos com fun��es nutricionais espec�ficas.

---

## ? Estrutura da Ferramenta
- **Base manual:** curada por especialista, com lista de nutrientes/compostos e genes associados.  
- **Classifica��o:** baseada no percentual de genes detectados para cada fun��o.  
- **Relat�rio:** lista de fun��es presentes e ausentes, com percentual de cobertura.

---

## ?? Como Testar
1. Baixe o modelo de entrada dispon�vel no app.  
2. Preencha com os genes identificados no genoma anotado.  
3. Carregue o arquivo no aplicativo **Streamlit**.  
4. Defina o percentual m�nimo de detec��o (por exemplo, 80%).  
5. Visualize as fun��es biofortificadoras detectadas e seus percentuais.

---

?? **Aten��o:** A vers�o p�blica n�o cont�m a base completa. Para uso oficial, solicite acesso conforme instru��es no in�cio deste documento.

---

## ? Exemplo de Sa�da

| Fun��o | Percentual de Genes Detectados |
|--------|--------------------------------|
| Vitamina K2 (menaquinona) | 100% |
| Ferro (sider�foros) | 90% |
| PUFAs (DHA/EPA) | 80% |
| Poliaminas | 100% |

---

## ?? Pr�-requisitos
- Python 3.9+  
- Streamlit  
- Arquivo CSV de entrada no formato:  
