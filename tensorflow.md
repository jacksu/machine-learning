## awesome
[awesome-tensorflow](https://github.com/jtoy/awesome-tensorflow)--A curated list of dedicated resources http://tensorflow.org

## tutorial
[tensorflow学习用例](https://github.com/burness/tensorflow-101)

[TensorFlow Tutorial and Examples for beginners](https://github.com/aymericdamien/TensorFlow-Examples)

[TensorBox](https://github.com/TensorBox/TensorBox)-----Object detection in TensorFlow

[Tensorflow入门：数据结构和编程思想](http://blog.csdn.net/lingerlanlan/article/details/61616906)

[TensorFlow学习笔记1：入门](http://www.jeyzhang.com/tensorflow-learning-notes.html)

[tensorflow-talk-debugging](https://github.com/wookayin/tensorflow-talk-debugging)------ Slides and supplementary codes for my talk 'Debugging Tips on TensorFlow' (2016)

[learning to learn](https://github.com/deepmind/learning-to-learn)------Learning to Learn in TensorFlow

[Example code to help get started using TensorFlow](https://github.com/Hack-a-Day/bincounter_TensorFlow_example/)

[详解TensorBoard如何调参](http://geek.csdn.net/news/detail/197155)


[Implementations of CNNs, RNNs, GANs, etc](https://github.com/adeshpande3/Tensorflow-Programs-and-Tutorials)

## 架构
[TensorFlow框架剖析与应⽤](http://ocgxshkaw.bkt.clouddn.com/11%20%E3%80%8ATensorFlow%E6%A1%86%E6%9E%B6%E5%89%96%E6%9E%90%E5%8F%8A%E5%BA%94%E7%94%A8%E3%80%8B%E7%8E%8B%E7%90%9B.pdf)

[十图详解TensorFlow数据读取机制（附代码）](http://geek.csdn.net/news/detail/201552)


```python
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3=tf.add(node1,node2)
#print(sess.run(node3))
tf.summary.scalar("test",node3)
summary_op = tf.summary.merge_all() 
sess.run(node3)
summary_log_dir=vi.get_summary_log_dir()
file_writer = tf.summary.FileWriter(summary_log_dir, sess.graph)
port = vi.open_tensorboard(summary_log_dir)
```
