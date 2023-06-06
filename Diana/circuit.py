# coding=gbk
import isq
from isq import LocalDevice, QcisDevice
from isq import quantumCor
from ezQpy import *
import copy

pi = 3.1415

a_list = np.array([[0.5, -0.5, -0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, 0.5, 0.5, -0.5]])
a_order = np.array([0,1,2,3])
a_input = np.array([0,0,0,0])
a_cnt = 0

b_list = np.array([[1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],#0000
                   [1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],#0001
                   [1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1],#0010
                   [1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1],#0011
                   [1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1],#0100
                   [1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1],#0101
                   [1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1],#0110
                   [1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1],#0111
                   [1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1],#1000
                   [1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1],#1001
                   [1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1],#1010
                   [1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1],#1011
                   [1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1],#1100
                   [1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1],#1101
                   [1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1],#1110
                   [1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1]]) / 4.0#1111
b_order = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
b_input = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
b_cnt = 0

ccz = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]])

# ʵ�ֶ���ӳ���ϵ�Ĵ洢
# params Matrix: ���ڴ洢ӳ���ϵ�ľ���
# params order: ���ڴ洢ӳ���ϵ��˳��
# params m_input: ���ڴ洢ӳ���ϵ������
# params len: ���ڴ洢ӳ���ϵ�ĳ���
# params ct1: ���ڴ洢ӳ���ϵ�ĵ�һ������
# params ct2: ���ڴ洢ӳ���ϵ�ĵڶ�������
def save(ct1, ct2, Matrix, order, m_input, len):
    if m_input[ct2]==1:
        print("save error, please check the input and reuinput!")
        return Matrix
    for i in range(len):
        if ct1 == order[i]:
            ct1_index = i
            # print(i)
    new_Matrix = np.copy(Matrix)
    ct2_list = np.copy(new_Matrix[ct2])
    # print(ct2_list)
    new_Matrix[ct2]=new_Matrix[ct1_index]
    new_Matrix[ct1_index]=ct2_list
    # print(new_Matrix)
    ct2_order = np.copy(order[ct2])
    order[ct2]=order[ct1_index]
    order[ct1_index]=ct2_order
    m_input[ct2]=1
    print('the quantum circuit updated succesfully!')
    return new_Matrix
    # if(num<=cnt):
    #     new_Matrix = np.copy(Matrix)
    #     tmp = np.copy(Matrix[cnt + num])
    #     for i in range(cnt + num, -1, -1):
    #         if i == cnt:
    #             break
    #         new_Matrix[i] = new_Matrix[i - 1]
    #     new_Matrix[cnt] = tmp
    #     # print(new_Matrix)
    #     return new_Matrix
    # else:
    #     new_Matrix = np.copy(Matrix)
    #     tmp = np.copy(Matrix[num])
    #     for i in range(num, -1, -1):
    #         if i == cnt:
    #             break
    #         new_Matrix[i] = new_Matrix[i - 1]
    #     new_Matrix[cnt] = tmp
    #     return new_Matrix

# ʵ�ֶ������ӵ�·�Ĺ���
# param: bit_len: ���ӱ�����
# param: bit: ���ӱ���
# param: matrix: �����ž���
# return: isq_str: ���ӵ�·�ַ���
def circuit(bit_len, bit: list, matrix):
    # �������ӱ���������ʼ�����ӱ���
    isq_str = '''qbit '''
    for i in range(bit_len):
        if i != bit_len - 1:
            isq_str += ('Q' + str(i + 1) + ', ')
        else:
            isq_str += ('Q' + str(i + 1) + ';\n')

    tmp = """"""
    # �������ӱ���������ʼ��������
    for i in range(bit_len):
        if bit[i] == '1':
            tmp += ("X(Q" + str(i + 1) + ');\n')

    isq_str += tmp
    # �������ӱ���������Ȩ����
    for i in range(bit_len):
        isq_str += ('H(Q' + str(i + 1) + ');\n')

    # �����Ͼ���
    quantumCor.addGate("Rs", matrix)
    # ����CCZ��
    quantumCor.addGate("CCZ", ccz)

    # �������ӱ������������Ͼ���
    isq_str += ('Rs(')
    for i in range(bit_len):
        if i != bit_len - 1:
            isq_str += ('Q' + str(i + 1) + ', ')
        else:
            isq_str += ('Q' + str(i + 1) + ');\n')

            # ���õ�������
    for i in range(bit_len):
        isq_str += ('H(Q' + str(i + 1) + ');\n')
    for i in range(bit_len):
        isq_str += ('X(Q' + str(i + 1) + ');\n')

    # ����CCZ��
    if bit_len == 2:
        isq_str += ('CZ(Q1, Q2);\n')
    else:
        isq_str += ('CCZ(')
        for i in range(bit_len):
            if i != bit_len - 1:
                isq_str += ('Q' + str(i + 1) + ', ')
            else:
                isq_str += ('Q' + str(i + 1) + ');\n')

    # ���õ�������
    for i in range(bit_len):
        isq_str += ('X(Q' + str(i + 1) + ');\n')
    for i in range(bit_len):
        isq_str += ('H(Q' + str(i + 1) + ');\n')

    # ��������
    for i in range(bit_len):
        isq_str += ('M(Q' + str(i + 1) + ');\n')

    return isq_str


def readBit():
    bit_in = input("please input the 4-bits for searching:")
    return bit_in


