# -*- coding: utf-8 -*-
import pandas as pd
from litNlp.train import SA_Model_Train
# load conf
from setting import *

def model_train():
    # data load
    train_data = pd.read_csv('data/label_comment.csv')
    # data process
    train_data['text_cut'] = train_data['text'].apply(lambda x: " ".join(list(x)))
    # train: evaluate 默认在训练完毕之后开启计算
    label = train_data['label']
    train_data = train_data['text_cut']
    # model load
    model = SA_Model_Train(max_words, embedding_dim, maxlen, tokenize_path, sa_model_path_m, train_method)
    # 模型训练
    model.train(train_data, label, num_classes=2, batch_size=256, epochs=2, verbose=1, evaluate=True)
    print('深度情感分析模型训练完毕')

# if __name__ == '__main__':
#     # run model trian
#     model_train()