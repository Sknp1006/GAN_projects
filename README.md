# GAN_projects
一些有关GAN的有趣项目  

-------------------
## anime-creater with tf-gan  
### 项目描述：  
  * 试用tf-gan工具制作动漫头像生成对抗网络
  * tf-gan链接：https://github.com/tensorflow/gan
  
### README.md（中文版）  

### TF-GAN是用于训练和评估生成对抗网络（GAN）的轻量级库
  * 安装：pip install tensorflow_gan  
  * [训练好的例子](https://github.com/tensorflow/gan/tree/master/tensorflow_gan/examples/)  
  * [交互式TF-GAN(Google Cola)](https://github.com/tensorflow/gan/blob/master/tensorflow_gan/examples/colab_notebooks/tfgan_tutorial.ipynb)  
### TF-GAN库的结构  
#### TF-GAN由几个部分组成，这些部分设计为独立存在：
  * [Core](https://github.com/tensorflow/gan/tree/master/tensorflow_gan/python/train.py): 训练GAN所需的主要基础架构。使用TF-GAN库调用，自定义代码，本机TF代码和其他框架的任意组合设置培训。  
  * [Features](https://github.com/tensorflow/gan/tree/master/tensorflow_gan/python/features/): 常用的GAN操作和规范化技术，例如实例规范化和条件化。  
  * [Losses](https://github.com/tensorflow/gan/tree/master/tensorflow_gan/python/losses/): 损失和惩罚，例如Wasserstein loss, gradient penalty, mutual information penalty等。  
  * [Evaluation](https://github.com/tensorflow/gan/tree/master/tensorflow_gan/python/eval/): 标准GAN评估指标。将 Inception Score, Frechet Distance, or Kernel Distance与预训练的Inception网络一起使用，以评估您的无条件生成模型。您还可以使用自己的预训练分类器来获得更具体的性能数字，或者使用其他方法来评估条件生成模型。
  * [Examples](https://github.com/tensorflow/gan/tree/master/tensorflow_gan/): 有关如何使用TF-GAN的简单示例，以及更复杂的最新示例。
#### 以下是一些使用TF-GAN的已发表论文：
  * [Self-Attention Generative Adversarial Networks](https://arxiv.org/abs/1805.08318)
  * [Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096)
  * [GANSynth: Adversarial Neural Audio Synthesis](https://arxiv.org/abs/1902.08710)
  * [Boundless: Generative Adversarial Networks for Image Extension](http://arxiv.org/abs/1908.07007)
  * [NetGAN: Generating Graphs via Random Walks](https://arxiv.org/abs/1803.00816)
  * [Discriminator rejection sampling](https://arxiv.org/abs/1810.06758)
  * [Generative Models for Effective ML on Private, Decentralized Datasets](https://arxiv.org/pdf/1911.06679.pdf)
#### 训练GAN：
  * 指定网络的输入
  * 使用 **GANModel** 创建生成器和判别器
  * 用 **GANLoss** 指定你的loss函数
  * 用 **GANTrainOps** 创建你的训练步骤
  * 开始训练吧<(￣︶￣)↗\[GO!]
  
