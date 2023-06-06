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

    # set the origin circuit and the Diana
    input_str = input('input the string here:   ')
    dur, ownerkey, keyleft, keyright = Diana.Setup()
    cb = check_binary(16)
    ca = check_binary(16)
    dur, ct1, ct2=Diana.Encrypt(input_str , 1, '0')
    num1 = cb.insert(ct1)
    num2 = ca.insert(ct2)
    print('-----------------------------------------------------')     
    print("the first part of encryption hash number is" ,num1)
    print('the second part of encryption hash number is',num2)
    print('the encrytion is done, the quantum circuit is updateting...')
    new_matrix = circuit.save(num1, num2, circuit.b_list, circuit.b_order, circuit.b_input, 16)
    input_str = input('input next string here:   ')


    while input_str != 'exit':
        print('-----------------------------------------------------')
        dur, ct1, ct2=Diana.Encrypt(input_str , 1, '0')
        num1 = cb.insert(ct1)
        num2 = ca.insert(ct2)
        print("the time of encryption is", dur)
        print("the first part of encryption hash number is" ,num1)
        print('the second part of encryption hash number is',num2)
        print('the encrytion is done, the quantum circuit is updateting...')
        
        list = circuit.save(num1, num2, new_matrix, circuit.b_order, circuit.b_input, 16)

        print('-----------------------------------------------------')
        input_str = input('input next string here:   ')
    print('\n')
    
    bit_in = circuit.readBit()
    while bit_in != 'exit':
        res = circuit.run(bit_in, 4, list)
        print('the binary result from Grover Algroithm is', res)
        # Convert binary string to decimal int
        decimal_value = int(res, 2)
        print('the decimal value is', decimal_value)
        # print('the corresponding string is', cb.get(ct1))
        bit_in = circuit.readBit()
        print('-----------------------------------------------------')
    
    print("Thank you for using the Diana Encryption Scheme!")
    print("See you next time!")
    print("=====================================================")