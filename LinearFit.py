import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


def main():
    pixel = []
    f1 = open("./data/pixel.txt", "r")
    for line in f1.readlines():
        line = line.rstrip("\n")
        pixel.append(float(line))

    real = []
    f2 = open("./data/real.txt", "r")
    for line in f2.readlines():
        line = line.rstrip("\n")
        real.append(float(line))

    X = np.array(pixel)[:, np.newaxis]
    y = np.array(real)
    clf = linear_model.LinearRegression()
    clf.fit(X, y)
    y_pred = clf.predict(X)
    print clf.coef_
    print clf.intercept_

    plt.scatter(pixel, real, s=10, c="b")
    plt.plot(pixel, y_pred, "r")
    plt.show()

def test():
    x = np.array(range(600))
    y1 = x * 1.816 + 2046.33
    y2 = x * 0.942 + 2366.73
    plt.plot(y1, "r")
    plt.plot(y2, "b")
    plt.show()


if __name__ == '__main__':
    test()
