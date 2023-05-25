# coding=gbk
import isq
from isq import LocalDevice, QcisDevice
from isq import quantumCor
from ezQpy import * 
import copy

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

pi = 3.1415

def calMatrix(a, b, c, d):
    return [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, -0.5, -0.5], [0.5, -0.5, 0.5, -0.5], [-0.5, 0.5, 0.5, -0.5]]
def circuit(bit_1, bit_2, bit_3, bit_4, matrix):
    isq_str = '''qbit a, b, c, d;\n'''
    tmp = """"""
    if bit_1 == '1':
        tmp += ('X(a);\n')
    if bit_2 == '1':
        tmp += ('X(b);\n')
    if bit_3 == '1':
        tmp += ('X(c);\n')
    if bit_4 == '1':
        tmp += ('X(d);\n')
    isq_str += tmp
    isq_str += ('H(a);\nH(b);\nH(c);\nH(d);\n')
    isq_str += ('Rs(a, b, c, d);\n')

    # ���õ�������
    reg = """H(a);\nH(b);\nH(c);\nH(d);\nX(a);\nX(b);\nX(c);\nX(d);\nCCZ(a, b, c, d);\nX(a);\nX(b);\nX(c);\nX(d);\nH(a);\nH(b);\nH(c);\nH(d);\n"""
    # ��������
    cal = ('M(a);\nM(b);\nM(c);\nM(d);\n')
    isq_str += reg
    isq_str += cal
    return isq_str

# ����Ƿ�Ϊ�Ͼ���
def check_par(matrix):
    if (len(matrix) != len(matrix[0])):
        return False
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] != matrix[j][i]):
                    return False
        return True
    
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


if __name__ == '__main__':
    bit_in = input("����8λ����bit:")
    t_list = t_list.tolist()
    # print(t_list)
    quantumCor.addGate("Rs", t_list)
    quantumCor.addGate("CCZ", ccz)
    # print("�Ͼ����⣺")
    # print(check_par([[0.5, 0.5, 0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, -0.5, -0.5, -0.5]]))
    # print(quantumCor.check_par("Rs"))
    for i in range(0, 2):
        isq_str = circuit(bit_in[i * 4], bit_in[i * 4 + 1], bit_in[i * 4 + 2], bit_in[i * 4 + 3], calMatrix)
        print(isq_str)
        ld = LocalDevice()
        ir = ld.compile_to_ir(isq_str, target = "qcis")
        account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')
        
        # ���˽ṹӳ��
        isq_qcis = account.qcis_mapping_isq(ir)
        # print(type(isq_qcis))
        # print(isq_qcis)
        isq_qcis = check_RZ(isq_qcis)
        print(isq_qcis)

        query_id_isQ = account.submit_job(circuit=isq_qcis,version="Bell_state_isQ")

        if query_id_isQ:
            result=account.query_experiment(query_id_isQ, max_wait_time=360000)
            #���ȴ�ʱ�䵥λΪ�룬������ʱĬ��Ϊ30�롣�����ӳ����ִ�л����Ŷӵ�����������Ӽ�����������Զ�У׼��ʱ�䣬�������ȫ�Զ��ĳ��򣬵ȴ�ʱ����ô������ߡ�
            print(result['probability'])
            #�������Ӧ��ʵ�֡�

    # # ת��Ϊqcisָ��
    #     ld_res = ld.run(isq_str)
    #     print(ld_res)
    # # ����dict
    # # ��ӡ���ӵ�·
    #     ld.draw_circuit()
    #     ld.draw_circuit(True)
