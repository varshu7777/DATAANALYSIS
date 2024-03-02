# -*- coding: utf-8 -*-
"""CNN1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qCWfiAlEjIw2D1BS-t-f-TMsrzjNWmp2
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#Define image size and batch size
IMG_SIZE=224
BATCH_SIZE=32

#define data generators for train,validation and testing
train_datagen=ImageDataGenerator(
          rescale=1./255,
          validation_split=0.2
)
train_generator=train_datagen.flow_from_directory(
                    '/content/drive/MyDrive/DATASET/Brain_Tumor_Detection/train',
                      target_size=(IMG_SIZE,IMG_SIZE),
                      batch_size=BATCH_SIZE,
                      class_mode='binary',
                      subset='training'
)
val_generator=train_datagen.flow_from_directory(
                    '/content/drive/MyDrive/DATASET/Brain_Tumor_Detection/train',
                      target_size=(IMG_SIZE,IMG_SIZE),
                      batch_size=BATCH_SIZE,
                      class_mode='binary',
                      subset='validation'
)
test_datagen=ImageDataGenerator(rescale=1./255)
test_generator=test_datagen.flow_from_directory(
                      '/content/drive/MyDrive/DATASET/Brain_Tumor_Detection/train',
                      target_size=(IMG_SIZE,IMG_SIZE),
                      batch_size=BATCH_SIZE,
                      class_mode='binary'
)

#define a model
model=keras.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(IMG_SIZE,IMG_SIZE,3)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(128,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(32,activation='relu'),
    layers.Dense(1,activation='sigmoid')
])

#compiling of model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

history=model.fit(train_generator,validation_data=val_generator,epochs=5)

model.save("model.h5","label.txt")

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
#load saved model
model=load_model('/content/model.h5')
#load and preprocess the test image
test_image_path='/content/drive/MyDrive/DATASET/Brain_Tumor_Detection/train/no/No19.jpg'
img=image.load_img(test_image_path,target_size=(224,224))
img_array=image.img_to_array(img)
img_array=np.expand_dims(img_array,axis=0) #add batch dimension
img_array /=255. # Normalize the pixel values
#make prediction
prediction=model.predict(img_array)
#print the prediction
if prediction<0.5:
  print("Prediciton: not a bridal dress (Probability:",prediction[0][0],")")
else:
  print("Prediciton: bridal dress(Probability:",prediction[0][0],")")
