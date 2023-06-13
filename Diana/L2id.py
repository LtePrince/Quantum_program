# encoding in utf-8
from simple_test_Diana import check_binary
import pdb
import Diana
import circuit


"""
the test file for Diana encryption scheme
date: 2023-6-13
author: Liheng Luo
using command: python/python3 L2id.py
"""

# define the str of the L and the int of id
dict_L2id = {
    'o0jn0VfPiytFqKTGcyulci64TX74HRyL+ElS5l4PvkI=':'1',
    'o0jn0VfPiytFqKTGcyulci64TX74HRyL+ElS5l4PvkI=':'2',
    '6n1aVPHFxs4NiKYqhsWOv03tg2juq6+NWAmEMXYK0LI=':'3',
    'wvMh232ycRio8CKcyRPNPgZ18F6y2kwfh3PzWIUVPGk=':'4',
    'xzv0PpAd3nGP6PXqjQvb8sdDwwvnPMLJ48viW74nrII=':'5',
    'ktviQzwt7ITgEGhUA89C+8eCxVwcyvru044T+7C96A8=':'6',
    'dxL8iHsHZTdC1sETpX1hIRXDQS6WrVy2oJDya1ESdxM=':'7',
    'zJR7mxiM28vLdHEf4abTfqRY6xTIBDWMUfcuLIjjExk=':'8' 
}
dict_str2int = {}


if __name__ == '__main__':
    print("欢迎进入量子比特搜索系统！")
    # 一般为1
    print("请选择本地模拟或真机运行（输入0为ClosedBetaQC，或1为本地模拟）：", end="")
    mode = int(input())
    if mode == 1:
        print("请输入要搜索的L字符串：（字符串输入，输入Q停止）：")
        cnt = 0
        while True:
            line = input()
            if line == 'Q':
                break
            else:
                key = hash(line)%16
                dict_str2int[line] = key
                print(key)
                value = dict_L2id[line]
                print(value)
                if cnt == 0:
                    b_new_list = circuit.save(int(key), int(value), circuit.b_list, circuit.b_order, circuit.b_input, 16)
                else:
                    b_new_list = circuit.save(int(key), int(value), b_new_list, circuit.b_order, circuit.b_input, 16)
                cnt += 1
            print("请继续输入要搜索的L字符串：（字符串输入，输入Q停止）：")

        print("现在您可以开始进行搜索！")
        while True:
            print("请输入可搜索密文", end="")
            search = input()
            search_int = dict_str2int[search]
            # 将search_int转换成四位二进制字符串
            search_int = bin(search_int)[2:]
            search_binary = '0'*(4-len(search_int)) + search_int
            print(search_binary)
            # search_int = check_binary(search_int, 4)
            res = circuit.run(search_binary, 4, b_new_list)
            if res == 'Q':
                break
            print("密钥地址为：", res)
            # 将res转换成十进制证书
            res_int = int(res, 2)
            print("文件id：", res_int)

    # else:
    #     print("请输入要搜索的比特数：", end="")
    #     bit_num = int(input())
    #     print("请输入密钥哈希值与地址索引的映射关系（十进制输入，输入Q停止）：")
    #     cnt = 0
    #     while True:
    #         line = input()
    #         if line == 'Q':
    #             break
    #         else:
    #             line = line.split()
    #             key = line[0]
    #             value = line[1]
    #             if cnt == 0:
    #                 # print(int(key) % 4, int(value) % 4, int(int(key) / 4), int(int(value) / 4))
    #                 a_new_list0 = circuit.save(int(key) % 4, int(value) % 4, circuit.a_list, circuit.a_order, circuit.a_input0, 4)
    #                 a_new_list1 = circuit.save(int(int(key) / 4),  int(int(value) / 4), circuit.a_list, circuit.a_order, circuit.a_input1, 4)
    #             else:
    #                 a_new_list0 = circuit.save(int(key) % 4, int(value) % 4, a_new_list0, circuit.a_order, circuit.a_input0, 4)
    #                 a_new_list1 = circuit.save(int(int(key) / 4),  int(int(value) / 4), a_new_list1, circuit.a_order, circuit.a_input1, 4)
    #             cnt += 1

    #     print("现在您可以开始进行搜索！")
    #     while True:
    #         res0 = circuit.run(circuit.readBit(), 2, circuit.a_list, mode)

    #         if res0 == 'Q':
    #             break
    #         res1 = circuit.run(circuit.readBit(), 2, circuit.a_list, mode)
    #         res = res0 + res1
    #         print("密钥地址为：", res)
        
    
    print("感谢您的使用！")