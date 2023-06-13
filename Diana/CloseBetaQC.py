
import isq
from isq import LocalDevice, QcisDevice
from isq import quantumCor
from ezQpy import *
import copy


"""
the test file for Diana encryption scheme
date: 2023-6-13
author: Liheng Luo Mingxin Yang
using command: python/python3 CloseBetaQC.py
"""

pi = 3.1415

a_list = np.array([[0.5, -0.5, -0.5, -0.5], [0.5, 0.5, -0.5, 0.5], [0.5, -0.5, 0.5, 0.5], [0.5, 0.5, 0.5, -0.5]])
a_order = np.array([0,1,2,3])
a_input0 = np.array([0,0,0,0])
a_input1 = np.array([0,0,0,0])
a_cnt0 = 0
a_cnt1 = 0

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

# 实现对于映射关系的存储
# params Matrix: 用于存储映射关系的矩阵
# params order: 用于存储映射关系的顺序
# params m_input: 用于存储映射关系的输入
# params len: 用于存储映射关系的长度
# params ct1: 用于存储映射关系的第一个输入
# params ct2: 用于存储映射关系的第二个输入
def save(ct1, ct2, Matrix, order, m_input, len):
    if m_input[ct2] == 1:
        if order[ct2] == ct1:
            return Matrix
        print("save error.")
        return Matrix
    for i in range(len):
        if ct1 == order[i]:
            ct1_index = i
            # print(i)
    new_Matrix = np.copy(Matrix)
    ct2_list = np.copy(new_Matrix[ct2])
    # print(ct2_list)
    new_Matrix[ct2] = new_Matrix[ct1_index]
    new_Matrix[ct1_index] = ct2_list
    # print(new_Matrix)
    ct2_order = np.copy(order[ct2])
    order[ct2] = order[ct1_index]
    order[ct1_index] = ct2_order
    m_input[ct2] = 1
    return new_Matrix

# 实现对于量子电路的构造
# param: bit_len: 量子比特数
# param: bit: 量子比特
# param: matrix: 量子门矩阵
# return: isq_str: 量子电路字符串
def circuit(bit_len, bit: list, matrix):
    # 根据量子比特数，初始化量子比特
    isq_str = '''qbit '''
    for i in range(bit_len):
        if i != bit_len - 1:
            isq_str += ('Q' + str(i + 1) + ', ')
        else:
            isq_str += ('Q' + str(i + 1) + ';\n')

    tmp = """"""
    # 根据量子比特数，初始化量子门
    for i in range(bit_len):
        if bit[i] == '1':
            tmp += ("X(Q" + str(i + 1) + ');\n')

    isq_str += tmp
    # 根据量子比特数，均权叠加
    for i in range(bit_len):
        isq_str += ('H(Q' + str(i + 1) + ');\n')

    # 设置酉矩阵
    quantumCor.addGate("Rs", matrix)
    # 设置CCZ门
    quantumCor.addGate("CCZ", ccz)

    # 根据量子比特数，设置酉矩阵
    isq_str += ('Rs(')
    for i in range(bit_len):
        if i != bit_len - 1:
            isq_str += ('Q' + str(i + 1) + ', ')
        else:
            isq_str += ('Q' + str(i + 1) + ');\n')

            # 设置迭代过程
    for i in range(bit_len):
        isq_str += ('H(Q' + str(i + 1) + ');\n')
    for i in range(bit_len):
        isq_str += ('X(Q' + str(i + 1) + ');\n')

    # 设置CCZ门
    if bit_len == 2:
        isq_str += ('CZ(Q1, Q2);\n')
    else:
        isq_str += ('CCZ(')
        for i in range(bit_len):
            if i != bit_len - 1:
                isq_str += ('Q' + str(i + 1) + ', ')
            else:
                isq_str += ('Q' + str(i + 1) + ');\n')

    # 设置迭代过程
    for i in range(bit_len):
        isq_str += ('X(Q' + str(i + 1) + ');\n')
    for i in range(bit_len):
        isq_str += ('H(Q' + str(i + 1) + ');\n')

    # 测量过程
    for i in range(bit_len):
        isq_str += ('M(Q' + str(i + 1) + ');\n')

    return isq_str


def readBit():
    bit_in = input("请输入要搜索的密钥哈希值（二进制输入）：")
    return bit_in


