<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
</head>
<body>
    <h1>Python Code Examples and Image</h1>

    <h2>1. DNA Sequence Manipulation</h2>
    <pre><code># Defining a DNA sequence
dna_sequence = "ATCGATCGATCGATCG"

print("First three nucleotides:", dna_sequence[:3])
print("Last three nucleotides:", dna_sequence[-3:])

print("Number of 'A's in the sequence:", dna_sequence.count('A'))

print("Length of the sequence:", len(dna_sequence))

dna_sequence += "ATCG"
print("Sequence after addition:", dna_sequence)

dna_sequence = dna_sequence[:-4]
print("Sequence after removal:", dna_sequence)
    </code></pre>

    <h2>2. Machine Learning Model for Railway Passenger Flow Prediction</h2>
    <pre><code>import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Define functions and data

user_data = get_railway_data()

# Assuming the capacity data for the railways is already available
X_train = [
    [200],  # Capacity of railway 1
    [250],  # Capacity of railway 2
    [180],  # Capacity of railway 3
    [220],  # Capacity of railway 4
    [300],  # Capacity of railway 5
]

y_train = [500, 600, 450, 550, 700]  # Example maximum passenger flow for each railway configuration

# Rest of the code for model training and prediction
    </code></pre>

    <h2>3. Image</h2>
    <img src="image.jpg" alt="Image Description">

</body>
</html>
