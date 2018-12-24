import numpy as np
import tensorflow as tf

# 定义IP和端口
strps_hosts = 'localhost:1681'
strworker_hosts = 'localhost:1682, localhost:1683'

# 定义角色名称
strjob_name = 'ps'
task_index = 0
# 将字符串转成数组
ps_hosts = strps_hosts.split(',')
strworker_hosts = strworker_hosts.split(',')

cluster_spec = tf.train.ClusterSpec({'ps': ps_hosts, 'worker': strworker_hosts})

# 创建server
server = tf.train.Server(
    {'ps': ps_hosts, 'worker': strworker_hosts},
    job_name=strjob_name,
    task_index=task_index
)

# ps角色使用join进行等待
if strjob_name == 'ps':
    print('wait')
    server.join()

# 定义生成loss可视化的函数
plotdata = {'batchsize': [], 'loss': []}
# 生成模拟数据
train_x = np.linspace(-1, 1, 100)
train_y = 2 * train_x + np.random.randn(*train_x.shape) * 0.3

with tf.device(tf.train.replica_device_setter(worker_device='/job:worker/task:%d' % task_index, cluster=cluster_spec)):
    X = tf.placeholder('float')
    Y = tf.placeholder('float')

    # 模型参数
    W = tf.Variable(tf.random_normal([1]), name='weight')
    b = tf.Variable(tf.zeros([1]), name='bias')

    global_step = tf.train.get_or_create_global_step()  # 获得迭代次数

    # 前向结构
    z = tf.multiply(X, W) + b

    tf.summary.histogram('z', z)  # 将预测值以直方图显示

    # 反向优化
    cost = tf.reduce_mean(tf.square(Y - z))

    tf.summary.scalar('loss_function', cost)  # 将损失以标量显示

    learning_rate = 0.01
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost, global_step=global_step)
    # 这样每运行一次优化器，global_step就会自动获得当期迭代次数

    saver = tf.train.Saver(max_to_keep=1)
    # max_to_keep=1代表在迭代过程中只保存一个文件，新生成的模型会覆盖以前的模型
    merged_summary_op = tf.summary.merge_all()  # 合并所有summary

    init = tf.global_variables_initializer()

# ###############################################
# 创建Supervisor，管理Session
# 定义参数
train_epochs = 2200
display_step = 2

sv = tf.train.Supervisor(is_chief=(task_index == 0),  # 0号worker为chief
                         logdir='log/super/',
                         init_op=None,
                         summary_op=None,
                         saver=saver,
                         global_step=global_step,
                         save_model_secs=5)
# is_chief表明了是否为chief supervisors角色，logdir为检查点文件和summary文件保存路径
# init_op表示使用初始化变量的函数，saver需要将保存检查点的saver对象传入，supervisor就会自动保存检查点文件
# summary_op也是自动保存summary文件，save_model_secs为保存检查点文件的时间间隔


# 连接目标角色创建session
with sv.managed_session(server.target) as sess:
    print('sess ok!')
    print(global_step.eval(session=sess))

    for epoch in range(global_step.eval(session=sess), train_epochs * len(train_x)):

        for (x, y) in zip(train_x, train_y):
            _, epoch = sess.run([optimizer, global_step], feed_dict={X: x, Y: y})
            # 生成summary
            summary_str = sess.run(merged_summary_op, feed_dict={X: x, Y: y})
            # 将summary写入文件
            sv.summary_computed(sess, summary_str, global_step=global_step)
            if epoch % display_step == 0:
                loss = sess.run(cost, feed_dict={X: train_x, Y: train_y})
                print('Epoch:', epoch + 1, 'cost=', loss, 'w=', sess.run(W), 'b=', sess.run(b))
                if not (loss == 'NA'):
                    plotdata['batchsize'].append(epoch)
                    plotdata['loss'].append(loss)
        print('Finished!')
        sv.saver(sess, 'log/mnist_with_summaries/' + 'sv.cpk', global_step=epoch)
    sv.stop()



















# c = tf.constant(0.0)
# g = tf.Graph()
#
# with g.as_default():
#     c1 = tf.constant(0.0)
#     # print(c1.graph)
#     # print(g)
#     # print(c.graph)
#
# g2 = tf.get_default_graph()
# # print(g2)
#
# tf.reset_default_graph()
# g3 = tf.get_default_graph()
# # print(g3)
#
#
# a = tf.constant([[1.0, 2.0]])
# b = tf.constant([[1.0], [3.0]])
#
# tensor1 = tf.matmul(a, b, name='exampleop')
# print('name:', tensor1.name)
# print(tensor1)
#
# test = g3.get_tensor_by_name('exampleop:0')
# print(test)
#
# testop = g3.get_operation_by_name('exampleop')
# print(testop)
#
#
# with tf.Session() as sess:
#     test = sess.run(test)
#     print(test)
#     test = tf.get_default_graph().get_tensor_by_name('exampleop:0')
#     print(test)


# print(c1.name)
# t = g.get_tensor_by_name(name='Const: 0')
# print(t)


