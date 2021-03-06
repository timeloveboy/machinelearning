# sigmoid函数

在介绍逻辑回归模型之前，我们先引入sigmoid函数，其数学形式是：

g(x)=1/(1+e^(-x))

从上图可以看到sigmoid函数是一个s形的曲线，它的取值在[0, 1]之间，在远离0的地方函数的值会很快接近0/1。这个性质使我们能够以概率的方式来解释（后边延伸部分会简单讨论为什么用该函数做概率建模是合理的)。

决策函数

![](/img/sigmoid.jpg)
一个机器学习的模型，实际上是把决策函数限定在某一组条件下，这组限定条件就决定了模型的假设空间。当然，我们还希望这组限定条件简单而合理。而逻辑回归模型所做的假设是：