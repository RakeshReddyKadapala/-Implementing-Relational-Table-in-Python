import numpy as np

class MultipleLinearRegression:
    
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
    
    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y).reshape(-1, 1)
        m, n = X.shape
        self.theta = np.zeros((n+1, 1))
        X = np.concatenate((np.ones((m, 1)), X), axis=1)
        for i in range(self.num_iterations):
            random_index = np.random.randint(0, m)
            xi = X[random_index:random_index+1]
            yi = y[random_index:random_index+1]
            prediction = np.dot(xi, self.theta)
            gradient = xi.T.dot(prediction - yi)
            self.theta = self.theta - self.learning_rate * gradient
    
    def predict(self, X):
        X = np.array(X)
        m, n = X.shape
        X = np.concatenate((np.ones((m, 1)), X), axis=1)
        return np.dot(X, self.theta)

# create a dataset with 4 features and 1 target
X = np.random.rand(100, 4)
y = np.dot(X, np.array([3, 5, 8, 2]).reshape(-1, 1)) + np.random.randn(100, 1)

# create a model and fit the data
model = MultipleLinearRegression(learning_rate=0.1, num_iterations=10000)
model.fit(X, y)

# predict on new data
X_new = np.random.rand(10, 4)
y_pred = model.predict(X_new)
y_pred
