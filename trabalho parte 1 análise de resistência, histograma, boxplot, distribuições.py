# parte1_analise.py
import numpy as np
import pandas as pd
from scipy import stats
import math
import matplotlib.pyplot as plt
import seaborn as sns

# Dados de resistência
dados = np.array([
    11.5, 12.1, 9.9, 9.3, 7.8, 6.2, 6.6, 7.0, 13.4, 17.1, 9.3, 5.6,
    5.7, 5.4, 5.2, 5.1, 4.9, 10.7, 15.2, 8.5, 4.2, 4.0, 3.9, 3.8,
    3.6, 3.4, 20.6, 25.5, 13.8, 12.6, 13.1, 8.9, 8.2, 10.7, 14.2, 7.6,
    5.2, 5.5, 5.1, 5.0, 5.2, 4.8, 4.1, 3.8, 3.7, 3.6, 3.6, 3.6
])

# Cálculos estatísticos
n = len(dados)
mean = np.mean(dados)
median = np.median(dados)

# Moda (pode ter mais de uma)
vals, counts = np.unique(dados, return_counts=True)
moda = vals[counts == counts.max()]
moda_str = ', '.join(map(str, moda))

var = np.var(dados, ddof=1)
std = np.std(dados, ddof=1)
coef_var = (std / mean) * 100
skewness = stats.skew(dados)
kurt = stats.kurtosis(dados)

# Percentis necessários
percentis_necessarios = [95, 88, 80, 75, 50, 25]  # 100 - p
values = np.percentile(dados, percentis_necessarios)

# Distribuição em classes
bins = [2, 4, 6, 8, 12, 20, 30]
labels = ['2–<4', '4–<6', '6–<8', '8–<12', '12–<20', '20–<30']

# Intervalo de confiança
alpha = 0.05
tcrit = stats.t.ppf(1 - alpha/2, df=n-1)
se = std / math.sqrt(n)
ci_lower = mean - tcrit * se
ci_upper = mean + tcrit * se

# ======================================
# Visualização: Histograma e Boxplot
# ======================================

plt.figure(figsize=(12, 5))

# Histograma
plt.subplot(1, 2, 1)
sns.histplot(dados, bins=bins, kde=True, color='royalblue', edgecolor='white')
plt.title('Distribuição da Resistência', fontweight='bold')
plt.xlabel('Resistência (MPa)')
plt.ylabel('Frequência')
plt.axvline(mean, color='red', linestyle='--', label=f'Média: {mean:.2f}')
plt.axvline(median, color='green', linestyle='--', label=f'Mediana: {median:.2f}')
plt.legend()

# Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(y=dados, color='lightgreen', showfliers=True)
plt.title('Análise de Quartis', fontweight='bold')
plt.ylabel('Resistência (MPa)')

# Adicionar valores
q1, q3 = np.percentile(dados, [25, 75])
plt.text(0.1, q1, f'Q1: {q1:.2f}', va='center', fontweight='bold')
plt.text(0.1, median, f'Mediana: {median:.2f}', va='center', fontweight='bold')
plt.text(0.1, q3, f'Q3: {q3:.2f}', va='center', fontweight='bold')
plt.text(0.1, np.min(dados), f'Mín: {np.min(dados):.2f}', va='center')
plt.text(0.1, np.max(dados), f'Máx: {np.max(dados):.2f}', va='center')

plt.tight_layout()
plt.savefig('analise_resistencia.png', dpi=300)
plt.show()

# ======================================
# Saída de resultados (opcional)
# ======================================
print("="*80)
print("RESULTADOS ESTATÍSTICOS")
print("="*80)
print(f"Média: {mean:.4f} MPa")
print(f"Mediana: {median:.4f} MPa")
print(f"Moda: {moda_str} MPa")
print(f"Desvio Padrão: {std:.4f} MPa")
print(f"Coeficiente de Variação: {coef_var:.2f}%")
print(f"Assimetria: {skewness:.4f}")
print(f"Curtose: {kurt:.4f}")
print(f"IC 95%: [{ci_lower:.4f}, {ci_upper:.4f}] MPa")

# Definir classes conforme o exemplo
bins = [3, 4, 6, 8, 12, 20, 30]
labels = ['3~<4', '4~<6', '6~<8', '8~<12', '12~<20', '20~<30']

# Classificar os dados nas classes
categorias = pd.cut(dados, bins=bins, right=False, labels=labels, include_lowest=True)

# Calcular frequências
freq = pd.value_counts(categorias, sort=False)
freq_acum = freq.cumsum()
freq_rel = freq / len(dados)
freq_perc = freq_rel * 100
amplitude = [bins[i+1]-bins[i] for i in range(len(bins)-1)]
densidade = freq_rel / pd.Series(amplitude, index=labels)
pontos_medios = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]


# Dados de resistência
dados = np.array([
    11.5, 12.1, 9.9, 9.3, 7.8, 6.2, 6.6, 7.0, 13.4, 17.1, 9.3, 5.6,
    5.7, 5.4, 5.2, 5.1, 4.9, 10.7, 15.2, 8.5, 4.2, 4.0, 3.9, 3.8,
    3.6, 3.4, 20.6, 25.5, 13.8, 12.6, 13.1, 8.9, 8.2, 10.7, 14.2, 7.6,
    5.2, 5.5, 5.1, 5.0, 5.2, 4.8, 4.1, 3.8, 3.7, 3.6, 3.6, 3.6
])

# Definir classes conforme o exemplo
bins = [3, 4, 6, 8, 12, 20, 30]
labels = ['3~<4', '4~<6', '6~<8', '8~<12', '12~<20', '20~<30']

# Classificar os dados nas classes
categorias = pd.cut(dados, bins=bins, right=False, labels=labels, include_lowest=True)

# Calcular frequências
freq = pd.value_counts(categorias, sort=False)
freq_acum = freq.cumsum()
freq_rel = freq / len(dados)
freq_perc = freq_rel * 100
amplitude = [bins[i+1]-bins[i] for i in range(len(bins)-1)]
densidade = freq_rel / pd.Series(amplitude, index=labels)
pontos_medios = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]

# Criar tabela formatada
tabela = pd.DataFrame({
    'Classe': labels,
    'Frequência': freq.values,
    'Freq. Acumulada': freq_acum.values,
    'Freq. Relativa': freq_rel.values.round(4),
    'Freq. Percentual (%)': freq_perc.values.round(2),
    'Densidade': densidade.values.round(4),
    'Ponto Médio': pontos_medios
})

# Exibir tabela formatada
print("="*70)
print("DISTRIBUIÇÃO EM CLASSES DE FREQUÊNCIA")
print("="*70)
print(tabela.to_string(index=False))
print("\nLEGENDA:")
print("- Classe: Intervalo de resistência (MPa)")
print("- Frequência: Número de observações na classe")
print("- Freq. Acumulada: Soma cumulativa das frequências")
print("- Freq. Relativa: Frequência dividida pelo total de observações")
print("- Freq. Percentual: Frequência relativa em porcentagem")
print("- Densidade: Frequência relativa dividida pela amplitude da classe")
print("- Ponto Médio: Centro da classe")