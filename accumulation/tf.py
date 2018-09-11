import tensorflow as tf

# sess = tf.Session()
a = tf.constant([1,2], name='a')
b = tf.constant([2,3], name='b')
# result = tf.add(a,b, name='add')
# print(result.eval(session=sess))
# # print(result)
# # Tensor("add:0", shape=(2,), dtype=int32)
# # 名字，维度，类型。其中0代表result结果的根节点，shape：一维数组长度为2
#
# print(sess.run(result))
# sess.close()
#
# # 利用上下文，防止未关闭session导致资源泄露
# with tf.Session() as sess:
#     # sess.run(result)
#     print(sess.run(result))
#
# # 设置默认回话
# with sess.as_default():
#     print(result.eval())
#
sess = tf.InteractiveSession()
#
# tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
# 第一个参数allow_soft_placement为True时：
    # 1. 运算无法再GPU上执行
    # 2. 没有GPU资源（比如运算被指定在第二个GPU上运行，但机器只要一个GPU）
    # 3. 运算输入包含对CPU计算结果的引用
    # 这个参数默认为False，但为了使得代码的可移植性更强，在没有GPU的环境下这个参数一般会被设置为True
# 第二个参数log_device_placement为True时日志中将会记录每个节点被安排在了哪个设备上以便调试，
# 而在生产环境中将这个参数设置为False可以减少日志量

tf.Variable  # 保存和更新神经网络中测参数
weights = tf.Variable(tf.random_normal([2,3], stddev=2))  # 初始化
print(weights)
tf.Variable(tf.truncated_normal())  # 如果随机出来的值超过2个标准差，那么这个数将会被重新随机



# 变量的值在使用之前，这个变量的初始化过程需要被明确的调用
w2 = tf.Variable(weights.initial_value())
w3 = tf.Variable(weights.initial_value() * 2.0)
biases = tf.Variable(tf.zeros([3]))



