import numpy as np
import tensorflow as tf



t = [[[[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11]],
       [[12,13,14,15],
       [16,17,18,19],
       [20,21,22,23]]]]

print(np.shape(t))

dim = [3]
rt = tf.reverse(t, dim)
sess = tf.Session()
print(sess.run(rt))

r = tf.reverse(t, [1,2])
print(sess.run(r))







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
