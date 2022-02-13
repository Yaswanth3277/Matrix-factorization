******Read me******

To execute the program read the following points.
1. The program is in a .py file you can execute the py file using python idle.
2. Once you run the code it will ask you for the size of the matrix you can enter it as row, column for example 3,3
3. After that it will ask to enter the matrix row wise so you can enter the values 1 by 1 for example
	Enter the row 1
	9
	8
	7
	Enter the row 2
	6
	5
	4
	Enter the row 3
	3
	2
	1
4. Once this is done you get 3 outputs. first is the matrix you entered, second the split matrices 
   and third is the final matrix that is the dot product of the split matrices

The Algorithm:

1. First we take the matrix input and then based on dimensions of the matrix we create the user matrix and feature matrix using the numpy.random.rand function.
2. Then we call the matrix_factorization function with the parameters as matrix, user matrix, item matrix, no_of_features.
3. In the function we use first calculate the error between given matrix and the user, item matrix.
4. The we use the gradient descent formula to reduce the error between them to reach the local minimum.
5. These matrices are returned to the main program and printed.
6. The we do a dot product of these 2 matrices which should give us a matrix which is almost equal to the given matrix.

References:

https://albertauyeung.github.io/2017/04/23/python-matrix-factorization.html

https://towardsdatascience.com/understanding-matrix-factorization-for-recommender-systems-4d3c5e67f2c9

https://towardsdatascience.com/recommendation-system-matrix-factorization-d61978660b4b


