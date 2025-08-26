# Projetos de Estatística Aplicada

Este repositório reúne análises estatísticas realizadas em Python, utilizando bibliotecas como **NumPy**, **Pandas**, **Matplotlib**, **Seaborn** e **Statsmodels**. Os projetos simulam cenários reais de aplicação em ciência de dados e engenharia.

---

## 📊 Análise de Resistência de Materiais (`analise_resistencia_material.py`)

- **Objetivo:** Avaliar a distribuição de dados de resistência (MPa) em amostras, com cálculo de média, mediana, moda, variância e intervalo de confiança.  
- **Métodos:** Estatística descritiva, histograma, boxplot e distribuição em classes de frequência.  
- **Resultado:** A análise identificou variabilidade significativa nos valores, com assimetria positiva e presença de outliers, reforçando a importância de controles de qualidade.

---

## 📈 Regressão Linear Múltipla em Desempenho Acadêmico (`regressao_desempenho_academico.py`)

- **Objetivo:** Estudar o impacto de variáveis como **horas de estudo**, **aulas assistidas** e **experiência prévia** sobre a nota final de estudantes.  
- **Métodos:** Regressão linear múltipla (OLS) com testes de significância global (F) e individuais (t).  
- **Resultado:** Todas as variáveis se mostraram significativas (p < 0.05). Horas de estudo teve maior impacto (+2.5 pontos por hora), seguido de experiência prévia (+3.0 por nível). O modelo apresentou alto poder explicativo (R² > 0.9).

---

## 🏭 Análises Estatísticas Industriais (`analises_estatisticas_industriais.py`)

Inclui diferentes estudos aplicados a cenários industriais:

1. **Lâmpadas** → duração média estimada em ~115 mil horas, com intervalo de confiança de 98%.  
2. **Teste de Fadiga** → ciclos até falha com desvio padrão reduzido em amostra de 25 unidades.  
3. **Anéis Industriais** → 68% dos anéis dentro da especificação; preço médio de venda ≈ \$22.  
4. **Pistões** → maior precisão ao aumentar tamanho amostral (n=64 mais confiável que n=16).  
5. **Safra de Soja** → forte correlação entre nitrogênio aplicado e produção (R² ≈ 98%), confirmando ajuste de regressão linear.  

- **Conclusão geral:** A aplicação de métodos estatísticos possibilitou quantificar variabilidade, estimar parâmetros com confiança e apoiar decisões em diferentes contextos industriais e agrícolas.

---

## 🚀 Tecnologias Utilizadas
- Python 3
- NumPy, Pandas
- Matplotlib, Seaborn
- SciPy, Statsmodels

---

## 📂 Estrutura
projetos_estatistica/
│── analise_resistencia_material.py
│── regressao_desempenho_academico.py
│── analises_estatisticas_industriais.py
│── README.md
│── /graficos (contém imagens geradas .png)

---

## ✍️ Autor
**Isaque Carvalho Silva**  
Estudante de Ciência de Dados (PUC-GO), com experiência prática em estatística, automação com IA e desenvolvimento web.  
[GitHub](https://github.com/zzaakkaass)
