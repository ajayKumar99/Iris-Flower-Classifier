#First ML app to classify petals of iris flowers

#Dependencies
import numpy as np
import pandas as pd
import matplotlib as mp
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier


def iris_predictor(sl , sw , pl , pw):

    irisDataset = load_iris()

    X_train , X_test , y_train , y_test = train_test_split(irisDataset['data'] , irisDataset['target'] , random_state = 0)


    knn = KNeighborsClassifier(n_neighbors = 1)

    knn.fit(X_train , y_train)

    prediction = knn.predict(np.array([[sl , sw , pl , pw]]))

    st = irisDataset['target_names'][prediction]

    return st[0]


