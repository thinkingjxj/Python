import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# MNIST数据集相关的常数
INPUT_NODE = 784  # 输入层的节点数，对于MNIST数据集，这个就等于图片的像素
OUTPUT_NODE = 10  # 输出层的节点数，这个等于类别的数目，
# 因为在MNIST数据集中需要区分的是0~9这10个数字，所以这里输出层的节点数为10

# 配置NN的参数
LAYER1_NODE = 500   #   隐藏层节点数，这里是有只有一个隐藏层的网络，这个隐藏层有500个节点

BATCH_SIZE = 100

LERNING_RATE_BASE = 0.8   # 基础学习率
LEARNING_RATE_DECAY = 0.99   # 学习率的衰减率

REGULARIZATION_RATE = 0.0001    # 正则化项在损失函数中的系数
TRAINING_STEPS = 30000          # 训练轮数
MOVING_AVERAGE_DECAY = 0.99     # 滑动平均衰减率


def inference(input_tensor, avg_class, weights1, bias1, weights2, bias2):
    if avg_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + bias1)
        return tf.matmul(layer1, weights2) + bias2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.averate(weights1)) + avg_class.average(bias1))
        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(bias2)


# 训练模型的过程
def train(mnist):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y_input')
    # 生成隐藏层参数
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))
    # 生成输出层参数
    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))
    # 计算在当前参数下NN前向传播的结果。这里给出的用于计算滑动平均类为None，所有函数不会使用参数的滑动平均值







