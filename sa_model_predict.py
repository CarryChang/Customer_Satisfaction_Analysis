# -*- coding: utf-8 -*-
from litNlp.predict import SA_Model_Predict

def model_predict():
    model = SA_Model_Predict(tokenize_path, sa_model_path_m, max_len=100)
    sa_score = model.predict(predict_text)
    # 情感极性输出
    print([i[1] for i in sa_score])

if __name__ == '__main__':
    # load conf
    from setting import *
    # example
    predict_text = ['这个我不喜欢', '这个我喜欢不']
    model_predict()
