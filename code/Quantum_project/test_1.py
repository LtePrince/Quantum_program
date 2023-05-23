
import isq
from isq import LocalDevice, QcisDevice
from isq import quantumCor

def calMatrix(a, b, c, d):
    return [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, -0.5, -0.5], [0.5, -0.5, 0.5, -0.5], [-0.5, 0.5, 0.5, -0.5]]
def circuit(bit_1, bit_2, matrix):
    isq_str = '''0'''
    if (bit_1 == '0' and bit_2 == '0'):
        quantumCor.addGate("Rs", [[0.5, 0.5, 0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, -0.5, -0.5, -0.5]])
        isq_str = '''
        qbit a, b;
        H(a);
        H(b);
        Rs(a, b);
        H(a);
        H(b);
        X(a);
        X(b);
        CZ(a, b);
        X(a);
        X(b);
        H(a);
        H(b);
        M(a);
        M(b);
        '''
    elif (bit_1 == '0' and bit_2 == '1'):
        isq_str = '''
        qbit a, b;
        X(b);
        H(a);
        H(b);
        Rs(a, b);
        H(a);
        H(b);
        X(a);
        X(b);
        CZ(a, b);
        X(a);
        X(b);
        H(a);
        H(b);
        M(a);
        M(b);
        '''
    elif (bit_1 == '1' and bit_2 == '0'):
        isq_str ='''
        qbit a, b;
        X(a);
        H(a);
        H(b);
        Rs(a, b);
        H(a);
        H(b);
        X(a);
        X(b);
        CZ(a, b);
        X(a);
        X(b);
        H(a);
        H(b);
        M(a);
        M(b);
        '''
    elif (bit_1 == '1' and bit_2 == '1'):  
        isq_str =''' 
        qbit a, b;
        X(a);
        X(b);
        H(a);
        H(b);
        Rs(a, b);
        H(a);
        H(b);
        X(a);
        X(b);
        CZ(a, b);
        X(a);
        X(b);
        H(a);
        H(b);
        M(a);
        M(b);'''
    return isq_str

# 检测是否为酉矩阵
def check_par(matrix):
    if (len(matrix) != len(matrix[0])):
        return False
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] != matrix[j][i]):
                    return False
        return True

if __name__ == '__main__':
    bit_in = input("输入8位查找bit:")
    quantumCor.addGate("Rs", [[0.5, 0.5, 0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, -0.5, -0.5, -0.5]])
    # print("酉矩阵检测：")
    # print(check_par([[0.5, 0.5, 0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, -0.5, -0.5, -0.5]]))
    # print(quantumCor.check_par("Rs"))
    for i in range(0, 4):
        bit_2 = [bit_in[i * 2], bit_in[i * 2 + 1]]
        isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], calMatrix)
        print(isq_str)
        ld = LocalDevice(shots=2000)
    # 转换为qcis指令
        ld_res = ld.run(isq_str)
        print(ld_res)
    # 返回dict
    # 打印量子电路
        ld.draw_circuit()
        ld.draw_circuit(True)
