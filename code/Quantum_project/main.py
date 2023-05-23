from isq import LocalDevice, QcisDevice
from ezQpy import *

# 本地测试
isq_str = '''
    qbit q[2];
    X<q[0]>;
    CNOT<q[0], q[1]>;
    M<q[0,1]>;
    '''

# local device
ld = LocalDevice(shots=200)
# 转换为qcis指令
ir = ld.compile_to_ir(isq_str, target="qcis")
print(ir)
# 返回dict
ld_res = ld.run(isq_str)
print(ld_res)

# 以下为远程平台测试的方法，一共提供两种方式，每次运行只能选择其中一种方式运行
isq_qcis='''
    X Q1
    Y2P Q2
    CZ Q1 Q2
    Y2M Q2
    M Q1
    M Q2
    '''
# 1、使用转换后的QCIS并指定运行机器运行程序
account = Account(login_key='3a04cbeef74fa6ec481581b56030708a', machine_name='应答机A')

# 拓扑结构映射
isq_qcis = account.qcis_mapping_isq(isq_qcis)

query_id_isQ = account.submit_job(circuit=isq_qcis, version="Bell_state_isQ")
if query_id_isQ:
    result = account.query_experiment(query_id_isQ, max_wait_time=360000)
    # 最大等待时间单位为秒，不传递时默认为30秒。因量子程序的执行会有排队的情况，而量子计算机本身有自动校准的时间，如果想跑全自动的程序，等待时间最好大于两者。
    print(result)
    # 后继数据应用实现。

# 2、直接使用外部ISQ文件开始运行程序
#qd = QcisDevice(user="Adolph", passwd="Wzy20031003", max_wait_time=360000)
# 返回ISQTask
#task = qd.run(file='./test.isq')
# 输出状态和结果
#print(task.state)
#print(task.result())


# 当测量比特超过10个时，量子计算机端就不再为用户做结果的概率统计和读取矫正，需要用户自行处理。
# probability_whole=account.readout_data_to_state_probabilities_whole(result)
# print(probability_whole)
# probability_part=account.readout_data_to_state_probabilities_part(result)
# print(probability_part)


