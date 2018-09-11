import numpy as np

# 利用mat()函数创建一个示例矩阵
A = np.mat("2 4 6;4 2 6; 10 -4 18")
print("A\n", A)

# 求矩阵的逆
inverse = np.linalg.inv(A)
print("inverse of A\n", inverse)

# 单位矩阵，忽略小误差
print("Check\n", A*inverse)

# 将上面的计算结果减去3x3的单位矩阵，会得到求逆矩阵中出现的误差
print('Error\n', A*inverse - np.eye(3))
# 一般来说，这些误差通常忽略不计，但是在某些情况下，细微的误差也可能导致不良的后果

# 用Numpy解线性方程组
B = np.mat("1 -2 1;0 2 -8;-4 5 9")
print('B\n', B)
b = np.array([0, 8, -9])
print('b\n', b)
x = np.linalg.solve(B, b)
print('Solution', x)
# 利用dot()函数进行验算
print('Chect\n', np.dot(B, x))
# 使用dot()函数来计算两个浮点型数组的点积

# 用NumPy计算特增值和特征向量
A = np.mat('3 -2;1 0')
print('A\n', A)
print('Eigenvalues', np.linalg.eigvals(A))
eigenvalues, eigenvectors = np.linalg.eig(A)
print('First tuple of eig', eigenvalues)
print('Second tuple of eig', eigenvectors)

for i in range(len(eigenvalues)):
    print('Left', np.dot(A, eigenvectors))
    print('Right', eigenvalues[i] * eigenvectors[:, i])
    print()

# # Examples
# x = np.array([[1, 2], [3, 4]])
# m = np.asmatrix(x)
# x[0, 0] = 5
# print(m)


