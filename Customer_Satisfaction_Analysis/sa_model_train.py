# -*- coding: utf-8 -*-
# @Time: 2020/6/20 0020 0:46
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from model_structure.TextCNN import sa_model
from model_structure.conf import *
from sklearn import metrics
import pandas as pd
import numpy as np
import pickle
import shutil
import os
class SA:
    def __init__(self):
        self.init_model = sa_model()
        self.model = self.init_model.create_model()
    def train_tk(self):
        tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', num_words=max_words)
        tokenizer.fit_on_texts(train_data['text_cut'])
        # # rebuild
        # shutil.rmtree(model_path)
        # os.mkdir(model_path)
        # tokenizer save
        with open(tokenize_path, 'wb') as tokenize:
            pickle.dump(tokenizer, tokenize)
        return tokenizer
    def train(self,x_train,x_test):
        self.model.fit(x_train, x_test, batch_size=256, epochs=10, validation_split=0.2,
                            callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])

        self.model.save(sa_model_path)
        try:
            pre_result = self.model.predict_classes(y_train, batch_size=256, verbose=0)
        except:
            result_ = self.model.predict_classes(y_train, batch_size=256, verbose=0)
            pre_result = np.argmax(result_, axis=1)
        return self.model, pre_result
    def evaluate(self,result,y_test):
        report = metrics.classification_report(y_test, result)
        # acc auc
        acc = metrics.accuracy_score(y_test, result)
        auc = metrics.roc_auc_score(y_test, result)
        print('acc:{}-auc:{}'.format(acc, auc))
        print(report)
if __name__ == '__main__':
    # C-CNN-SA(字符级卷积网络)
    train_data = pd.read_csv('data/sa_data_train.csv')
    # list sentence
    train_data['text_cut'] = train_data['text'].apply(lambda x :" ".join(list(x)))
    model = SA()
    tokenizer = model.train_tk()
    # 2-8的分割数据,固定测试数据
    x_train, y_train, x_test, y_test = train_test_split(train_data['text_cut'], train_data['label'], test_size=0.2, random_state=1)
    # pad_sequences
    x_train, x_test = pad_sequences(tokenizer.texts_to_sequences(x_train), maxlen), np.array(x_test)
    y_train, y_test = pad_sequences(tokenizer.texts_to_sequences(y_train), maxlen), np.array(y_test)
    # train
    _, pre_result = model.train(x_train, x_test)
    # evaluate
    model.evaluate(pre_result, y_test)






