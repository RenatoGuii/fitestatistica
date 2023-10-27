#  CÓDIGO FEITO NO COLLAB

pip install pandas
import pandas as pd
data = pd.read_csv ('/content/fitestatisticas.csv')
display(data)

# 1 - Análise de Orçamento
import matplotlib.pyplot as plt

distribuicao_orcamento = data['Quanto você estaria disposto a pagar em uma academia?'].value_counts()

# Gráfico
distribuicao_orcamento.plot(kind='bar', color='skyblue')
plt.xlabel('Faixa de Orçamento')
plt.ylabel('Número de Respostas')
plt.title('Distribuição de Faixas de Orçamento para Academia')
plt.xticks(rotation=45)
plt.show()

contagem_suplementacao = data['Você faria uso de Suplementação?'].value_counts()

contagem_suplementacao.plot(kind='bar', color='lightgreen')
plt.xlabel('Uso de Suplementação')
plt.ylabel('Número de Respostas')
plt.title('Demanda por Suplementação na Academia')
plt.xticks(rotation=0)
plt.show()

import seaborn as sns

sns.histplot(data=data, x='Quanto você estaria disposto a pagar em uma academia?', hue='Você faria uso de Suplementação?', multiple='stack', kde=True)
plt.xlabel('Faixa de Orçamento')
plt.ylabel('Número de Respostas')
plt.title('Distribuição de Orçamento em relação à Suplementação')
plt.xticks(rotation=45)
plt.show()

# Se, ao analisar o gráfico de barras empilhadas com a linha KDE, você observa que a maioria das pessoas está disposta a fazer uso de suplementação, independentemente da faixa de
# orçamento para a academia, isso indica que a suplementação é uma preferência comum entre os respondentes.
# Isso pode ser uma conclusão importante para a academia, pois sugere que há uma demanda significativa por serviços relacionados a suplementos, independentemente do orçamento dos
#clientes em potencial. Com base nessa análise, a academia pode considerar estratégias de marketing e serviços relacionados a suplementos para atender a essa demanda.

# 2 - Barreiras a Adesão a Academia

# 1. Proximidade da Academia
proximidade_counts = data['Tem academia perto de sua casa?'].value_counts()
percentagem_sem_academia = (proximidade_counts['Não'] / len(data)) * 100

# 2. Disponibilidade e Turno
turno_counts = data['Qual seria o turno de disponibilidade?'].value_counts()
data['Quantos dias por semana você se disponibilizaria para treinar?'] = data['Quantos dias por semana você se disponibilizaria para treinar?'].str.replace(' por semana', '', regex=True)
dias_semana_counts = data['Quantos dias por semana você se disponibilizaria para treinar?'].value_counts()

# 3. Motivação para Entrar na Academia
motivacao_counts = data['Por qual motivo você entraria na academia?'].value_counts()

# 4. Motivos que Impedem a Idas à Academia
motivos_impedem_counts = data['Qual(is) motivo(s) te impedem de ir para a academia hoje?'].value_counts()

# Visualização das análises
plt.figure(figsize=(16, 8))

# Gráfico de barra para a proximidade da academia
plt.subplot(231)
proximidade_counts.plot(kind='bar', color='skyblue')
plt.title('Proximidade da Academia')
plt.ylabel('Número de Respostas')
plt.xticks(rotation=0)
plt.grid(True)

# Gráfico de barra para dias por semana disponíveis
plt.subplot(233)
dias_semana_counts.plot(kind='bar', color='lightcoral')
plt.title('Dias por Semana Disponíveis')
plt.ylabel('Número de Respostas')
plt.xticks(rotation=0)
plt.grid(True)

# Gráfico de barra para turno de disponibilidade
plt.subplot(232)
turno_counts.plot(kind='bar', color='lightgreen')
plt.title('Turno de Disponibilidade')
plt.ylabel('Número de Respostas')
plt.xticks(rotation=0)
plt.grid(True)

# Gráfico de barra para motivos que impedem a ida à academia
plt.subplot(236)
motivos_impedem_counts.plot(kind='bar', color='yellow')
plt.title('Motivos que Impedem a Ida à Academia')
plt.ylabel('Número de Respostas')
plt.xticks(rotation=50)
plt.grid(True)

# Gráfico de barra para motivação para entrar na academia
plt.subplot(234)
motivacao_counts.plot(kind='bar', color='lightblue')
plt.title('Motivação para Entrar na Academia')
plt.ylabel('Número de Respostas')
plt.xticks(rotation=0)
plt.grid(True)

plt.tight_layout()
plt.show()

print(f"\nPorcentagem de respondentes sem academia próxima: {percentagem_sem_academia:.2f}%")


tabela_contingencia = pd.crosstab([data['Tem academia perto de sua casa?'], data['Por qual motivo você entraria na academia?']], data['Qual seria o turno de disponibilidade?'])

# Gráfico de barras empilhadas para visualizar a relação
tabela_contingencia.plot(kind='bar', stacked=True)
plt.xlabel('Proximidade da Academia e Motivo para Entrar')
plt.ylabel('Número de Respostas')
plt.title('Relação entre Proximidade da Academia, Motivo para Entrar e Turno de Disponibilidade')
plt.xticks(rotation=30)
plt.show()

# É possível observar dois pontos

# 1 - Independentemente da combinação de escolhas, é evidente que o turno da noite é a opção mais amplamente preferida pelos participantes da pesquisa para
# realizar treinamentos. Esta observação sugere a possibilidade de que fatores como obrigações de trabalho e/ou estudos restrinjam a disponibilidade de outros
# horários, levando as pessoas a recorrerem ao turno noturno para a prática de exercícios, possivelmente devido à fadiga resultante dessas responsabilidades,
# o que pode constituir uma barreira à adesão à academia.
