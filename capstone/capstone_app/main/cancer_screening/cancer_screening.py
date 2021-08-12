from django.db.models.fields import BooleanField
import numpy as np
import pandas as pd
from PIL import Image
from django.conf import settings
import os
import pickle

from pathlib import Path

def analyze_photo(photo):
    
    base_dir = settings.BASE_DIR
    photo_dir = settings.MEDIA_ROOT + photo.image.url.replace('/media/',"")    
    image_list = []

    image_list.append(np.asarray(Image.open(photo_dir).resize((90,90)).convert("RGB")))

    resized_rbg_photo_scaled = np.array(image_list, dtype = 'uint8') / 255

    ML_model_location = str(base_dir) + '/main/cancer_screening/saved_model.sav'

    model = pickle.load(open(ML_model_location,'rb'))

    prediction = model.predict(resized_rbg_photo_scaled.reshape(resized_rbg_photo_scaled.shape[0],-1))

    if prediction == 1:
        outcome = True
    else:
        outcome = False

    return outcome


def analyze_photo1(photo):
    base_dir = settings.BASE_DIR
    photo_dir = os.path.join(base_dir,photo.image.url)


    return True