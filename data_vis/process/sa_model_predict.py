# -*- coding: utf-8 -*-
# @Time: 2020/6/20 0020 0:55
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from process.conf import *
import pickle
# vec loading
class SA:
    def __init__(self):
        with open(tokenize_path, 'rb') as tokenize_save:
            self.tokenizer_load = pickle.load(tokenize_save)
        self.model_load = load_model(sa_model_path)
        self.maxlen = maxlen
    def predict(self,predict_text):
        tk_list = [list(text) for text in predict_text]
        test_text = pad_sequences(self.tokenizer_load.texts_to_sequences(tk_list), self.maxlen)
        test_proba_list = self.model_load.predict_proba(test_text)
        return test_proba_list
if __name__ == '__main__':
    # 解决同词不同意的问题,增加批处理
    predict_text = ['这个我不喜欢', '这个我喜欢不']
    model = SA()
    sa_score = model.predict(predict_text)
    print(sa_score)
    # [[0.19279656]  [0.74052083]]