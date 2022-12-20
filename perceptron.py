import numpy as np

X1 = np.array([1, -2, 0, -1], dtype=float)
X2 = np.array([0, 1.5, -0.5, -1], dtype=float)
X3 = np.array([-1, 1, 0.5, -1], dtype=float)

X = np.array([X1, X2, X3], dtype=float)
W = np.array([1, -1, 0, 0.5], dtype=float)

d = np.array([-1, -1, 1], dtype=float)

c = 0.1
epochs = 1

for i in range(epochs):
    for j in range(len(X)):
        net = np.dot(X[j],W)

        if net <=0:
            op = -1
        else:
            op=1

        dW = c * (d[j] - op) * X[j]
        W+=dW

print(W)