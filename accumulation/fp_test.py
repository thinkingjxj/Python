import tensorflow as tf

# w1 = tf.Variable(tf.random_normal([2,3], stddev=1, seed=1))
# w2 = tf.Variable(tf.random_normal([3,1], stddev=1, seed=1))
#
# # x = tf.constant([[0.7, 0.9]])
# # tf.placeholder  # 相当于定义了一个位置，这个位置中的数据在程序运行时再指定，数据类型需要指定
# x = tf.placeholder(tf.float32, shape=(3,2), name='inpuut')
#
# a = tf.matmul(x, w1)
# y = tf.matmul(a, w2)
#
# with tf.Session() as sess:
#     # 解决所有变量的初始化过程
#     init_op = tf.global_variables_initializer()
#     sess.run(init_op)
#     print(sess.run(y, feed_dict={x: [[0.7,0.9], [0.1,0.4], [0.5,0.8]]}))
#
#     # 定义损失函数
#     cross_entropy = -tf.reduce_mean(y * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
#     # 学习率
#     learning_rate = 0.001
#     # 定义反向传播算法来优化神经网络中的参数
#     train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)
#
#     print(sess.run(train_step))  # 对所有在GraphKeys.TRAINABLE_VARIABLES集合中的变量进行优化，使得当前batch下损失函数更小
#
# #
# # tf.all_variables   # 可以拿到当前计算图上的所有变量，拿到运算图上的所有变量有助于持久化整个计算图的运行状态
# #
# # tf.GraphKeys.VARIABLES   # 所有的变量会被自动加入到这个集合中
# #
# # tf.trainable_variables  # 得到所有需要优化的参数
# # # TensorFlow中提供的神经网络优化算法会将tf.GraphKeys.TABLE_INITIALIZERS集合中的变量作为默认的优化对象

# from numpy.random import RandomState
#
#
# # 定义训练数据batch的大小
# batch_size = 8
#
#
# w1 = tf.Variable(tf.random_normal([2,3], stddev=1, seed=1))
# w2 = tf.Variable(tf.random_normal([3,1], stddev=1, seed=1))
#
# x = tf.placeholder(tf.float32, shape=(None, 2), name='x_input')
# y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y_input')
# # 在shape的一个维度上使用None可以方便使用不大的batch大小。在训练时需要把数据分成比较小的batch，
# # 但在测试时，可以一次性使用全部的数据。当数据集比较小时这样比较方便测试，
# # 但数据集比较大时，将大量数据放入一个batch可能导致内存溢出
#
# # 定义神经网络前向传播过程
# a = tf.matmul(x, w1)
# y = tf.matmul(a, w2)
# # 定义损失函数和反向传播算法
# cross_entropy = -tf.reduce_mean(y_*tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
# train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
#
# # 通过随机数生成一个模拟数据集
# rdm = RandomState(1)
# dataset_size = 128
# X = rdm.rand(dataset_size, 2)
#
# # 0表示负样本，1表示正样本
# Y = [[int(x1+x2 < 1)] for (x1,x2) in X]
#
#
# with tf.Session() as sess:
#     init_op = tf.global_variables_initializer()
#     sess.run(init_op)
#     # print(sess.run(w1))
#     # print(sess.run(w2))
#
#     '''
#     [[-0.8113182   1.4845988   0.06532937]
#      [-2.4427042   0.0992484   0.5912243 ]]
#
#     [[-0.8113182 ]
#      [ 1.4845988 ]
#      [ 0.06532937]]
#     '''
#     # 设定训练的轮数
#     STEPS = 5000
#     for i in range(STEPS):
#         # 每次选取batch_size个样本进行训练
#         start = (i*batch_size) % dataset_size
#         end = min(start+batch_size, dataset_size)
#         sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
#         if i % 1000 == 0:
#             total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
#             # print("After %d training steps, cross entropy on all data is %g" % (i, total_cross_entropy))
#             '''After 0 training steps, cross entropy on all data is 0.0674925
#             After 1000 training steps, cross entropy on all data is 0.0163385
#             After 2000 training steps, cross entropy on all data is 0.00907547
#             After 3000 training steps, cross entropy on all data is 0.00714436
#             After 4000 training steps, cross entropy on all data is 0.00578471
#             '''
#
#
#     print(sess.run(w1))
#     print(sess.run(w2))
#
#     '''
#     [[-1.9618274  2.582354   1.6820377]
#     [-3.4681718  1.0698233  2.11789  ]]
#     [[-1.8247149]
#      [ 2.6854665]
#      [ 1.418195 ]]
#     '''
#
#
#
# tf.nn.softmax_cross_entropy_with_logits()
# # 分类问题
#
#
# # 回归问题：均方误差；均方误差也是分类问题中常用的一种损失函数
# mse = tf.reduce_mean(tf.square(y_ - y))


v1 = tf.constant([1.0, 2.0, 3.0, 4.0])
v2 = tf.constant([4.0, 3.0, 2.0, 1.0])
sess = tf.InteractiveSession()
print(tf.greater(v1, v2).eval())

print(tf.select(tf.greater(v1, v2), v1, v2).eval())
