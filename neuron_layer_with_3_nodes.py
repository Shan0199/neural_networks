import random
# basic idea of neural network output calculation
# (inputs)dot_product(weights) + bias

def calculate_output_of_neuron(inputs, list_of_weights, bias):
    output = []
    for weight, bias in zip(list_of_weights, bias):
        output.append(round(sum([inp*weight for inp, weight in zip(inputs, weight)]) + bias, 4))
    return output

def create_random_weights_bias(size = 3):
    weights = [round(random.random()*4, 3) for _ in range(size)]
    bias = round(random.random()* 3, 3)
    return (weights, bias)



INPUTS = [1.3, 5.3, 1.8, 2.4]
# creating 3 weights list and bias for each of them

weight1, bias1 = create_random_weights_bias(size=4)
weight2, bias2 = create_random_weights_bias(size=4)
weight3, bias3 = create_random_weights_bias(size=4)

weights = [weight1, weight2, weight3]
bias = [bias1, bias2, bias3]


print("Inputs: ", INPUTS)
print(f"weight1: {weight1}, bias1: {bias1}")
print(f"weight2: {weight2}, bias2: {bias2}")
print(f"weight3: {weight3}, bias3: {bias3}")

# computing output
print("Output of 3 neurons.")
print(calculate_output_of_neuron(INPUTS, weights, bias))
