# coding=gbk
import numpy as np
import matplotlib.pyplot as plt



def mat_define(input_list:list):
    """
    生成映射后的矩阵
    :param input_list: 代映射的列表
    :return:
    """
    mat = np.zeros((4,4))
    for i in range(0,4):
        for j in range(0,4):
            if (input_list[i] == j):
                mat[i][j] = -1
            else:
                mat[i][j] = 1
    return mat


def mat_solve(B):
    """
    计算酉矩阵
    :param A:索引经过叠加后的矩阵，固定
    :param B:映射之后的矩阵，由输入可得
    :return:矩阵X，求解矩阵X使得X*A=B
    """
    # 定义索引矩阵A
    A = [[1, 1, 1, 1],
         [1, 1, -1, -1],
         [1, -1, 1, -1],
         [1, -1, -1, 1]]
    # 对A进行转置
    A = np.transpose(A)
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
    input_list = [3,1,2,0]


    B = mat_define(input_list)
    # print("映射后的矩阵为:\n", B)
    # 对B进行转置
    B = np.transpose(B)
    # 求解矩阵X
    X = mat_solve(B)
    print("对应的酉矩阵为:\n", X)# coding=gbk
import numpy as np
import matplotlib.pyplot as plt



def mat_define(input_list:list):
    """
    生成映射后的矩阵
    :param input_list: 代映射的列表
    :return:
    """
    mat = np.zeros((4,4))
    for i in range(0,4):
        for j in range(0,4):
            if (input_list[i] == j):
                mat[i][j] = -1
            else:
                mat[i][j] = 1
    return mat


def mat_solve(input_list:list):
    """
    计算酉矩阵
    :param A:索引经过叠加后的矩阵，固定
    :param B:映射之后的矩阵，由输入可得
    :return:矩阵X，求解矩阵X使得X*A=B
    """
    # 定义索引矩阵A
    A = [[1, 1, 1, 1],
         [1, 1, -1, -1],
         [1, -1, 1, -1],
         [1, -1, -1, 1]]
    # 对A进行转置
    A = np.transpose(A)
    # 求A的逆矩阵
    A_inv = np.linalg.inv(A)
    B = mat_define(input_list)
    # print("映射后的矩阵为:\n", B)
    # 对B进行转置
    B = np.transpose(B)
    # 求解矩阵X
    X = np.dot(B, A_inv)
    # 检验X是否为酉矩阵
    if np.allclose(np.dot(X, X.T.conj()), np.eye(X.shape[0])):
        pass
        # print("X为酉矩阵")
        print("对应的酉矩阵为:\n", X)
    else:
        print("X不是酉矩阵")
        exit(0)
    return X

if __name__ == "__main__":
    input_list = [3,1,2,0]
    # 求解矩阵X
    X = mat_solve(input_list)
    print("对应的酉矩阵为:\n", X)