## FaceProcess
### 项目描述：
  * 数据预处理模块  
  * 在DeepFaceLab3.15集成环境的基础上进行扩展，可对真人像进行人脸检测和裁切
  * [S3FD算法论文笔记](https://blog.csdn.net/weixin_40671425/article/details/90206650)（非本人）
  * tf-gan链接：https://github.com/tensorflow/gan
  * 训练用的头像(273.46MB, 96x96, 51223张) 【[百度云](https://pan.baidu.com/s/1lcmXRihOPh8F55l294T45w)：zs1g】
  * 依赖**DeepFaceLab3.15**，集成环境 **_internal** 太大，故请移步【[百度云](https://pan.baidu.com/s/1fdj5kAPsvgSqQR9GL1GOBQ)：rjzo】
### 文件描述： 
  1) clear workspace.bat  
    * 清理 **workplace**
  2) pre_load_files.bat  
    * 将目标文件夹下的所有jpg文件导入 **workplace\data_src**
  3) data_src extract full_face S3FD.bat  
    * 识别 **data_src** 中的人脸，并导入aligned  
  4) data_src sort.bat  
    * 头像按从好到坏的顺序排序
  5) pre_process.py  
    * 文件复制模块  
    
---

# **\-\-**施工中**\-\-     d=====(￣▽￣*)b**

---  