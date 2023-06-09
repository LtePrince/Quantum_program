# encoding in utf-8
from simple_test_Diana import check_binary
import pdb
import Diana
import circuit

"""
the test file for Diana encryption scheme
date: 2023-6-5
author: Liheng Luo
using command: python/python3 test_quantum.py
"""


if __name__ == '__main__':
    print("Welcome to the Diana Encryption Scheme!")
    print("=====================================================")
    print("Please input the updatetoken you want to encrypt:")
    print("Tips: input \"exit\" to exit the program")

    dict = {}
    # set the origin circuit and the Diana
    input_str = input('input the keyword here:   ')
    input_fileid = input('input the file id here:   ')
    dur, ownerkey, keyleft, keyright = Diana.Setup()
    cb = check_binary(16)
    ca = check_binary(16)
    cc = check_binary(16)
    dur, ct1, ct2=Diana.Encrypt(input_str , 1, input_fileid)
    num1 = cb.insert(ct1)
    num2 = ca.insert(ct2)
    dict[input_str] = num1
    print('-----------------------------------------------------')     
    print("the token number of keyword is" ,num1)
    print('the encrypted file id is',num2)
    print('the encrytion is done, the quantum circuit is updateting...')
    new_matrix = circuit.save(num1, num2, circuit.b_list, circuit.b_order, circuit.b_input, 16)
    input_str = input('input next keyword here:   ')
    while input_str != 'exit':
        
        input_fileid = input('input next file id here:   ')
        print('-----------------------------------------------------')
        dur, ct1, ct2=Diana.Encrypt(input_str , 1, input_fileid)
        num1 = cb.insert(ct1)
        num2 = ca.insert(ct2)
        dict[input_str] = num1
        print("the time of encryption is", dur)
        print("the token number of keyword is" ,num1)
        print('the encrypted file id is',num2)
        print('the encrytion is done, the quantum circuit is updateting...')
        
        list = circuit.save(num1, num2, new_matrix, circuit.b_order, circuit.b_input, 16)

        print('-----------------------------------------------------')
        input_str = input('input next keyword here:   ')
        

    print('\n')
    
    input_keyword = input("please input the keyword!:    ")
    # bit_in = circuit.readBit()
    # bit_in = dict[input_keyword]
    dur, k2, kc, kdepth = Diana.Trapdoor(input_keyword, 1)
    dur, ctcheck = Diana.Search( 1, k2, kc, kdepth)
    num_bit = cc.insert(ctcheck)
    # if num_bit == 0: 
    #     bit_in = 15
    # else:
    #     bit_in = num_bit - 1
    bit_in = num_bit
    # convert bit_in to 4-bits binary string
    bit_in = bin(bit_in)[2:]
    bit_in = '0'*(4-len(bit_in)) + bit_in
    print('the binary input is', bit_in)
    while bit_in != 'exit':
        res = circuit.run(bit_in, 4, list)
        print('the binary result from Grover Algroithm is', res)
        # Convert binary string to decimal int
        decimal_value = int(res, 2)
        print('the file id number is', decimal_value)
        # print('the corresponding string is', cb.get(ct1))
        # bit_in = circuit.readBit()
        input_keyword = input("please input the next keyword!:    ")
        # bit_in = circuit.readBit()
        dur, k2, kc, kdepth = Diana.Trapdoor(input_keyword, 1)
        dur, ctcheck = Diana.Search( 1, k2, kc, kdepth)
        num_bit = cc.insert(ctcheck)
        # if num_bit == 0: 
        #     bit_in = 15
        # else:
        #     bit_in = num_bit - 1
        bit_in = num_bit
        # convert bit_in to 4-bits binary string
        bit_in = bin(bit_in)[2:]
        bit_in = '0'*(4-len(bit_in)) + bit_in
        print('the binary input is', bit_in)
        print('-----------------------------------------------------')
    
    print("Thank you for using the Diana Encryption Scheme!")
    print("See you next time!")
    print("=====================================================")