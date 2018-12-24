from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import pylab



mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
# 每一幅图就是一行784(28X28)列的数据，括号中的每一个值代表一个像素
# print('输入数据：', mnist.train.images)
# print('输入数据的shape:', mnist.train.images.shape)

# im = mnist.train.images[1]
# im = im.reshape(-1, 28)
# pylab.imshow(im)
# pylab.show()


tf.reset_default_graph()
# 定义占位符
x = tf.placeholder(tf.float32, [None, 784])   # None表示此张量的第一个维度可以时任意长度的
y = tf.placeholder(tf.float32, [None, 10])

# 模型参数
W = tf.Variable(tf.random_normal(([784,10])))
b = tf.Variable(tf.zeros([10]))

# 正向传播
pred = tf.nn.softmax(tf.matmul(x, W) + b)   # Softmax分类

# 反向
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
# 交叉熵运算

# 定义参数
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)


# #######################################
training_epochs = 25  # 把整个训练样本集迭代25次
batch_size = 100      # 代表在训练过程中一次取100条数据进行训练
display_step = 1      # 代表每训练一次就把具体的中间状态显示出来

# 启动session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # 启动循环开始训练
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples/batch_size)
        # 循环所有数据集
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # 运行优化器
            _, c = sess.run([optimizer, cost], feed_dict={x:batch_xs, y:batch_ys})
            # 计算平均损失
            avg_cost += c / total_batch
        # 显示训练中的详细信息
        if (epoch+1) % display_step == 0:
            print('Epoch:', '%04d' % (epoch+1), 'cost=', "{:.9f}".format(avg_cost))
    print('Finished!')