# 检测RZ门电路, 传入量子程序, 匹配其中的RZ门和参数
# 例如RZ Q1 3.14156
def check_RZ(isq_qcis: str):
    # 匹配RZ门
    RZ = re.compile(r'RZ\sQ\d*\s\d\.\d+')
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


def run(bit_in, bit_number, matrix, tag):  # bit_number为处理位数输入2或4
    res = ""
    if bit_in == 'Q':
        return bit_in
    if bit_number == 2:
        for i in range(0, 1):
            bit_2 = [bit_in[i * 2], bit_in[i * 2 + 1]]
            print(bit_2)
            # isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], calMatrix)
            isq_str = circuit(2, bit_2, matrix)  # isq_str存储字符串

            if tag == 1:    
                # =============================================isq跑================================================
                # 转换为qcis指令
                ld = LocalDevice()
                ld_res = ld.run(isq_str)
                # print(ld_res)

                # =============================================isq跑================================================
            else:
            # =============================================真机跑================================================
                # print(isq_str)
                ld = LocalDevice()
                ir = ld.compile_to_ir(isq_str, target="qcis")
                account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')
                # account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='应答机A')
                # account.assign_parameters(name="2-bits搜索实验")
                # 拓扑结构映射
                isq_qcis = account.qcis_mapping_isq(ir)
                isq_qcis = check_RZ(isq_qcis)
                query_id_isQ = account.submit_job(circuit=isq_qcis, version="isQ")
                
                if query_id_isQ:
                    ld_res = account.query_experiment(query_id_isQ, max_wait_time=360000)['probability']

            # =============================================真机跑================================================

            m = max(ld_res.values())
            for key, value in ld_res.items():
                if (value == m):
                    res += key
    else:
        for i in range(0, 1):
            bit_2 = [bit_in[i * 4], bit_in[i * 4 + 1], bit_in[i * 4 + 2], bit_in[i * 4 + 3]]
            # isq_str = circuit(bit_in[i * 2], bit_in[i * 2 + 1], calMatrix)
            isq_str = circuit(4, bit_2, matrix)  # isq_str存储字符串
            if tag == 1:    
                # =============================================isq跑================================================
                # 转换为qcis指令
                ld = LocalDevice(2000)
                ld_res = ld.run(isq_str)
                # print(ld_res)

                # =============================================isq跑================================================

            else:
                # =============================================真机跑================================================

                # print(isq_str)
                ld = LocalDevice()
                ir = ld.compile_to_ir(isq_str, target = "qcis")
                account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='ClosedBetaQC')
                # account = Account(login_key='f719ca98fc5ae6ab03580a039bd0289f', machine_name='应答机A')
                # 设置实验名称
                
                # 拓扑结构映射
                isq_qcis = account.qcis_mapping_isq(ir)
                isq_qcis = check_RZ(isq_qcis)
                query_id_isQ = account.submit_job(circuit=isq_qcis,version="isQ")
                
                if query_id_isQ:
                    ld_res = account.query_experiment(query_id_isQ, max_wait_time=360000)['probability']

                # =============================================真机跑================================================

            m = max(ld_res.values())
            for key, value in ld_res.items():
                if (value == m):
                    res += key
    # 将res的高低位互换
    res = res[1]+res[0]
    return res

# define the str of the L and the int of id
dict_L2id = {
    'o0jn0VfPiytFqKTGcyulci64TX74HRyL+ElS5l4PvkI=':'1',
    'ThnNx6gK+07LBwUzGmxcYXBK5LikPRGW7/UrC4gjL+s=':'2',
    '6n1aVPHFxs4NiKYqhsWOv03tg2juq6+NWAmEMXYK0LI=':'3',
    'wvMh232ycRio8CKcyRPNPgZ18F6y2kwfh3PzWIUVPGk=':'4',
    'xzv0PpAd3nGP6PXqjQvb8sdDwwvnPMLJ48viW74nrII=':'5',
    'ktviQzwt7ITgEGhUA89C+8eCxVwcyvru044T+7C96A8=':'6',
    'dxL8iHsHZTdC1sETpX1hIRXDQS6WrVy2oJDya1ESdxM=':'7',
    'zJR7mxiM28vLdHEf4abTfqRY6xTIBDWMUfcuLIjjExk=':'8' 
}
dict_str2int = {}

