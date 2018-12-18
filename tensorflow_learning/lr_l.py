import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


train_x = np.linspace(-1, 1, 100)
train_y = 2 * train_x + np.random.randn(*train_x.shape) * 0.3

plt.plot(train_x, train_y, 'ro', label='Original data')
plt.legend()
plt.show()

# 占位符
X = tf.placeholder('float')
Y = tf.placeholder('float')

# 模型参数
W = tf.Variable(tf.random_normal([1]), name='Weight')
b = tf.Variable(tf.zeros([1]), name='bias')

# 前向结构
z = tf.multiply(X, W) + b


# 反向优化
cost = tf.reduce_mean(tf.square(Y - z))
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)   # 梯度下降

# 初始化所有变量
init = tf.global_variables_initializer()
# 定义参数
training_epochs = 20
# display_step = 2

# 启动session
with tf.Session() as sess:
    sess.run(init)
    plotdata = {'batchsize':[], 'loss':[]}
    for epoch in range(training_epochs):
        loss = sess.run(cost, feed_dict={X:train_x, Y:train_y})
        print('Epoch: ', epoch+1, 'cost=', loss, 'W=', sess.run(W), 'b=', sess.run(b))
        if not (loss == 'NA'):
            plotdata['batchsize'].append(epoch)
            plotdata['loss'].append(loss)


    print('Finished!')
    print('cost=', sess.run(cost, feed_dict={X: train_x, Y: train_y}), 'W=', sess.run(W), 'b=', sess.run(b))





    plt.plot(train_x, train_y, 'ro', label='Original data')
    plt.plot(train_x, sess.run(W) * train_x + sess.run(b), label='Fittedline')
    plt.legend()
    plt.show()



def moving_average(a, w=10):
    if len(a) < w:
        return a[:]
    return [val if idx<w else sum(a[(idx-w):idx])/w for idx, val in enumerate(a)]




plotdata['avgloss'] = moving_average(plotdata['loss'])
plt.figure(1)
plt.subplot(211)
plt.plot(plotdata['batchsize'], plotdata['avgloss'], 'b--')
plt.xlabel('Minibatch number')
plt.ylabel('Loss')
plt.title('Minibatch run vs. Training loss')
plt.show()

plotdata = {'batchsize':[], 'loss':[]}



inputdict = {
    'x': tf.placeholder('float'),
    'y': tf.placeholder('float')
}


paradict = {
    'w': tf.Variable(tf.random_normal([1])),
    'b': tf.Variable(tf.zeros([1]))
}


z = tf.multiply(X, paradict['w']) + paradict['b']




