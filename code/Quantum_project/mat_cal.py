# coding=gbk
import numpy as np
import matplotlib.pyplot as plt

# ���庯��
# �������������A������B
# �������������X
# ������Xʹ��X*A=B
def mat_solve(A, B):
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
    A = [[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]
    # ��A����ת��
    A = np.transpose(A)
    B = [[1, 1, -1, 1], [1, 1, 1, -1], [1, -1, 1, 1], [-1, 1, 1, 1]]
    # ��B����ת��
    B = np.transpose(B)
    # ������X
    X = mat_solve(A, B)
    print("��Ӧ���Ͼ���Ϊ:\n", X)
    print(np.dot(X, A))