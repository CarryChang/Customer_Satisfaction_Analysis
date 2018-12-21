#### Customer_satisfaction_Analysis
##### 本软件开发的目的是实时对重庆地区在线民宿的满意度进行评测，使用Python实现了在线评论采集和情感可视化分析，克服用户打分和评论不一致的问题，不一致现象如下。
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/不一致.png"></div>

##### 主要功能包括在线原始评论采集、主题分类、评论情感分析与结果可视化展示等四个模块，项目流程如下所示。
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/民宿挖掘步骤.jpg"></div>

>1.   使用Selenium模拟浏览器点击翻页操作，并配合Request实现了携程网爬虫封锁和自动化的采集民宿UGC内容的功能，提取后的民宿地址和在线评论等信息如下。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/数据库.png"></div>

>2.   搭建了百度地图POI查询入口，可以进行自动化的批量查询POI信息的功能，信息直接存入excel中

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/地址.png"></div>

> 3.   通过高频词可视化展示，归纳出评论主题
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/高频2.png"></div>
> 4.   构建了基于在线民宿语料的Word2vec主题聚类模型，利用主题中心词能找出对应的主题属性字典，并使用用户打分作为标注，然后通过实验贝叶斯、SVM、决策树等多种分类模型，选用最优模型对提出的评价主体 进行情感分类
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/主题.png"></div>
> 6.   通过POI热力图的方式对在线民宿满意度进行展示。
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/poi可视化.png"></div>
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/poi打分.png"></div>
> 7.   代码结构如下
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/总的结构.png"></div>
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/结构1.png"></div>
