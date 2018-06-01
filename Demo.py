# Python ML program

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(20)

print(sess.run(a + b))

train_dataSet_url = "http://download.tensorflow.org/data/iris_training.csv"

train_dataSet_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataSet_url), origin=train_dataSet_url)

print("Local copy of the dataset file: {}".format(train_dataSet_fp))

print("Tensorflow")