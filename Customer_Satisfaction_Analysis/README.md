[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
#### Sentiment_Analysis
1. 训练的语料来自于snownlp的训练语料和用户打分的极值进行筛选出来的评论相结合筛选出来的
2. Project_Mail执行所有的操作

>1. sa_model_train.py是字符级卷积网络（TextCNN）的训练阶段
>2. sa_model_predict.py是字符级卷积网络（TextCNN)的推理阶段

##### bug record
>1. model 模式下无法使用predict_class：需要先predict后再使用np.argmax(result, axis=1)统一标签转换
>2. 

##### 待优化
1. 主题识别加入分类模型，增加泛化
2.  
