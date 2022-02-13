import numpy as np


#Matrix Factorization function.
def mat_factorization(mat, user_features, item_features, features, epoch=1000, alpha=0.002, beta=0.02):
    for val in range(epoch):
        for value in range(len(mat)):
            for values in range(len(mat[value])):
                if mat[value][values] > 0:
                    error_mat = mat[value][values] - np.dot(user_features[value,:], item_features[:, values]) # To find the error between the original given matrix and the matrices obtained from the rand function.

                    for data in range(features):
                        user_features[value][data] = user_features[value][data] + alpha * (2 * item_features[data][values] * error_mat - beta * user_features[value][data]) # Using the gradient descent function to reduce the error between matrices
                        item_features[data][values] = item_features[data][values] + alpha * (2 * user_features[value][data] * error_mat - beta * item_features[data][values])

    return user_features, item_features.T

size = []

sizes = input("Enter the size of matrix as row, column") #Taking the matrix input from the user.
sizes = sizes.split(",")
for keys in sizes:
    size.append(int(keys))
print(size)
row = []
mat = []

for value in range(size[0]):
    print("Enter the row", value+1)
    for values in range(size[1]):
        row.append(int(input()))
    mat.append(row)
    row = []

print("Input Matrix")
print(mat)

features = 3

user_features = np.random.rand(len(mat), features) # Initializing the user and item matrix using the np.random.rand function.
item_features = np.random.rand(features, len(mat[0]))

user_mat, item_mat = mat_factorization(mat, user_features, item_features, features)

final_mat = np.dot(user_mat, item_mat.T)

print("User Matrix and Item Matrix")
print(user_mat,"\n", item_mat)
print("final matrix")
print(final_mat)