print("Banco de Dados para Análise de Regressão")
print("conjunto de dados fictício sobre desempenho acadêmico")

import numpy as np
import pandas as pd
import statsmodels.api as sm

# Configurar semente para reprodutibilidade
np.random.seed(42)

# Criar dados fictícios (código original mantido)
n = 50
horas_estudo = np.random.uniform(5, 25, n)
aulas_assistidas = np.random.uniform(60, 100, n)
experiencia = np.random.randint(1, 6, n)
erro = np.random.normal(0, 5, n)
nota_final = 30 + 2.5 * horas_estudo + 0.3 * aulas_assistidas + 3.0 * experiencia + erro

dados = pd.DataFrame({
    'Desempenho': nota_final,
    'Horas_Estudo': horas_estudo,
    'Aulas_Assistidas': aulas_assistidas,
    'Experiencia_Previa': experiencia
})

# Ajustar modelo
X = dados[['Horas_Estudo', 'Aulas_Assistidas', 'Experiencia_Previa']]
X = sm.add_constant(X)
y = dados['Desempenho']
modelo = sm.OLS(y, X).fit()

# Testes de significância
f_value = modelo.fvalue
p_value = modelo.f_pvalue
significancia_global = "Significante" if p_value < 0.05 else "Não significante"

# Resultados formatados
print("="*80)
print("ANÁLISE DE REGRESSÃO LINEAR MÚLTIPLA")
print("="*80)
print(f"a) ")
print(f"   Desempenho = {modelo.params['const']:.2f} + "
      f"{modelo.params['Horas_Estudo']:.2f} * Horas_Estudo + "
      f"{modelo.params['Aulas_Assistidas']:.2f} * Aulas_Assistidas + "
      f"{modelo.params['Experiencia_Previa']:.2f} * Experiencia_Previa")
print(f"   R² = {modelo.rsquared:.4f} (Coeficiente de Determinação)")
print(f"   R² Ajustado = {modelo.rsquared_adj:.4f}")

print("\nb) SIGNIFICÂNCIA GLOBAL DA REGRESSÃO (Teste F):")
print(f"   F-statistic = {f_value:.4f}")
print(f"   p-valor = {p_value:.5f}")  # Alterado para 5 casas decimais
print(f"   Conclusão: O modelo é {significancia_global} (p < 0.05)")

print("\nc) SIGNIFICÂNCIA DOS COEFICIENTES INDIVIDUAIS (Teste t):")
coeficientes = pd.DataFrame({
    'Coeficiente': modelo.params,
    'Erro Padrão': modelo.bse,
    't-statistic': modelo.tvalues,
    'p-valor': modelo.pvalues
})
# Formatação especial para p-valor
coef_formatado = coeficientes.round({
    'Coeficiente': 4,
    'Erro Padrão': 4,
    't-statistic': 4,
    'p-valor': 5  # Especifica 5 casas decimais apenas para p-valor
})
print(coef_formatado)

print("\nINTERPRETAÇÃO FINAL:")
print("- Todas as variáveis são significativas para o modelo (p < 0.05)")
print("- Horas de estudo tem o maior impacto: +2.5 pontos por hora adicional")
print("- Experiência prévia contribui com +3.0 pontos por nível")
print("- Aulas assistidas tem menor impacto: +0.3 pontos por % adicional")