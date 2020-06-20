# -*- coding: utf-8 -*-
# @Time: 2020/6/20 0020 0:46
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau
from tensorflow.keras.layers import Dense, Embedding, Flatten,Dropout,Convolution1D,BatchNormalization
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam,RMSprop
from tensorflow.keras.models import Sequential, Model
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import concatenate,GlobalAveragePooling1D,Activation,MaxPool1D,Input
from model_structure.conf import *
class sa_model:
    def create_model(self):
        # 使用model模式
        main_input = Input(shape=(maxlen,), dtype='float64')
        embedder = Embedding(max_words + 1, 300, input_length=maxlen)
        embed = embedder(main_input)
        # 3,4,5 windows
        cnn1 = Convolution1D(256, 3, padding='same', strides=1, activation='relu')(embed)
        cnn1 = MaxPool1D(pool_size=4)(cnn1)
        cnn2 = Convolution1D(256, 4, padding='same', strides=1, activation='relu')(embed)
        cnn2 = MaxPool1D(pool_size=4)(cnn2)
        cnn3 = Convolution1D(256, 5, padding='same', strides=1, activation='relu')(embed)
        cnn3 = MaxPool1D(pool_size=4)(cnn3)
        # concat
        cnn = concatenate([cnn1, cnn2, cnn3], axis=-1)
        flat = Flatten()(cnn)
        drop = Dropout(0.5)(flat)
        main_output = Dense(1, activation='sigmoid')(drop)
        model = Model(inputs=main_input, outputs=main_output)
        model.compile(loss='binary_crossentropy', optimizer=Adam(lr=1e-3), metrics=['accuracy'])
        return model
if __name__ == '__main__':
    model = sa_model()
    sa = model.create_model()
    sa.summary()