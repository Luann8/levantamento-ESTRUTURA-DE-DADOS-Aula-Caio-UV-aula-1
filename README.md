
 # 1- Defining a DNA sequence
dna_sequence = "ATCGATCGATCGATCG"

print("First three nucleotides:", dna_sequence[:3])
print("Last three nucleotides:", dna_sequence[-3:])

print("Number of 'A's in the sequence:", dna_sequence.count('A'))

print("Length of the sequence:", len(dna_sequence))

dna_sequence += "ATCG"
print("Sequence after addition:", dna_sequence)

dna_sequence = dna_sequence[:-4]
print("Sequence after removal:", dna_sequence)

# 2- Como encontrar o fluxo máximo de passageiros entre as duas cidades?
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def measure_performance(y_real, y_pred, model_name):
    mae = mean_absolute_error(y_real, y_pred)
    print(f'The Mean Absolute Error (MAE) for the {model_name} is: {mae}')

def get_railway_data():
    # Assuming the user provides data for each railway connecting intermediate cities
    num_railways = int(input("Enter the number of railways connecting intermediate cities: "))
    railway_data = []
    for i in range(num_railways):
        capacity = float(input(f"Enter the capacity of railway {i+1} (in passengers/hour): "))
        railway_data.append(capacity)
    return railway_data

user_data = get_railway_data()

#Assuming the capacity data for the railways is already available

X_train = [
    [200],  # Capacity of railway 1
    [250],  # Capacity of railway 2
    [180],  # Capacity of railway 3
    [220],  # Capacity of railway 4
    [300],  # Capacity of railway 5
]

y_train = [500, 600, 450, 550, 700]  # Example maximum passenger flow for each railway configuration

scaler = StandardScaler()
X_train_normalized = scaler.fit_transform(X_train)

linear_model = LinearRegression()
linear_model.fit(X_train_normalized, y_train)

user_data = np.array(user_data).reshape(1, -1)  # Reshape user_data for prediction
user_data_normalized = scaler.transform(user_data)
linear_prediction = linear_model.predict(user_data_normalized)
linear_prediction_rounded = round(linear_prediction[0], 2)
print(f'The maximum passenger flow prediction (linear model) for the provided railway configuration is: {linear_prediction_rounded} passengers/hour')

polynomial_model = make_pipeline(StandardScaler(), LinearRegression())
polynomial_model.fit(X_train_normalized, y_train)

polynomial_prediction = polynomial_model.predict(user_data_normalized)
polynomial_prediction_rounded = round(polynomial_prediction[0], 2)
print(f'The maximum passenger flow prediction (polynomial model) for the provided railway configuration is: {polynomial_prediction_rounded} passengers/hour')

measure_performance([800], [linear_prediction_rounded], "Linear Model")
measure_performance([800], [polynomial_prediction_rounded], "Polynomial Model")

# 3. Image
![image](https://github.com/Luann8/levantamento-ESTRUTURA-DE-DADOS-Aula-Caio-UV-aula-1/assets/133384636/89ae1631-0e4c-462f-8c81-30e21ff6b4d2)

