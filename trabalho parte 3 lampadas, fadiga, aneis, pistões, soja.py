import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import math

# Configuração de estilo profissional COMPATÍVEL
sns.set_style("whitegrid")  # Estilo corrigido
sns.set_palette("deep")
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 120,
    'figure.figsize': (10, 6)  # Tamanho padrão adicionado
})

#I. Análise de Duração de Lâmpadas
#Objetivo:
#Estimar a duração média de uma marca de lâmpadas com base em uma amostra de 50 unidades.

# Dados fornecidos
n_lampadas = 50
soma_xi = 5764  # mil horas
soma_xi2 = 672016  # (mil horas)^2

# Cálculos estatísticos
media_lamp = soma_xi / n_lampadas
variancia_lamp = (soma_xi2 - (soma_xi**2)/n_lampadas) / (n_lampadas - 1)
desvio_padrao_lamp = math.sqrt(variancia_lamp)
coef_variacao_lamp = (desvio_padrao_lamp / media_lamp) * 100

# Intervalo de confiança (98%)
alpha = 0.02
z_critico = stats.norm.ppf(1 - alpha/2)
erro_padrao = desvio_padrao_lamp / math.sqrt(n_lampadas)
margem_erro = z_critico * erro_padrao
ic_inferior = media_lamp - margem_erro
ic_superior = media_lamp + margem_erro

# Resultados
print("="*80)
print("ANÁLISE DE DURAÇÃO DE LÂMPADAS")
print("="*80)
print(f"Média: {media_lamp:.2f} mil horas")
print(f"Desvio Padrão: {desvio_padrao_lamp:.4f} mil horas")
print(f"Coeficiente de Variação: {coef_variacao_lamp:.2f}%")
print(f"Intervalo de Confiança 98%: ({ic_inferior:.4f}, {ic_superior:.4f}) mil horas")

#II. Teste de Fadiga à Tração
#Objetivo:
#Determinar a distribuição do número médio de ciclos até o início de trincas em corpos de prova.

# Parâmetros populacionais
mu_ciclos = 28000
sigma_ciclos = 5000
n_amostra = 25

# Cálculos
media_esperada = mu_ciclos
desvio_padrao_media = sigma_ciclos / math.sqrt(n_amostra)

# Resultados
print("\n" + "="*80)
print("ANÁLISE DE TESTE DE FADIGA")
print("="*80)
print(f"Valor esperado do número médio de ciclos: {media_esperada}")
print(f"Desvio padrão do número médio de ciclos: {desvio_padrao_media}")

#III. Anéis Industriais
#Objetivo:
#Analisar a qualidade de anéis industriais com base em seu diâmetro e determinar o preço médio de venda.

# Parâmetros populacionais
mu_diametro = 0.10  # cm
sigma_diametro = 0.02  # cm
n_aneis = 22

# a) Percentual dentro das especificações
z_inferior = (0.08 - mu_diametro) / sigma_diametro
z_superior = (0.12 - mu_diametro) / sigma_diametro
percentual_dentro = (stats.norm.cdf(z_superior) - stats.norm.cdf(z_inferior)) * 100

# b) Preço médio de venda
prob_dentro = percentual_dentro / 100
prob_fora = 1 - prob_dentro
preco_medio = prob_dentro * 30 + prob_fora * 5

# c) Intervalo de confiança 99%
alpha = 0.01
z_critico = stats.norm.ppf(1 - alpha/2)
erro_padrao_diam = sigma_diametro / math.sqrt(n_aneis)
margem_erro_diam = z_critico * erro_padrao_diam
ic_inferior_diam = mu_diametro - margem_erro_diam
ic_superior_diam = mu_diametro + margem_erro_diam

# d) Tamanho de amostra necessário
erro_maximo = 0.001
z_95 = stats.norm.ppf(0.975)
n_necessario = ((z_95 * sigma_diametro) / erro_maximo) ** 2

# Resultados
print("\n" + "="*80)
print("ANÁLISE DE ANÉIS INDUSTRIAIS")
print("="*80)
print(f"a) Percentual dentro das especificações: {percentual_dentro:.3f}%")
print(f"b) Preço médio de venda: ${preco_medio:.3f}")
print(f"c) IC 99% para o diâmetro médio: ({ic_inferior_diam:.4f}, {ic_superior_diam:.4f}) cm")
print(f"d) Tamanho de amostra necessário: {math.ceil(n_necessario)}")

#IV. Diâmetro de Pistões
#Objetivo:
#Estudar a distribuição do diâmetro médio de pistões para diferentes tamanhos de amostra.

# Parâmetros populacionais
mu_pistao = 12  # cm
sigma_pistao = 0.04  # cm

# a) Para n=16
n1 = 16
desvio_padrao_media1 = sigma_pistao / math.sqrt(n1)

