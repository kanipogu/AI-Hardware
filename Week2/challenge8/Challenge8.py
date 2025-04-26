import numpy as np
import matplotlib.pyplot as plt

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

class MLP:
    def __init__(self):
        # Random initialization of weights
        self.input_hidden_weights = np.random.randn(2, 2)  # 2 inputs -> 2 hidden neurons
        self.hidden_output_weights = np.random.randn(2)    # 2 hidden -> 1 output
        self.hidden_bias = np.random.randn(2)
        self.output_bias = np.random.randn(1)
        self.lr = 0.1  # Learning rate

    def forward(self, x):
        self.hidden_input = np.dot(x, self.input_hidden_weights) + self.hidden_bias
        self.hidden_output = sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.hidden_output_weights) + self.output_bias
        self.final_output = sigmoid(self.final_input)
        return self.final_output

    def train(self, X, y, epochs=10000):
        losses = []
        for epoch in range(epochs):
            total_loss = 0
            for xi, target in zip(X, y):
                # Forward pass
                output = self.forward(xi)
                loss = (target - output) ** 2
                total_loss += loss

                # Backpropagation
                output_error = target - output
                d_output = output_error * sigmoid_derivative(self.final_input)

                hidden_errors = d_output * self.hidden_output_weights
                d_hidden = hidden_errors * sigmoid_derivative(self.hidden_input)

                # Update weights and biases
                self.hidden_output_weights += self.lr * d_output * self.hidden_output
                self.output_bias += self.lr * d_output
                self.input_hidden_weights += self.lr * np.outer(xi, d_hidden)
                self.hidden_bias += self.lr * d_hidden

            losses.append(total_loss / len(X))

        # Plot loss curve
        plt.plot(losses)
        plt.title("Training Loss Curve")
        plt.xlabel("Epochs")
        plt.ylabel("Loss")
        plt.grid(True)
        # Save the loss curve to a file
        plt.savefig("training_loss_curve.png")
        plt.show()

    def visualize_hidden_activations(self, X):
        activations = []
        for xi in X:
            _ = self.forward(xi)
            activations.append(self.hidden_output)

        activations = np.array(activations)

        plt.figure(figsize=(8,6))
        plt.scatter(activations[:,0], activations[:,1], c='red')
        plt.title("Hidden Neuron Activations")
        plt.xlabel("Hidden Neuron 1 Output")
        plt.ylabel("Hidden Neuron 2 Output")
        plt.grid(True)
        plt.savefig("hidden_activations.png")
        plt.show()


# XOR dataset
XOR_inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

XOR_outputs = np.array([0, 1, 1, 0])

# Initialize and train the MLP
mlp = MLP()
mlp.train(XOR_inputs, XOR_outputs)

# Open a file to save test results
with open("xor_outputs.txt", "w") as f:
    print("\nTesting Trained MLP on XOR:")
    f.write("Testing Trained MLP on XOR:\n")
    for xi, target in zip(XOR_inputs, XOR_outputs):
        output = mlp.forward(xi)
        result = f"Input: {xi} -> Predicted Output: {output} (Expected: {target})\n"
        print(result.strip())  # print on console
        f.write(result)        # write to file

# Visualize hidden neuron activations
mlp.visualize_hidden_activations(XOR_inputs)
