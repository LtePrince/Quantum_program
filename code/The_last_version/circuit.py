# coding=gbk
import isq
from isq import LocalDevice, QcisDevice
from isq import quantumCor
from ezQpy import * 
import copy

pi = 3.1415

def calMatrix(a, b, c, d):
    return [[0.5, 0.5, 0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, -0.5, -0.5, -0.5]]

t_list = np.array([[1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1],
         [1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1],
         [1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
         [1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1],
         [1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1],
         [1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1],
         [1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1],
         [1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1],
         [1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1],
         [1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1],
         [1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1],
         [1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1],
         [1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1]]) / 4.0

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

# ʵ�ֶ������ӵ�·�Ĺ���
# param: bit_len: ���ӱ�����
# param: bit: ���ӱ���
# param: matrix: �����ž���
# return: isq_str: ���ӵ�·�ַ���
def circuit(bit_len, bit : list, matrix):
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
    bit_in = input("����8λ����bit")
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


def run(bit_in, bit_number, matrix):  #bit_numberΪ����λ������2��4
    res = ""
    if bit_number == 2:
        for i in range(0, 4):
            bit_2 = [bit_in[i * 2], bit_in[i * 2 + 1]]
        #isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], calMatrix) 
            isq_str = circuit(2, bit_2, matrix) #isq_str�洢�ַ���

            # =============================================isq��================================================
            # ת��Ϊqcisָ��
            ld_res = ld.run(isq_str)
            ld = LocalDevice()
            # print(ld_res)

            # =============================================isq��================================================

            # =============================================�����================================================
        #print(isq_str)
            ld = LocalDevice()
            ir = ld.compile_to_ir(isq_str, target = "qcis")
            account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')
        # account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='Ӧ���A')

        # ���˽ṹӳ��
            isq_qcis = account.qcis_mapping_isq(ir)
            isq_qcis = check_RZ(isq_qcis)
            query_id_isQ = account.submit_job(circuit=isq_qcis,version="isQ")

            if query_id_isQ:
                ld_res = account.query_experiment(query_id_isQ, max_wait_time=360000)['probability']


            # =============================================�����================================================


            m = max(ld_res.values())
            for key, value in ld_res.items():
                if (value == m):
                    res += key
    else:
        for i in range(0, 2):
            bit_2 = [bit_in[i * 4], bit_in[i * 4 + 1],bit_in[i * 4 + 2], bit_in[i * 4 + 3]]
        #isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], calMatrix) 
            isq_str = circuit(4, bit_2, matrix) #isq_str�洢�ַ���

            # =============================================isq��================================================
            # ת��Ϊqcisָ��
            ld = LocalDevice(2000)
            ld_res = ld.run(isq_str)
            # print(ld_res)

            # =============================================isq��================================================

            # =============================================�����================================================
            
        # #print(isq_str)
        #     # ld = LocalDevice()
        #     ir = ld.compile_to_ir(isq_str, target = "qcis")
        #     account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')
        # # account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='Ӧ���A')

        # # ���˽ṹӳ��
        #     isq_qcis = account.qcis_mapping_isq(ir)
        #     isq_qcis = check_RZ(isq_qcis)
        #     query_id_isQ = account.submit_job(circuit=isq_qcis,version="isQ")

        #     if query_id_isQ:
        #         ld_res = account.query_experiment(query_id_isQ, max_wait_time=360000)['probability']


            # =============================================�����================================================
            m = max(ld_res.values())
            for key, value in ld_res.items():
                if (value == m):
                    res += key
    return res
if __name__ == "__main__":
    res = run(readBit(), 4, t_list)
    print(res)