# coding=gbk
import numpy as np
import matplotlib.pyplot as plt

# 定义函数
# 输入参数：矩阵A，矩阵B
# 输出参数：矩阵X
# 求解矩阵X使得X*A=B
def mat_solve(A, B):
    # 求A的逆矩阵
    A_inv = np.linalg.inv(A)
    # 求解矩阵X
    X = np.dot(B, A_inv)
    # 检验X是否为酉矩阵
    if np.allclose(np.dot(X, X.T.conj()), np.eye(X.shape[0])):
        print("X为酉矩阵")
    else:
        print("X不是酉矩阵")
        exit(0)
    return X

if __name__ == "__main__":
    A = [[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]
    # 对A进行转置
    A = np.transpose(A)
    B = [[1, 1, -1, 1], [1, 1, 1, -1], [1, -1, 1, 1], [-1, 1, 1, 1]]
    # 对B进行转置
    B = np.transpose(B)
    # 求解矩阵X
    X = mat_solve(A, B)
    print("对应的酉矩阵为:\n", X)
    print(np.dot(X, A))