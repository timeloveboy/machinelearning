# -*- coding: UTF-8 -*-

# 引入 Tensorflow 库
import tensorflow as tf

# 创建一个常量 Operation （操作）
hw = tf.constant("Hello Wolrd!")

# 启动一个Tensorflow 的 Session（会话）
sess = tf.Session()

# 运行 Graph （计算图）
print sess.run(hw)

# 关闭 Session（会话）
sess.close()
