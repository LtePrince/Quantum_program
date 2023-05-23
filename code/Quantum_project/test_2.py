# coding=gbk
import isq
from isq import LocalDevice, QcisDevice
from isq import quantumCor
from ezQpy import * 
import copy

pi = 3.1415

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
    RZ = re.compile(r'RZ\sQ\d\s\d\.\d+')
    RZ_list = RZ.findall(isq_qcis)
    # ����RZ_list
    RZ_list_c = copy.deepcopy(RZ_list)

    print(RZ_list)
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
    print(RZ_list)
    # �滻ԭ���ӳ����е�RZ��
    for i in range(len(RZ_list)):
        isq_qcis = isq_qcis.replace(RZ_list_c[i], RZ_list[i])
    print(isq_qcis)
    return isq_qcis


if __name__ == '__main__':
    bit_in = input("����8λ����bit:")
    quantumCor.addGate("Rs", [[0.5, 0.5, 0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, -0.5, -0.5, -0.5]])
    # print("�Ͼ����⣺")
    # print(check_par([[0.5, 0.5, 0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, -0.5, -0.5, -0.5]]))
    # print(quantumCor.check_par("Rs"))
    for i in range(0, 4):
        bit_2 = [bit_in[i * 2], bit_in[i * 2 + 1]]
        isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], calMatrix)
        # print(isq_str)
        ld = LocalDevice()
        ir = ld.compile_to_ir(isq_str, target = "qcis")
        account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')
        
        # ���˽ṹӳ��
        isq_qcis = account.qcis_mapping_isq(ir)
        # print(type(isq_qcis))
        # print(isq_qcis)
        isq_qcis = check_RZ(isq_qcis)

        query_id_isQ = account.submit_job(circuit=isq_qcis,version="Bell_state_isQ")
        

        if query_id_isQ:
            result=account.query_experiment(query_id_isQ, max_wait_time=360000)
            #���ȴ�ʱ�䵥λΪ�룬������ʱĬ��Ϊ30�롣�����ӳ����ִ�л����Ŷӵ�����������Ӽ�����������Զ�У׼��ʱ�䣬�������ȫ�Զ��ĳ��򣬵ȴ�ʱ����ô������ߡ�
            print(result)
            #�������Ӧ��ʵ�֡�

    # # ת��Ϊqcisָ��
    #     ld_res = ld.run(isq_str)
    #     print(ld_res)
    # # ����dict
    # # ��ӡ���ӵ�·
    #     ld.draw_circuit()
    #     ld.draw_circuit(True)