# ���RZ�ŵ�·, �������ӳ���, ƥ�����е�RZ�źͲ���
# ����RZ Q1 3.14156
def check_RZ(isq_qcis: str):
    # ƥ��RZ��
    RZ = re.compile(r'RZ\sQ\d*\s\d\.\d+')
    RZ_list = RZ.findall(isq_qcis)
    # ����RZ_list
    RZ_list_c = copy.deepcopy(RZ_list)

    # print(RZ_list)
    for i in range(len(RZ_list)):
        RZ_list[i] = RZ_list[i].split(' ')
    # ����б��еĲ����Ƿ�Ϊ����pi, �����, ������滻
    for i in range(len(RZ_list)):
        # print(RZ_list[i])
        if (float(RZ_list[i][2]) > pi):
            RZ_list[i][2] = str(float(RZ_list[i][2]) - 2 * pi)
        if (float(RZ_list[i][2]) < -pi):
            RZ_list[i][2] = str(float(RZ_list[i][2]) + 2 * pi)
        RZ_list[i] = ' '.join(RZ_list[i])
    # print(RZ_list)
    # �滻ԭ���ӳ����е�RZ��
    for i in range(len(RZ_list)):
        isq_qcis = isq_qcis.replace(RZ_list_c[i], RZ_list[i])
    # print(isq_qcis)
    return isq_qcis


def run(bit_in, bit_number, matrix):  # bit_numberΪ����λ������2��4
    res = ""
    if bit_number == 2:
        for i in range(0, 1):
            bit_2 = [bit_in[i * 2], bit_in[i * 2 + 1]]
            # isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], calMatrix)
            isq_str = circuit(2, bit_2, matrix)  # isq_str�洢�ַ���

            # =============================================isq��================================================
            # ת��Ϊqcisָ��
            print("the first isq gate is displayed as follows")
            print(isq_str)
            ld = LocalDevice()
            ld_res = ld.run(isq_str)
            ld.draw_circuit(isq_str)
            # print(ld_res)

            # =============================================isq��================================================

            # =============================================�����================================================
            # print(isq_str)
            # ld = LocalDevice()
            # ir = ld.compile_to_ir(isq_str, target="qcis")
            # account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')
            # # account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='Ӧ���A')
            #
            # # ���˽ṹӳ��
            # isq_qcis = account.qcis_mapping_isq(ir)
            # isq_qcis = check_RZ(isq_qcis)
            # query_id_isQ = account.submit_job(circuit=isq_qcis, version="isQ")
            #
            # if query_id_isQ:
            #     ld_res = account.query_experiment(query_id_isQ, max_wait_time=360000)['probability']

            # =============================================�����================================================

            m = max(ld_res.values())
            for key, value in ld_res.items():
                if (value == m):
                    res += key
    else:
        for i in range(0, 1):
            bit_2 = [bit_in[i * 4], bit_in[i * 4 + 1], bit_in[i * 4 + 2], bit_in[i * 4 + 3]]
            # isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], calMatrix)
            isq_str = circuit(4, bit_2, matrix)  # isq_str�洢�ַ���

            # =============================================isq��================================================
            # ת��Ϊqcisָ��
            print("the first isq gate is displayed as follows")
            print(isq_str)
            ld = LocalDevice(2000)
            ld_res = ld.run(isq_str)
            # draw the circuit
            ld.draw_circuit(isq_str)
            # print(ld_res)

            # =============================================isq��================================================

            # =============================================�����================================================

            #print(isq_str)
            # ld = LocalDevice()
            # ir = ld.compile_to_ir(isq_str, target = "qcis")
            # account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')
            # # account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='Ӧ���A')
            #
            # # ���˽ṹӳ��
            # isq_qcis = account.qcis_mapping_isq(ir)
            # isq_qcis = check_RZ(isq_qcis)
            # query_id_isQ = account.submit_job(circuit=isq_qcis,version="isQ")
            #
            # if query_id_isQ:
            #     ld_res = account.query_experiment(query_id_isQ, max_wait_time=360000)['probability']

            # =============================================�����================================================
            m = max(ld_res.values())
            for key, value in ld_res.items():
                if (value == m):
                    res += key
    return res


if __name__ == "__main__":
    # a_new_list = save(2,a_list,0)
    # a_new_list = save(3, a_new_list, 1)

    b_new_list = save(15, 0, b_list, b_order, b_input, 16)
    b_new_list = save(14, 1, b_new_list, b_order, b_input, 16)
    b_new_list = save(13, 2, b_new_list, b_order, b_input, 16)
    b_new_list = save(12, 3, b_new_list, b_order, b_input, 16)
    b_new_list = save(11, 4, b_new_list, b_order, b_input, 16)
    b_new_list = save(10, 5, b_new_list, b_order, b_input, 16)
    b_new_list = save(9, 6, b_new_list, b_order, b_input, 16)
    b_new_list = save(8, 7, b_new_list, b_order, b_input, 16)
    b_new_list = save(7, 8, b_new_list, b_order, b_input, 16)
    b_new_list = save(6, 9, b_new_list, b_order, b_input, 16)
    b_new_list = save(5, 10, b_new_list, b_order, b_input, 16)
    b_new_list = save(4, 11, b_new_list, b_order, b_input, 16)
    b_new_list = save(3, 12, b_new_list, b_order, b_input, 16)
    b_new_list = save(2, 13, b_new_list, b_order, b_input, 16)
    b_new_list = save(1, 14, b_new_list, b_order, b_input, 16)
    b_new_list = save(0, 15, b_new_list, b_order, b_input, 16)

    res = run(readBit(), 4, b_new_list)
    # res = run(readBit(), 2, a_new_list)

    print(res)