# with tf.variable_scope('scope2'):
#     var2 = tf.get_variable('v', [1])
#
#     with tf.variable_scope('sp') as sp1:
#         var3 = tf.get_variable('v3', [1])
#         with tf.variable_scope(''):
#             var4 = tf.get_variable('v4', [1])
#
# with tf.variable_scope('scope'):
#     with tf.name_scope('bar'):
#         v = tf.get_variable('v', [1])
#         x = 1.0 + v
#         with tf.name_scope(''):
#             y = 1.0 + v
#
# print('var4:', var4.name)
# print('y.op:', y.op.name)


# with tf.variable_scope('scope1') as sp:
#     var1 = tf.get_variable('v', [1])
#
# print('sp:', sp.name)
# print('var1:', var1.name)
#
#
# with tf.variable_scope('scope2') as sp:
#     var2 = tf.get_variable('v', [1])
#
#     with tf.variable_scope(sp) as sp1:
#         var3 = tf.get_variable('v3', [1])
#
# print('sp1:', sp1.name)
# print('var2:', var2.name)
# print('var3', var3.name)


# with tf.variable_scope('test1', initializer=tf.constant_initializer(0.4)):
#     var1 = tf.get_variable('firstvar', shape=[2], dtype=tf.float32)
#
#     with tf.variable_scope('test2'):
#         var2 = tf.get_variable('firstvar', shape=[2], dtype=tf.float32)
#         var3 = tf.get_variable('var3', shape=[2], initializer=tf.constant_initializer(0.3))
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print('var1=', var1.eval())
#     print('var2=', var2.eval())    # 继承test1初始化
#     print('var3=', var3.eval())


# # 共享变量作用域
# with tf.variable_scope("test1"):     # 定义一个作用域test1
#     var1 = tf.get_variable('firstvar', shape=[2], dtype=tf.float32)
#
#     with tf.variable_scope('test2'):
#         var2 = tf.get_variable('firstvar', shape=[2], dtype=tf.float32)
#
# print('var1:', var1.name)
# print('var2:', var2.name)
#
# with tf.variable_scope('test1', reuse=True):  # reuse实现变量共享
#     var3 = tf.get_variable('firstvar', shape=[2], dtype=tf.float32)
#     with tf.variable_scope('test2'):
#         var4 = tf.get_variable('firstvar', shape=[2], dtype=tf.float32)
# print('var3:', var3.name)
# print('var4:', var4.name)


# var1 = tf.Variable(1.0, name='firstvar')
# print('var1: ', var1.name)
#
# var1 = tf.Variable(2.0, name='firstvar')
# print('var1: ', var1.name)
# var2 = tf.Variable(3.0)
# print('var2: ', var2.name)
#
# var2 = tf.Variable(4.0)
# print('var1: ', var2.name)
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print('var1=', var1.eval())
#     print('var2=',var2.eval())
#
# get_val1 = tf.get_variable('firstvar', [1], initializer=tf.constant_initializer(0.3))
# print('get_var1:', get_val1.name)
#
# get_var1 = tf.get_variable('firstvar1', [1], initializer=tf.constant_initializer(0.4))
# print('get_var1:', get_val1.name)
#
#
# with tf.Session() as sess2:
#     sess2.run(tf.global_variables_initializer())
#     print('get_var1=', get_val1.eval())


# t = [[[[0,1,2,3],
#        [4,5,6,7],
#        [8,9,10,11]],
#        [[12,13,14,15],
#        [16,17,18,19],
#        [20,21,22,23]]]]
#
# print(np.shape(t))
#
# dim = [3]
# rt = tf.reverse(t, dim)
# sess = tf.Session()
# print(sess.run(rt))
#
# r = tf.reverse(t, [1,2])
# print(sess.run(r))

# t = [[[[2], [1]]]]
# t1 = tf.squeeze(t, 0)
# print(np.shape(t))
# print(np.shape(t1))
# sess = tf.Session()
# print(t)
# print(sess.run(t1))
# t2 = tf.squeeze(t, 1)
# print(sess.run(t2))
# t3 = tf.squeeze(t, 3)
# print(sess.run(t3))


# t = [[2,3,3], [1,5,5]]
# sess = tf.Session()
# t1 = tf.expand_dims(t, 0)
# t2 = tf.expand_dims(t, 1)
# t3 = tf.expand_dims(t, 2)
# t4 = tf.expand_dims(t, -1)
# print(t)
# print(t1)
# print('!!!', sess.run(t1))
# print('@@@', sess.run(t2))
# print('###', sess.run(t3))
# print('%%%', sess.run(t4))


# t = [[[[1,1,1], [2,2,2], [3,3,3], [4,4,4]]]]
# sizet = tf.size(t)
# print(tf.shape(t))
# sess = tf.Session()
# print(sess.run(sizet))
#
# rankt = tf.rank(t)
# print(rankt)
# print(sess.run(rankt))


# t = [1,2,3,4,5,6,7,8,9]
# sess = tf.Session()
# tt = tf.reshape(t, [3,3])
# print(sess.run(tt))
#
# ttt = tf.reshape(tt, [1,-1])
# print(sess.run(ttt))
# print(ttt.shape)
# print(tt.shape)
# print(np.shape(t))
# tshape = tf.shape(t)
# tshape2 = tf.shape(tshape)
# print(tshape)
# print(tshape2)
#
# sess = tf.Session()
# print(sess.run(tshape))
# print(sess.run(tshape2))
