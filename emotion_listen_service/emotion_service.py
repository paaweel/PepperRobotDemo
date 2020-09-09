import keras
from keras.models import model_from_json
import os
import librosa
import numpy as np
import pandas as pd
import wave
import io
import soundfile as sf
import tensorflow as tf
import scipy.io.wavfile

from audio_file import AudioFile


class EmotionService:
    def __init__(self):
        self.relative_path = os.getcwd()
        self.audio_file_service = AudioFile()
        with open(os.path.join(self.relative_path, 'models/model.json'), 'r') as json_file:
            self.model = model_from_json(json_file.read())
            self.model.load_weights(os.path.join(self.relative_path, 'models/audio_emotion_model.h5'))
            opt = keras.optimizers.rmsprop(lr=0.00001, decay=1e-6)
            self.model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
            self.feature_decoding = {0: "angry",
                                 1: "calm",
                                 2: "fearful",
                                 3: "happy",
                                 4: "sad",
                                 5: "angry",
                                 6: "calm",
                                 7: "fearful",
                                 8: "happy",
                                 9: "sad"}
        self.audio_buf = None
        self.emotion_buf = None

    def add_audio_data(self, data):
        self.audio_buf.append(data)

    def get_last_emotions(self):
        if self.emotion_buf:
            return self.emotion_buf[-1]
        return "NaN"

    def __extract_features(self, audio_name):
        audio_path = os.path.join(self.audio_dir, audio_name)
        df = pd.DataFrame(columns=['feature'])
        X, sample_rate = librosa.load(audio_path, duration=2.5, sr=22050 * 2, offset=0.5)
        sample_rate = np.array(sample_rate)
        feature = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),
                          axis=0)
        feature = np.expand_dims(np.array(feature), axis=2)
        if feature.shape[0] < 216:
            tmp_feature = np.zeros((216, 1))
            tmp_feature[:feature.shape[0]] = feature
            feature = tmp_feature
        return np.expand_dims(feature, axis=0)

    def predict(self):
        audio_name = 'output.wav'
        features = self.__extract_features(audio_name)
        preds = self.model.predict(features, batch_size=32, verbose=1)
        pred = preds.argmax(axis=1)[0]
        return self.feature_decoding[pred]

    def predict_from_txt(self):
        self.audio_file_service.txt_to_wav()
        features = self.__extract_features(self.audio_file_service.output_audio)
        preds = self.model.predict(features, batch_size=32, verbose=1)
        pred = preds.argmax(axis=1)[0]
        return self.feature_decoding[pred]

    def test_all(self):
        self.audio_file_service.wav_to_txt()
        self.audio_file_service.txt_to_wav()
        features = self.__extract_features(self.audio_file_service.output_audio)
        preds = self.model.predict(features, batch_size=32, verbose=1)
        pred = preds.argmax(axis=1)[0]
        return self.feature_decoding[pred]

