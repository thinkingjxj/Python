import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# 定义生成loss可视化的函数
plotdata = {'batchsize':[], 'loss':[]}

def moving_average(a, w=10):
    if len(a) < w:
        return a[:]
    return [val if idx<w else sum(a[(idx-w):idx])/w for idx, val in enumerate(a)]

# 生成模拟数据
train_x = np.linspace(-1, 1, 100)
train_y = 2*train_x + np.random.randn(*train_x.shape)*0.3

# 图形显示
plt.plot(train_x, train_y, 'ro', label='Original data')
plt.legend()
plt.show()


tf.reset_default_graph()

# 创建模型
# 占位符
X = tf.placeholder('float')
Y = tf.placeholder('float')
# 模型参数
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.zeros([1]), name='bias')
# 前向结构
z = tf.multiply(X, W) + b
tf.summary.histogram('z', z)   # 将预测值以直方图形式显示

# 反向优化
cost = tf.reduce_mean(tf.square(Y-z))
tf.summary.scalar('loss_function', cost) # 将损失以标量形式显示
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# 初始化所有变量
init = tf.global_variables_initializer()
# 定义学习参数
train_epochs = 20
display_steps = 2
saver = tf.train.Saver(max_to_keep=1)
savedir = 'log/'
# 启动图
with tf.Session() as sess:
    sess.run(init)

    merged_summary_op = tf.summary.merge_all()  # 合并所有summary
    # 创建summary_writer,用于写文件
    summary_writer = tf.summary.FileWriter('log/mnist_with_summaries', sess.graph)

    # 向模型中输入数据
    for epoch in range(train_epochs):
        for (x, y) in zip(train_x, train_y):
            sess.run(optimizer, feed_dict={X:x, Y:y})

            # 生成summary
            summary_str = sess.run(merged_summary_op, feed_dict={X:x, Y:y})
            summary_writer.add_summary(summary_str, epoch)   # 将summary写入文件


            # 显示训练中的详细信息
            if epoch % display_steps == 0:
                loss = sess.run(cost, feed_dict={X:train_x, Y:train_y})
            print('Epoch:',epoch+1, 'cost=',loss, 'W=',sess.run(W), 'b=',sess.run(b))
            if not (loss == 'NA'):
                plotdata['batchsize'].append(epoch)
                plotdata['loss'].append(loss)
            saver.save(sess, savedir+'linemodel.cpkt', global_step=epoch)

    print('Finished!')

    print('cost=', sess.run(cost, feed_dict={X:train_x, Y:train_y}), 'W=',sess.run(W), 'b=',sess.run(b))

    # 显示模型
    plt.plot(train_x, train_y, 'ro', label='Original data')
    plt.plot(train_x, sess.run(W)*train_x+sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

    plotdata['avgloss'] = moving_average(plotdata['loss'])
    plt.figure(1)
    plt.subplot(211)
    plt.plot(plotdata['batchsize'], plotdata['avgloss'], 'b--')
    plt.xlabel('Minibatch number')
    plt.ylabel('Loss')
    plt.title('Minibatch run vs. Training loss')
    plt.show()


# # 重启一个session, 载入检查点
# load_epoch = 18
# with tf.Session() as sess2:
#     sess2.run(tf.global_variables_initializer())
#     saver.restore(sess2, savedir+'linemodel.cpkt-'+str(load_epoch))
#     print('x=0.2, z=', sess2.run(z, feed_dict={X:0.2}))
#














