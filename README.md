  <h1>1- Definindo uma sequência de DNA</h1>

   <pre> <code>
dna_sequence = "ATCGATCGATCGATCG"

print("Primeiros três nucleotídeos:", dna_sequence[:3])
print("Últimos três nucleotídeos:", dna_sequence[-3:])

print("Número de 'A's na sequência:", dna_sequence.count('A'))

print("Comprimento da sequência:", len(dna_sequence))

dna_sequence += "ATCG"
print("Sequência após adição:", dna_sequence)

dna_sequence = dna_sequence[:-4]
print("Sequência após remoção:", dna_sequence)

    </code> </pre>

  <h1>2- Como encontrar o fluxo máximo de passageiros entre as duas cidades?</h1>

  <pre><code>
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def medir_desempenho(y_real, y_pred, nome_modelo):
    mae = mean_absolute_error(y_real, y_pred)
    print(f'O Erro Médio Absoluto (MAE) para o {nome_modelo} é: {mae}')

def obter_dados_ferroviarios():
    # Supondo que o usuário forneça dados para cada ferrovia conectando cidades intermediárias
    num_ferrovias = int(input("Digite o número de ferrovias que conectam cidades intermediárias: "))
    dados_ferroviarios = []
    for i in range(num_ferrovias):
        capacidade = float(input(f"Digite a capacidade da ferrovia {i+1} (em passageiros/hora): "))
        dados_ferroviarios.append(capacidade)
    return dados_ferroviarios

dados_usuario = obter_dados_ferroviarios()

# Supondo que os dados de capacidade para as ferrovias já estejam disponíveis

X_treino = [
    [200],  # Capacidade da ferrovia 1
    [250],  # Capacidade da ferrovia 2
    [180],  # Capacidade da ferrovia 3
    [220],  # Capacidade da ferrovia 4
    [300],  # Capacidade da ferrovia 5
]

y_treino = [500, 600, 450, 550, 700]  # Exemplo de fluxo máximo de passageiros para cada configuração de ferrovia

normalizador = StandardScaler()
X_treino_normalizado = normalizador.fit_transform(X_treino)

modelo_linear = LinearRegression()
modelo_linear.fit(X_treino_normalizado, y_treino)

dados_usuario = np.array(dados_usuario).reshape(1, -1)  # Reformular dados_usuario para previsão
dados_usuario_normalizado = normalizador.transform(dados_usuario)
previsao_linear = modelo_linear.predict(dados_usuario_normalizado)
previsao_linear_arredondada = round(previsao_linear[0], 2)
print(f'A previsão de fluxo máximo de passageiros (modelo linear) para a configuração de ferrovia fornecida é: {previsao_linear_arredondada} passageiros/hora')

modelo_polinomial = make_pipeline(StandardScaler(), LinearRegression())
modelo_polinomial.fit(X_treino_normalizado, y_treino)

previsao_polinomial = modelo_polinomial.predict(dados_usuario_normalizado)
previsao_polinomial_arredondada = round(previsao_polinomial[0], 2)
print(f'A previsão de fluxo máximo de passageiros (modelo polinomial) para a configuração de ferrovia fornecida é: {previsao_polinomial_arredondada} passageiros/hora')

medir_desempenho([800], [previsao_linear_arredondada], "Modelo Linear")
medir_desempenho([800], [previsao_polinomial_arredondada], "Modelo Polinomial")


    </code></pre>

  <h1>3. Ir de Arad até Bucharest. Qual seria o menor caminho?</h1>

  <img src="https://github.com/Luann8/levantamento-ESTRUTURA-DE-DADOS-Aula-Caio-UV-aula-1/assets/133384636/89ae1631-0e4c-462f-8c81-30e21ff6b4d2" alt="imagem">
</body>
