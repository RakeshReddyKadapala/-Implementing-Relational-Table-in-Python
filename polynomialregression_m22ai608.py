import numpy as np
import matplotlib.pyplot as plt

class PolynomialRegression:
    
    def __init__(self, degree):
        self.degree = degree
        
    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        n = len(X)
        X_poly = np.zeros((n, self.degree+1))
        X_poly[:,0] = 1
        for i in range(1, self.degree+1):
            X_poly[:,i] = X ** i
        self.theta = np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ y
    
    def predict(self, X):
        X = np.array(X)
        n = len(X)
        X_poly = np.zeros((n, self.degree+1))
        X_poly[:,0] = 1
        for i in range(1, self.degree+1):
            X_poly[:,i] = X ** i
        y_pred = X_poly @ self.theta
        return y_pred
    
    def plot_fit(self, X, y):
        plt.scatter(X, y, color='blue')
        x_grid = np.linspace(min(X), max(X), 100)
        y_grid = self.predict(x_grid)
        plt.plot(x_grid, y_grid, color='red')
        plt.title('Polynomial Regression (degree {})'.format(self.degree))
        plt.xlabel('X')
        plt.ylabel('y')
        plt.show()
        

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 5, 8, 12, 17, 23, 30, 38, 47, 57]

degrees = range(1, 11)
errors = []
for degree in degrees:
    model = PolynomialRegression(degree)
    model.fit(X, y)
    y_pred = model.predict(X)
    error = np.sqrt(np.mean((y - y_pred)**2))
    errors.append(error)
    model.plot_fit(X, y)

best_degree = degrees[np.argmin(errors)]
print("Best fitting curve: degree", best_degree)

