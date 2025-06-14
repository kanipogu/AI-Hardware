import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid (for learning)
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Perceptron class
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.random.randn(input_size)
        self.bias = np.random.randn()
        self.lr = learning_rate

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias
        output = sigmoid(summation)
        return output

    def train(self, training_inputs, labels, epochs=10000):
        for epoch in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                # Update rule
                self.weights += self.lr * error * inputs
                self.bias += self.lr * error

# Create datasets
NAND_inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
NAND_outputs = np.array([1,1,1,0])

XOR_inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
XOR_outputs = np.array([0,1,1,0])

# Open a file to save the output
with open("output.txt", "w") as f:
    # Train for NAND
    print("Training for NAND...")
    f.write("Training for NAND...\n")
    nand_perceptron = Perceptron(2)
    nand_perceptron.train(NAND_inputs, NAND_outputs)

    print("\nTesting NAND Perceptron:")
    f.write("\nTesting NAND Perceptron:\n")
    for inputs in NAND_inputs:
        output = nand_perceptron.predict(inputs)
        result = f"Input: {inputs} -> Output: {output}\n"
        print(result.strip())  # Also print to screen
        f.write(result)

    # Train for XOR
    print("\nTraining for XOR...")
    f.write("\nTraining for XOR...\n")
    xor_perceptron = Perceptron(2)
    xor_perceptron.train(XOR_inputs, XOR_outputs)

    print("\nTesting XOR Perceptron:")
    f.write("\nTesting XOR Perceptron:\n")
    for inputs in XOR_inputs:
        output = xor_perceptron.predict(inputs)
        result = f"Input: {inputs} -> Output: {output}\n"
        print(result.strip())  # Also print to screen
        f.write(result)