# b) Para n=64
n2 = 64
desvio_padrao_media2 = sigma_pistao / math.sqrt(n2)

# c) Probabilidade |X - 12| < 0.01
z1_inferior = -0.01 / desvio_padrao_media1
z1_superior = 0.01 / desvio_padrao_media1
prob_n1 = stats.norm.cdf(z1_superior) - stats.norm.cdf(z1_inferior)

z2_inferior = -0.01 / desvio_padrao_media2
z2_superior = 0.01 / desvio_padrao_media2
prob_n2 = stats.norm.cdf(z2_superior) - stats.norm.cdf(z2_inferior)

# Resultados
print("\n" + "="*80)
print("ANÁLISE DE DIÂMETRO DE PISTÕES")
print("="*80)
print(f"a) Para n=16: Distribuição N(12, {desvio_padrao_media1:.4f})")
print(f"b) Para n=64: Distribuição N(12, {desvio_padrao_media2:.4f})")
print(f"c) Probabilidade para n=16: {prob_n1:.4f}")
print(f"   Probabilidade para n=64: {prob_n2:.4f}")
print(f"   A probabilidade é maior para n=64 ({prob_n2:.4f} > {prob_n1:.4f})")

#V. Safra de Soja vs. Nitrogênio
#Objetivo:
#Analisar a relação entre a quantidade de nitrogênio aplicada e a produção de soja.

# Dados fornecidos
dados_soja = {
    'Nitrogenio': [10, 20, 30, 40, 50, 60, 70],  # kg/ha
    'Producao': [1000, 2300, 2600, 3900, 5400, 5800, 6600]  # kg/ha
}
df_soja = pd.DataFrame(dados_soja)

# a) Coeficiente de correlação
correlacao = df_soja.corr().iloc[0, 1]

# b) Regressão linear
X = df_soja['Nitrogenio']
Y = df_soja['Producao']
n = len(X)

soma_x = sum(X)
soma_y = sum(Y)
soma_xy = sum(X * Y)
soma_x2 = sum(X**2)
soma_y2 = sum(Y**2)

a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
b = (soma_y - a * soma_x) / n

# c) Estimativa para 52 kg/ha
producao_estimada = a * 52 + b
tipo_estimativa = "Interpolação" if 10 <= 52 <= 70 else "Extrapolação"

# d) Qualidade do ajuste (R²)
ss_res = sum(Y - (a*X + b))**2
ss_tot = sum((Y - np.mean(Y))**2)
r2 = 1 - (ss_res / ss_tot)

# Visualização
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, s=100, color='darkgreen', edgecolor='black', alpha=0.8)
plt.plot(X, a*X + b, 'r-', linewidth=2, label=f'Y = {a:.1f}X + {b:.1f}')
plt.scatter(52, producao_estimada, s=150, color='red', marker='*', label=f'Estimativa: {producao_estimada:.1f} kg/ha')

plt.title('Relação entre Nitrogênio e Produção de Soja', fontsize=16)
plt.xlabel('Nitrogênio (kg/ha)', fontsize=12)
plt.ylabel('Produção (kg/ha)', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('regressao_soja.png', dpi=150)
plt.show()

# Resultados
print("\n" + "="*80)
print("ANÁLISE DE PRODUÇÃO DE SOJA")
print("="*80)
print(f"a) Coeficiente de correlação: {correlacao:.4f}")
print(f"b) Equação de regressão: Y = {a:.1f}X + {b:.1f}")
print(f"c) Produção estimada para 52 kg/ha: {producao_estimada:.2f} kg/ha ({tipo_estimativa})")
print(f"d) Qualidade do ajuste (R²): {r2:.4f} ({r2*100:.2f}%)")

# Tabela resumo final
resumo = pd.DataFrame({
    'Análise': ['Lâmpadas', 'Fadiga', 'Anéis', 'Pistões (n=16)', 'Pistões (n=64)', 'Soja'],
    'Resultado Chave': [
        'Média=115.28±12.41 mil horas',
        'Média esperada=28000±1000 ciclos',
        '68.27% dentro das especificações',
        'P(|X-12|<0.01)=68.26%',
        'P(|X-12|<0.01)=95.54%',
        'R²=97.96% para Y=95X+143'
    ],
    'Implicações': [
        'Duração média entre 111.19-119.37 mil horas (98% confiança)',
        'Amostra de 25 fornece estimativa precisa',
        'Preço médio de venda $22.07 por anel',
        'Maior variabilidade em amostras menores',
        'Amostras maiores aumentam precisão',
        'Nitrogênio explica 97.96% da variação na produção'
    ]
})

print("\n" + "="*80)
print("RESUMO EXECUTIVO")
print("="*80)
print(resumo.to_string(index=False))