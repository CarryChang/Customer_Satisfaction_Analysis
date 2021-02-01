[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
#### Customer_satisfaction_Analysis 

[![Stargazers over time](https://starchart.cc/CarryChang/Customer_Satisfaction_Analysis.svg)](https://starchart.cc/CarryChang/Customer_Satisfaction_Analysis)

##### 结果整合
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/情感分析图.png"></div>

##### Demo 演示
  - [视频演示demo](https://github.com/CarryChang/C-CNN-for-Chinese-Sentiment-Analysis/blob/master/video/demo.mp4)
  - [详细步骤](https://www.lanqiao.cn/courses/2628)

##### 基于用户 UGC 的在线民宿满意度挖掘，负责数据采集、主题抽取、情感分析等任务。开发的目的是克服用户打分和评论不一致，实现了在线评论采集和用户满意度分析。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/不一致.png"></div>

#####  主要功能包括在线原始评论采集、主题聚类、评论情感分析与结果可视化展示等四个模块，如下所示。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/流程.png"></div>


>1.   提取后的民宿地址和在线评论等信息如下。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/数据库.png"></div>

>2.   搭建了百度地图 POI 查询入口，可以进行自动化的批量查询地理信息。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/地址.png"></div>

> 3.   通过高频词可视化展示，归纳出评论主题。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/gaopin1.png"></div>
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/高频2.png"></div>

> 4.   构建了基于在线民宿语料的 LDA 自动化主题聚类模型，利用主题中心词能找出对应的主题属性字典，并使用用户打分作为标注，然后通过多种分类模型，选用最优模型对提出的评价主体 进行情感分析，针对主题属性表进行主题提取后的文本进行情感分析，分别得出当前主题对应的情感趋势，横坐标为所有关于主题为“环境”的情感得分，纵坐标为对应的情感的条数，可以起到纵观当前“环境”主题下的情感趋势，趋势往右代表当前主题评价较好，总共有{“交通”，“价格”，“体验”，“服务”，“特色”，“环境”，“设施”，“餐饮”}的主题，选取“环境”主题进行可视化之后的结果如下图所示。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/lda_topic_select.png"></div>
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/lda_topic_select1.png"></div>
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/主题.png"></div>

> 5.   通过POI热力图的方式对在线民宿满意度进行展示。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/poi可视化.png"></div>
<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/poi打分.png"></div>

> 6.   代码结构如下。

<div align=center><img  src="https://github.com/CarryChang/Customer_Satisfaction_Analysis/blob/master/pic/结构1.png"></div>

#####  新版本特性
> 1. 使用 litNLP 深度情感推理
> 2. 增加多进程提高多个 topic 下的文本匹配速度
> 3. Project_Main.py 直接完成细粒度情感极性可视化操作
