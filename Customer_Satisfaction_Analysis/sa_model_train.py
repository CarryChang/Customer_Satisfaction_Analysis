# -*- coding: utf-8 -*-
# @Time: 2020/6/20 0020 0:46
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau
from tensorflow.keras.layers import Dense, Embedding, Flatten,Dropout,Convolution1D,Activation
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam,RMSprop
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn import metrics
import pandas as pd
from conf import *
import numpy as np
import pickle
class SA:
    def train_tk(self):
        tokenizer = Tokenizer(num_words=max_words)
        tokenizer.fit_on_texts(train_data['text_cut'])
        # tokenizer save
        with open(tokenize_path, 'wb') as tokenize:
            pickle.dump(tokenizer, tokenize)
        return tokenizer
    def create_model(self):
        model = Sequential()
        #  embedding layer
        model.add(Embedding(max_words,embedding_dim,input_length=maxlen))
        # CNN的代码
        model.add(Convolution1D(64, 3, input_shape=(-1, embedding_dim)))
        model.add(Activation('relu'))
        model.add(Flatten())
        model.add(Dense(1024, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1,  activation='sigmoid'))
        model.compile(loss='binary_crossentropy',optimizer=Adam(lr=1e-3),metrics=['accuracy'])
        return model
    def train(self,x_train,x_test):
        ## 模型训练
        x_test = np.array(x_test)
        model = self.create_model()
        model.fit(x_train, x_test, batch_size=256, epochs=10, validation_split=0.2,
                            callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])
        return model
    def evaluate(self,result,y_test):
        y_test = np.array(y_test)
        report = metrics.classification_report(y_test, result)
        # acc auc
        acc = metrics.accuracy_score(y_test, result)
        auc = metrics.roc_auc_score(y_test, result)
        return acc, auc, report
if __name__ == '__main__':
    # C-CNN-SA(字符集卷积网络情感分析)
    train_data = pd.read_csv('data/sa_data_train.csv')
    # 不使用分词
    train_data['text_cut'] = train_data['text'].apply(lambda x :" ".join(list(x)))
    model = SA()
    tokenizer = model.train_tk()
    # 2-8的分割数据,固定测试数据
    x_train, y_train, x_test, y_test = train_test_split(train_data['text_cut'], train_data['label'], test_size=0.2,random_state=1)
    # pad_sequences
    x_train = pad_sequences(tokenizer.texts_to_sequences(x_train), maxlen)
    y_train = pad_sequences(tokenizer.texts_to_sequences(y_train), maxlen)
    # train
    sa_model = model.train(x_train, x_test)
    # evaluate
    result = sa_model.predict_classes(y_train, batch_size=256, verbose=0)
    acc, auc, report = model.evaluate(result, y_test)
    print('acc:{}-auc:{}'.format(acc,auc))
    print(report)
    # model save
    sa_model.save(sa_model_path)
    # acc:0.9241685779816514-auc:0.9232760870449649









