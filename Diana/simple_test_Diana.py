# coding=utf-8
import Diana
import pdb

class check_binary():
	"""docstring for cb.insert"""
	def __init__(self, max_size):
		self.max_size_array = [0]*max_size
		self.max_size = max_size
		self.hash_dic = dict()
	def insert(self,binary_string):
		result = 0
		cnt = 1
		for i in range(0, len(binary_string), 8):
			decimal_value = int.from_bytes(binary_string[i:i+8], byteorder='big')
			if decimal_value % 2 == 0:
				result += cnt
			cnt = cnt <<1
		while  self.max_size_array[result % self.max_size] != 0:
			result= (result + 1) % self.max_size 
		self.max_size_array[result] = 1
		self.hash_dic[binary_string] = result
		return result	

	def get(self,binary_string):
	 	return self.hash_dic[binary_string]	
	

# # dur, ct1, ct2=Diana.Encrypt('114516' , 1, '0')
# # print(cb.insert(ct1))
# # print('x',ca.insert(ct2))
# # dur, ct1, ct2=Diana.Encrypt('114517' , 1, '0')
# # print(cb.insert(ct1))
# # print('x',ca.insert(ct2))
# # dur, ct1, ct2=Diana.Encrypt('114518' , 1, '0')
# # print(cb.insert(ct1))
# # print('x',ca.insert(ct2))
# # dur, ct1, ct2=Diana.Encrypt('114514' , 1, '0')
# # print(cb.insert(ct1))
# # print('x',ca.insert(ct2))
# # dur, ct1, ct2=Diana.Encrypt('114513' , 1, '0')
# # print(cb.insert(ct1))
# # print('x',ca.insert(ct2))
# # dur, ct1, ct2=Diana.Encrypt('114512' , 1, '0')
# # print(cb.insert(ct1))
# # print('x',ca.insert(ct2))
# # dur, ct1, ct2=Diana.Encrypt('114511' , 1, '0')
# # print(cb.insert(ct1))
# # print('x',ca.insert(ct2))
# # dur, ct1, ct2=Diana.Encrypt('2' , 1, '0')
# # print(cb.insert(ct1))
# # print('x',ca.insert(ct2))
# # # pdb.set_trace()



# dur, ownerkey, keyleft, keyright = Diana.Setup()
# cb = check_binary(16)
# ca = check_binary(16) 
# dur, ct1, ct2=Diana.Encrypt('114515' , 1, 'file.txt')
# print(cb.insert(ct1))
# print('x',ca.insert(ct2))
# dur, k2, kc, kdepth = Diana.Trapdoor('114515', 1)
# dur, ctcheck = Diana.Search( 1, k2, kc, kdepth)


# print(cb.insert(ctcheck)-1)

