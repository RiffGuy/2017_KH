
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Lab 10 MNIST and Deep learning CNN
import tensorflow as tf
import random
import mfcc
import numpy as np

import glob
from collections import defaultdict

import librosa
import record

import time
tf.set_random_seed(777)  # reproducibility




class CNN():
    def __init__(self):
        self.build()

    def build(self):
        self.nb_classes = len(glob.glob(mfcc.MFCC_EXTRACT().MFCC_NAME + '[0-9][0-9][0-9]'))
        self.X = tf.placeholder(tf.float32, [None, mfcc.MFCC_EXTRACT().FEATURE_NUMBER])
        X_MFCC = tf.reshape(self.X, [-1, 1, mfcc.MFCC_EXTRACT().FEATURE_NUMBER, 1])
        self.Y = tf.placeholder(tf.int32, [None, 1])
        Y_one_hot = tf.one_hot(self.Y, self.nb_classes)
        Y_one_hot = tf.reshape(Y_one_hot, [-1, self.nb_classes])
        
        self.keep_prob = tf.placeholder(tf.float32)
        
        print ('L1--------------------------------------------------------------')
        W1 = tf.Variable(tf.random_normal([1, 3, 1, 4], stddev=0.01))
        L1 = tf.nn.conv2d(X_MFCC, W1, strides=[1, 1, 2, 1], padding='SAME')
        print (L1)
        L1 = tf.nn.relu(L1)
        print (L1)
        L1 = tf.nn.max_pool(L1, ksize=[1, 1, 2, 1], strides=[1, 1, 2, 1], padding='SAME')
        print (L1)
        L1 = tf.nn.dropout(L1, keep_prob=self.keep_prob)
        print (L1)

        print ('L2--------------------------------------------------------------')
        W2 = tf.Variable(tf.random_normal([1, 3, 4, 32], stddev=0.01))
        L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
        print (L2)
        L2 = tf.nn.relu(L2)
        print (L2)
        L2 = tf.nn.max_pool(L2, ksize=[1, 1, 2, 1], strides=[1, 1, 2, 1], padding='SAME')
        print (L2)
        L2 = tf.nn.dropout(L2, keep_prob=self.keep_prob)
        print (L2)
        L2 = tf.reshape(L2, [-1, 4 * 32])
        print (L2)

        print ('L3--------------------------------------------------------------')
        W3 = tf.get_variable("W3", shape=[4 * 32, 4 * 16], initializer=tf.contrib.layers.xavier_initializer())
        b3 = tf.Variable(tf.random_normal([4 * 16]))
        L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)
        print (L3)
        L3 = tf.nn.dropout(L3, keep_prob=self.keep_prob)
        print (L3)
        
        W4 = tf.get_variable("W5", shape=[4 * 16, self.nb_classes], initializer=tf.contrib.layers.xavier_initializer())
        b4 = tf.Variable(tf.random_normal([self.nb_classes]))
        hypothesis = tf.matmul(L3, W4) + b4

        self.l_r = tf.placeholder(tf.float32)

        """
        print ('L1--------------------------------------------------------------')
        print (X_MFCC)
        Layer = tf.layers.conv1d(inputs=X_MFCC, filters=4, kernel_size=[2], strides=2, padding="same", activation=tf.nn.relu)
        print (Layer)
        Layer = tf.layers.max_pooling1d(inputs=Layer, pool_size=[2], strides= 2, padding="same")
        print (Layer)
        Layer = tf.layers.dropout(inputs=Layer, rate=self.keep_prob)

        print ("L2-------------------------------------------------------------------")
        Layer = tf.layers.conv1d(inputs=Layer, filters=32, kernel_size=[2], strides=1, padding="same", activation=tf.nn.relu)
        print (Layer)
        Layer = tf.layers.max_pooling1d(inputs=Layer, pool_size=[2], strides=2, padding="same")
        print (Layer)
        Layer = tf.layers.dropout(inputs=Layer, rate=self.keep_prob)
        Layer = tf.reshape(Layer, [-1, 4 * 32])

        print ("L3-------------------------------------------------------------------")
        print (Layer)
        Layer = tf.layers.dense(inputs=Layer, units=4 * 16, activation=tf.nn.relu)
        print (Layer)
        Layer = tf.layers.dropout(inputs=Layer, rate=self.keep_prob)
        print (Layer)

        self.l_r = tf.placeholder(tf.float32)

        W = tf.get_variable("W", shape=[4 * 16, self.nb_classes], initializer=tf.contrib.layers.xavier_initializer())
        b = tf.Variable(tf.random_normal([self.nb_classes]))
        hypothesis = tf.matmul(Layer, W) + b
        """
        # define cost/loss & optimizer
        self.cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
            logits=hypothesis, labels=Y_one_hot))
        self.optimizer = tf.train.AdamOptimizer(learning_rate=self.l_r).minimize(self.cost)

        # Test model and check accuracy


        self.prediction = tf.argmax(hypothesis, 1)
        correct_prediction = tf.equal(self.prediction, tf.argmax(Y_one_hot, 1))
        self.accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        #tf.summary.scalar("loss", cost)
        self.saver = tf.train.Saver()

    def save(self, sess):
        self.saver.save(sess, './model/cnn.ckpt')

    def load(self, sess):
        self.saver.restore(sess, './model/cnn.ckpt')

    def evaluate(self, sess, X_sample, y_sample, batch_size=512):
        '''Run a minibatch accuracy op'''

        N = X_sample.shape[0]
        correct_sample = 0

        for i in range(0, N, batch_size):
            X_batch = X_sample[i: i + batch_size]
            y_batch = y_sample[i: i + batch_size]
            N_batch = X_batch.shape[0]

            feed = {
                self.X: X_batch,
                self.Y: y_batch,
                self.keep_prob: 1
            }

            correct_sample += sess.run(self.accuracy, feed_dict=feed) * N_batch
        if N == 0 :
            return 0
        return correct_sample / N


    def train(self):

        learning_rate = 0.01
        training_epochs = 600
        batch_size = 5000
        RATE=44100
        m = mfcc.MFCC_EXTRACT()
        x_data, y_data, x_test_data, y_test_data = m.temp_load(0, 10)

        y_data = np.reshape(y_data, (-1, 1))
        y_test_data = np.reshape(y_test_data, (-1, 1))
        print (x_data.shape, y_data.shape, x_test_data.shape, y_test_data.shape)


        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())     #python 2.7
            #sess.run(tf.global_variables_initializer())     #python 3.n
            print('Learning stared. It takes sometime.')
            
            ts_time = time.time()
            for epoch in range(training_epochs):
                s_time = time.time()
                avg_cost = 0
                total_batch = int(len(x_data) / batch_size)

                for i in range(0, x_data.shape[0], batch_size):
                    batch_xs = x_data[i : i + batch_size]
                    batch_ys = y_data[i : i + batch_size]

                    feed_dict = {self.X: batch_xs, self.Y: batch_ys, self.keep_prob: 0.7, self.l_r: learning_rate}
                    c, _ = sess.run([self.cost, self.optimizer], feed_dict=feed_dict)
                    avg_cost += c * len(batch_xs)
                    
                    #if i == 0:
                    #    s = sess.run(summary, feed_dict=feed_dict)
                    #    writer.add_summary(s, global_step=global_step)
                    #    global_step += 1
                
                t = self.evaluate(sess, x_test_data, y_test_data)
                print('[Epoch]', '%04d' % (epoch + 1), '[cost]', '{:.5f}'.format(avg_cost/len(x_data)),
                      "[Train]", '{:.5f}'.format(t),
                      "[Test]", '{:.5f}'.format(self.evaluate(sess, x_test_data, y_test_data)),
                      "[Time]", '{:.5f}'.format(time.time()-s_time))
                    
                if t > 0.83:
                    learning_rate = 0.001
                else:
                    learning_rate = 0.01
            

            print('Learning Finished!')

            print("\nAccuracy Evaluates")
            print("-------------------------------")
            print('Train Accuracy:', self.evaluate(sess, x_data, y_data))
            print('Test Accuracy:', self.evaluate(sess, x_test_data, y_test_data))
                
            print ('time = ', time.time() - ts_time)

            self.save(sess)

    def valid(self):


        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())     #python 2.7
            #sess.run(tf.global_variables_initializer())     #python 3.n
            print("\nGet one and predict")
            print("-------------------------------")
            self.load(sess)

            _str = ''
            str_ = ''


            x_valid = mfcc.MFCC_EXTRACT().temp_valid_to_feature('./validation/' + str_ + 'ahn' + _str +'.wav',44100)
            percent = 0
            for i in range(self.nb_classes):
                y_valid = np.full((len(x_valid),),i, dtype=np.float32)
                y_valid = np.reshape(y_valid, (-1, 1))
                a = self.evaluate(sess, x_valid, y_valid) 
                print(format(i,'03'), ' Accuracy:', a)
                percent += a
            print (sess.run(self.prediction, feed_dict={self.X:x_valid, self.Y:y_valid, self.keep_prob:1.0}))
            print (percent)

            print("-------------------------------")

            x_valid = mfcc.MFCC_EXTRACT().temp_valid_to_feature('./validation/' + str_ + 'park' + _str + '.wav',44100)
            percent = 0
            for i in range(self.nb_classes):
                y_valid = np.full((len(x_valid),),i, dtype=np.float32)
                y_valid = np.reshape(y_valid, (-1, 1))
                a = self.evaluate(sess, x_valid, y_valid) 
                print(format(i,'03'), ' Accuracy:', a)
                percent += a
            print (sess.run(self.prediction, feed_dict={self.X:x_valid, self.Y:y_valid, self.keep_prob:1.0}))
            print (percent)

            print("-------------------------------")

            x_valid = mfcc.MFCC_EXTRACT().temp_valid_to_feature('./validation/' + str_ + 'kim' + _str + '.wav',44100)
            percent = 0
            for i in range(self.nb_classes):
                y_valid = np.full((len(x_valid),),i, dtype=np.float32)
                y_valid = np.reshape(y_valid, (-1, 1))
                a = self.evaluate(sess, x_valid, y_valid) 
                print(format(i,'03'), ' Accuracy:', a)
                percent += a
            print (sess.run(self.prediction, feed_dict={self.X:x_valid, self.Y:y_valid, self.keep_prob:1.0}))
            print (percent)

            print("-------------------------------")

            v = record.VOICE_RECORD(seconds=2)
            frames = v.record()
            v.temp_save('./valid.wav', frames)
            x_valid = mfcc.MFCC_EXTRACT().temp_frame_to_feature(frames,44100)
            percent = 0
            result = -1
            for i in range(self.nb_classes):
                y_valid = np.full((len(x_valid),),i, dtype=np.float32)
                y_valid = np.reshape(y_valid, (-1, 1))
                a = self.evaluate(sess, x_valid, y_valid) 
                print(format(i,'03'), ' Accuracy:', a)
                if a >= 0.6:
                    result = i
                percent += a
            print (sess.run(self.prediction, feed_dict={self.X:x_valid, self.Y:y_valid, self.keep_prob:1.0}))
            print (percent)

            return result
    
    def predict(self):
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())     #python 2.7
            #sess.run(tf.global_variables_initializer())     #python 3.n
            print("\nGet one and predict")
            print("-------------------------------")
            self.load(sess)

            v = record.VOICE_RECORD(seconds=1)
            frames = v.record()
            v.temp_save('./valid.wav', frames)
            x_valid = mfcc.MFCC_EXTRACT().temp_frame_to_feature(frames,44100)
            percent = 0
            result = -1
            for i in range(self.nb_classes):
                y_valid = np.full((len(x_valid),),i, dtype=np.float32)
                y_valid = np.reshape(y_valid, (-1, 1))
                a = self.evaluate(sess, x_valid, y_valid) 
                print(format(i,'03'), ' Accuracy:', a)
                if a >= 0.6:
                    result = i
                percent += a
            print (sess.run(self.prediction, feed_dict={self.X:x_valid, self.Y:y_valid, self.keep_prob:1.0}))
            print (percent)

            return result

if __name__ == '__main__':
    cnn = CNN()
    cnn.train()
    cnn.valid()