# coding=gbk
import numpy as np
import matplotlib.pyplot as plt



def mat_define(input_list:list):
    """
    ����ӳ���ľ���
    :param input_list: ��ӳ����б�
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
    �����Ͼ���
    :param A:�����������Ӻ�ľ��󣬹̶�
    :param B:ӳ��֮��ľ���������ɵ�
    :return:����X��������Xʹ��X*A=B
    """
    # ������������A
    A = [[1, 1, 1, 1],
         [1, 1, -1, -1],
         [1, -1, 1, -1],
         [1, -1, -1, 1]]
    # ��A����ת��
    A = np.transpose(A)
    # ��A�������
    A_inv = np.linalg.inv(A)
    # ������X
    X = np.dot(B, A_inv)
    # ����X�Ƿ�Ϊ�Ͼ���
    if np.allclose(np.dot(X, X.T.conj()), np.eye(X.shape[0])):
        print("XΪ�Ͼ���")
    else:
        print("X�����Ͼ���")
        exit(0)
    return X

if __name__ == "__main__":
    input_list = [3,1,2,0]


    B = mat_define(input_list)
    # print("ӳ���ľ���Ϊ:\n", B)
    # ��B����ת��
    B = np.transpose(B)
    # ������X
    X = mat_solve(B)
    print("��Ӧ���Ͼ���Ϊ:\n", X)# coding=gbk
import numpy as np
import matplotlib.pyplot as plt



def mat_define(input_list:list):
    """
    ����ӳ���ľ���
    :param input_list: ��ӳ����б�
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
    �����Ͼ���
    :param A:�����������Ӻ�ľ��󣬹̶�
    :param B:ӳ��֮��ľ���������ɵ�
    :return:����X��������Xʹ��X*A=B
    """
    # ������������A
    A = [[1, 1, 1, 1],
         [1, 1, -1, -1],
         [1, -1, 1, -1],
         [1, -1, -1, 1]]
    # ��A����ת��
    A = np.transpose(A)
    # ��A�������
    A_inv = np.linalg.inv(A)
    B = mat_define(input_list)
    # print("ӳ���ľ���Ϊ:\n", B)
    # ��B����ת��
    B = np.transpose(B)
    # ������X
    X = np.dot(B, A_inv)
    # ����X�Ƿ�Ϊ�Ͼ���
    if np.allclose(np.dot(X, X.T.conj()), np.eye(X.shape[0])):
        pass
        # print("XΪ�Ͼ���")
        print("��Ӧ���Ͼ���Ϊ:\n", X)
    else:
        print("X�����Ͼ���")
        exit(0)
    return X

if __name__ == "__main__":
    input_list = [3,1,2,0]
    # ������X
    X = mat_solve(input_list)
    print("��Ӧ���Ͼ���Ϊ:\n", X)