if __name__ == "__main__":
    
    print("欢迎进入量子比特搜索系统！")
    print("请选择本地模拟或真机运行（输入0为ClosedBetaQC，或1为本地模拟）：", end="")
    mode = int(input())
    if mode == 1:
        print("请输入要搜索的比特数：", end="")
        bit_num = int(input())
        print("请继续输入要搜索的L字符串：（字符串输入，输入Q停止）：")
        cnt = 0
        while True:
            line = input()
            if line == 'Q':
                break
            else:
                line = line.split()
                key = line[0]
                value = line[1]
                if cnt == 0:
                    b_new_list = save(int(key), int(value), b_list, b_order, b_input, 16)
                else:
                    b_new_list = save(int(key), int(value), b_new_list, b_order, b_input, 16)
                cnt += 1
            print("请继续输入要搜索的L字符串：（字符串输入，输入Q停止）：")

        print("现在您可以开始进行搜索！")
        while True:
            res = run(readBit(), 4, b_new_list, mode)
            if res == 'Q':
                break
            print("密钥地址为：", res)

    else:
        print("请输入要搜索的比特数：", end="")
        bit_num = int(input())
        print("请继续输入要搜索的加密数据库索引：（字符串输入，输入Q停止）：")
        cnt = 0
        while True:
            line = input()
            if line == 'Q':
                break
            else:
                key = hash(line)%16
                dict_str2int[line] = key
                print("加密数据库索引的哈希值：",key)
                value = dict_L2id[line]
                print("可搜索密文：",value)
                if cnt == 0:
                    # print(int(key) % 4, int(value) % 4, int(int(key) / 4), int(int(value) / 4))
                    # 获取key高两位
                    key_high = int(key) >> 2
                    # print(key_high)
                    # 获取key低两位
                    key_low = int(key) & 3
                    # print(key_low)
                    # 获取value高两位
                    value_high = int(value) >> 2
                    # print(value_high)
                    # 获取value低两位
                    value_low = int(value) & 3
                    # print(value_low)
                    a_new_list0 = save(key_high, value_high, np.copy(a_list), np.copy(a_order), np.copy(a_input0), 4)
                    # print(a_new_list0)
                    a_new_list1 = save(key_low,  value_low, np.copy(a_list), np.copy(a_order), np.copy(a_input1), 4)
                    # print(a_new_list1)
                else:
                    # 获取key高两位
                    key_high = int(key) >> 2
                    # print(key_high)
                    # 获取key低两位
                    key_low = int(key) & 3
                    # print(key_low)
                    # 获取value高两位
                    value_high = int(value) >> 2
                    # print(value_high)
                    # 获取value低两位
                    value_low = int(value) & 3
                    # print(value_low)
                    a_new_list0 = save(key_high, value_high, a_new_list0, a_order, a_input0, 4)
                    a_new_list1 = save(key_low,  value_low, a_new_list1, a_order, a_input1, 4)
                cnt += 1
            print("请继续输入要搜索的加密数据库索引：（字符串输入，输入Q停止）：")

        print("现在您可以开始进行搜索！")
        while True:
            # print(a_new_list0)
            # print(a_new_list1)
            print("请输入加密数据库索引", end="")
            search = input()
            if search == 'Q':
                break
            search_int = dict_str2int[search]
            # 将search_int转换成四位二进制字符串
            search_int = bin(search_int)[2:]
            search_binary = '0'*(4-len(search_int)) + search_int
            bit_in = search_binary
            # 取字符串前两位
            bit_high = bit_in[:2]
            # 取后两位
            bit_low = bit_in[2:]
            print(bit_high, bit_low)
            print("程序已在量子云平台上运行")
            res0 = run(bit_high, 2, a_new_list0, mode)
            print("搜索结果的高两位为: ",res0)
            res1 = run(bit_low, 2, a_new_list1, mode)
            print("搜索结果的低两位为: ",res1)
            res = res0+res1
            print("文件id的可搜索密文（二进制）为：", res)

            res_int = int(res, 2)
            print("文件id的可搜索密文（十进制）为：", res_int)
        
    
    print("感谢您的使用！")
    # res = run(readBit(), 2, a_new_list)

    
