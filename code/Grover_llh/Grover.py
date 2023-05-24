# coding=gbk
import isq
from isq import LocalDevice, QcisDevice
from isq import quantumCor
from ezQpy import *
import copy
from Oracle import *

pi = 3.1415


def circuit(bit_1, bit_2, matrix):
    isq_str = '''0'''
    quantumCor.addGate("Rs",
                       matrix)
    if (bit_1 == '0' and bit_2 == '0'):
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
        isq_str = '''
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
        isq_str = ''' 
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


# 检测RZ门电路, 传入量子程序, 匹配其中的RZ门和参数
# 例如RZ Q1 3.14156
def check_RZ(isq_qcis: str):
    # 匹配RZ门
    RZ = re.compile(r'RZ\sQ\d\s\d\.\d+')
    RZ_list = RZ.findall(isq_qcis)
    # 复制RZ_list
    RZ_list_c = copy.deepcopy(RZ_list)

    # print(RZ_list)
    for i in range(len(RZ_list)):
        RZ_list[i] = RZ_list[i].split(' ')
    # 检查列表中的参数是否为大于pi, 如果是, 则进行替换
    for i in range(len(RZ_list)):
        # print(RZ_list[i])
        if (float(RZ_list[i][2]) > pi):
            RZ_list[i][2] = str(float(RZ_list[i][2]) - 2 * pi)
        if (float(RZ_list[i][2]) < -pi):
            RZ_list[i][2] = str(float(RZ_list[i][2]) + 2 * pi)
        RZ_list[i] = ' '.join(RZ_list[i])
    # print(RZ_list)
    # 替换原量子程序中的RZ门
    for i in range(len(RZ_list)):
        isq_qcis = isq_qcis.replace(RZ_list_c[i], RZ_list[i])
    # print(isq_qcis)
    return isq_qcis


if __name__ == '__main__':
    # 数据库 每个数据用8位字符串表示，共有4个数据
    data = ['11000000', '11010101', '01101010', '00111111']
    bit_in = input("输入8位查找bit:")
    result_list = []
    for i in range(0, 4):
        input = []
        # bit_search = bit_in[i * 2], bit_in[i * 2 + 1]
        for j in range(0, 4):
            # 将i*2和i*2+1位的数据连起来转换成int
            num = int(data[j][i * 2] + data[j][i * 2 + 1], 2)
            input.append(num)
        # print(input)
        isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], mat_solve(input))
        # print(isq_str)

        # 运行量子电路
        ld = LocalDevice()
        ir = ld.compile_to_ir(isq_str, target="qcis")
        account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')

        # 拓扑结构映射
        isq_qcis = account.qcis_mapping_isq(ir)
        # print(type(isq_qcis))
        # print(isq_qcis)
        isq_qcis = check_RZ(isq_qcis)

        query_id_isQ = account.submit_job(circuit=isq_qcis, version="Bell_state_isQ")

        if query_id_isQ:
            result = account.query_experiment(query_id_isQ, max_wait_time=360000)
            # 最大等待时间单位为秒，不传递时默认为30秒。因量子程序的执行会有排队的情况，而量子计算机本身有自动校准的时间，如果想跑全自动的程序，等待时间最好大于两者。
            print(result['probability'])
            # 选取可能性最大的结果, 返回一个tuple,
            result_max = max(result['probability'].items(), key=lambda x: x[1])
            # 加入队列
            result_list.append(result_max[0])
    print(result_list)

    # 判断索引
    # # 若有不一样索引的，则认为该搜索是非法数据
    # if (result_list[0] != result_list[1] or result_list[0] != result_list[2] or result_list[0] != result_list[3]):
    #     print("非法数据")
    # else:
    #     print("数据索引为: ", result_list[0])

    # # 转换为qcis指令
    #     ld_res = ld.run(isq_str)
    #     print(ld_res)
    # # 返回dict
    # # 打印量子电路
    #     ld.draw_circuit()
    #     ld.draw_circuit(True)
