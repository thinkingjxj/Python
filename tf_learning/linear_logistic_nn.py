import numpy as np
import matplotlib.pylab as plt
import tensorflow as tf


def generate(sample_size, mean, cov, diff, regression):
    num_classes = 2
    sample_per_class = int(sample_size/2)

    X0 = np.random.multivariate_normal(mean, cov, sample_per_class)
    Y0 = np.zeros(sample_per_class)

    for ci, d in enumerate(diff):
        X1 = np.random.multivariate_normal(mean+d, cov, sample_per_class)
        Y1 = (ci+1)*np.ones(sample_per_class)

        X0 = np.concatenate((X0, X1))
        Y0 = np.concatenate((Y0, Y1))

    if regression == False:   # one-hot编码，将0转成1 0
        class_ind = [class_number for class_number in range(num_classes)]
        Y = np.asarray(np.hstack(class_ind), dtype=np.float32)
    # X, Y = random.shuffle(X0, Y0)

    return X0, Y0



np.random.seed(10)
num_classes = 2
mean = np.random.randn(num_classes)
cov = np.eye(num_classes)
X, Y = generate(1000, mean, cov, [3.0], True)
colors = ['r' if i == 0 else 'b' for i in Y[:]]

plt.scatter(X[:, 0], X[:, 1], c=colors)
plt.xlabel('Scaled age (in yrs)')
plt.ylabel('Tumor size (in cm)')
plt.show()
lab_dim = 1



input_features = tf.placeholder(tf.float32, [None, input_dim])
input_labels = tf.placeholder(tf.float32, [None, lab_dim])

# 定义学习参数
W = tf.Variable(tf.random_normal([input_dim, lab_dim]), name='weight')
b = tf.Variable(tf.zeros([lab_dim]), name='bias')

output = tf.nn.sigmoid(tf.matmul(input_features, W) + b)
cross_entropy = -(input_labels*tf.log(output) + (1-input_labels) * tf.log(1-output))
ser = tf.square(input_labels - output)
loss = tf.reduce_mean(cross_entropy)
err = tf.reduce_mean(ser)
optimizer = tf.train.AdamOptimizer(0.04)
# 尽量用这个，因其收敛快，会动态调节梯度
train = optimizer.minimize(loss)


# ######################################################
maxeopchs = 50
minibatchsize = 25

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(maxeopchs):
        sumerr = 0

        for i in range(np.int32(len(Y)/minibatchsize)):
            x1 = X[i*minibatchsize:(i+1)*minibatchsize]
            y1 = np.reshape(Y[i*minibatchsize:(i+1):minibatchsize])
            tf.reshape(y1, [-1, 1])
            _, lossval, outputval,errval = sess.run([train, loss, output, err], feed_dict={input_features:x1, input_labels:y1})
            sumerr += errval
            print('epoch:', '%04d' % (epoch+1), 'cost=', '{:.9f}'.format(lossval), 'err=', sumerr/minibatchsize)















