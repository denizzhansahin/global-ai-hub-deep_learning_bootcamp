# -*- coding: utf-8 -*-
"""deep_learning_for_loop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pIDv0N9BGplzT42GQ2EybyWAQqcp7ESu
"""

#kütüphanelerin eklenmesi
import tensorflow as tf
import librosa
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import librosa.display

#ses verisini oynatmak için
import IPython.display as ipd

#görüntü işleme için
import cv2
from google.colab.patches import cv2_imshow

#verileri bölmek için
from sklearn.model_selection import train_test_split

#listeler
goruntu = []
etiket = []

liste_ekleme = []
liste_ikili = []

#veri seti indirme
!wget https://zenodo.org/record/1203745/files/UrbanSound8K.tar.gz
!tar -xvf /content/UrbanSound8K.tar.gz

#veri işleme
veri = pd.read_csv('/content/UrbanSound8K/metadata/UrbanSound8K.csv')
className = veri.iloc[0:8000,7:]

veri1 = pd.read_csv('/content/UrbanSound8K/metadata/UrbanSound8K.csv')
slice_name = veri1.iloc[0:8000,0:1]

veri2 = pd.read_csv('/content/UrbanSound8K/metadata/UrbanSound8K.csv')
fold_name = veri2.iloc[0:8000,5:6]

veri3 = pd.read_csv('/content/UrbanSound8K/metadata/UrbanSound8K.csv')
classID_name = veri3.iloc[0:8000,6:7]

#her fold içindeki tüm classID'ler ile işlem yapar
i = 0
file_name = ''
fold = ''
dosya_yolu =''
audio_data = ''

liste_ikili = []
while i < 100:
  a = '/content/UrbanSound8K/audio/fold'
  if(fold_name.values[i]!=-1):
    dosya_isim = slice_name.values[i]
    print(dosya_isim)
    dosya_isim1 = dosya_isim[0]
    print(dosya_isim1)

    fold_isim = fold_name.values[i]
    print(fold_isim)
    fold = str(fold_isim[0])
    print(fold)


    audio_data = '/content/UrbanSound8K/audio/fold'+fold+'/'+dosya_isim1
    print(audio_data)
    x , sr = librosa.load(audio_data)
    print(type(x), type(sr))
    print(x.shape, sr)
    librosa.load(audio_data, sr=44100)
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)

    n = i
    n =str(n)
    file_name = '/content/gorsel/gorsel'+n+'.png'
    plt.savefig(file_name)
    

    #listeye eleman ekleme
    etiket_eleman = classID_name.values[i]
    etiket.append(etiket_eleman[0])


    #gorntu isleme
    image = cv2.imread (file_name)
    gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
    w = int(gray.shape[1]/2)
    h = int(gray.shape[0]/2)
    resize = cv2.resize(gray, (w, h), interpolation= cv2.INTER_LINEAR)
    yeni_image = cv2.normalize(resize,None,0,1,cv2.NORM_MINMAX)

    opencv_isim = '/content/opencv_gorsel/gorsel'+n+'.png'
    cv2.imwrite(opencv_isim, yeni_image)
    cv2_imshow(yeni_image)

    ekle_goruntu = cv2.imread(opencv_isim)
    goruntu.append(ekle_goruntu)

    liste_ekleme.append(ekle_goruntu)
    liste_ekleme.append(etiket_eleman[0])
    liste_ikili.append(liste_ekleme)
    liste_ekleme = []



    n = int(n)
    plt.show()
  i+=1

print(liste_ikili)

#verileri parçalamak
liste_numpy = np.array(liste_ikili)
X = liste_numpy[:,0]
Y = liste_numpy[:,1]
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.3, random_state=0)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

x_train_uzunluk_yarisi = int(len(x_train)/2)
y_train_uzunluk_yarisi = int(len(y_train)/2)
print("x_train uzunluk  :  ",x_train_uzunluk_yarisi,"\n")
print("y_train uzunluk  :  ",y_train_uzunluk_yarisi,"\n")
x_train = x_train.reshape(x_train_uzunluk_yarisi,2)
y_train = y_train.reshape(y_train_uzunluk_yarisi,2)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

#model eğitimi
model = tf.keras.Sequential()

#giriş katman
input_layer = tf.keras.layers.Dense(4096, input_dim=7,activation='relu')
model.add(input_layer)

#gizli katman
model.add(tf.keras.layers.Dense(4096, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))

#çıkış katmanı
model.add(tf.keras.layers.Dense(7,activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.add(tf.keras.layers.Flatten())

results = model.fit(x_train, y_train, epochs=10)

"""Deneme Amaçlı"""

#dosyaları ziple
!zip -r opencv.zip '/content/opencv_gorsel'

#liste uzunluğu
print(type(liste_ikili))
print(len(liste_ikili))

y_train = np.int32(y_train)
type(x_train.shape)
x_train.shape

print(type(X))
print(type(Y))
print(type(x_train))
print(type(y_train))
print(type(x_test))
print(type(y_test))

print(len(X))
print(len(Y))
print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))

brbrt = []
sdfvd = []

for ddd in range(10):
  a343 = ddd+2
  brbrt.append(ddd)
  brbrt.append(a343)
  sdfvd.append(brbrt)
  brbrt = []

print(sdfvd)

print(len(sdfvd))

array = np.array(sdfvd) 
print(array)
print(len(array))
print(type(array))
X = array[:,0]
y = array[:,1]
print(X)
print(len(X))
print(type(X))
print(Y)
print(len(Y))
print(type(Y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_train.shape, X_test.shape