import os
import wave
import numpy as np


class AudioFile:
    def __init__(self):
        self.audio_dir = 'tmp'
        if not os.path.exists(self.audio_dir):
            os.makedirs(self.audio_dir)
        self.input_audio = "input.wav"
        self.input_txt = "input.txt"
        self.output_audio = "output.wav"
        self.output_txt = "output.txt"

    def txt_to_wav(self):
        in_file = open(self.input_txt, "rb")  # opening for [r]eading as [b]inary
        data = in_file.read()  # if you only wanted to read 512 bytes, do .read(512)
        in_file.close()
        audio_path = os.path.join(self.audio_dir, self.output_audio)
        if os.path.exists(audio_path):
            os.remove(audio_path)
        with open(audio_path, mode='bx') as f:
            f.write(data)

    def txt_bytes_to_wav(self):
        in_file = open(self.output_txt, 'rb')
        response_list = in_file.read()
        in_file.close()
        data = np.frombuffer(response_list, dtype='int16')
        print(data)
        # 1 - mruczenie, 2 - powoli, 3 - internal data stream error, 4 - szybki smerf
        channels = 2
        sampleswidth = 2 # 1: szum + dźwięk, 2  ok, 3- sam szum, 4 - za szybko żeby zrozumieć
        out_file = wave.open(self.output_audio, 'wb')
        out_file.setnchannels(channels)
        out_file.setframerate(16000)
        out_file.setsampwidth(sampleswidth)
        out_file.writeframes(data)
        out_file.close()

    def wav_to_txt_bytes(self, verbose=False):
        audio_path = os.path.join(self.audio_dir, self.input_audio)
        with open(audio_path, mode='rb') as f:
            wave_data = f.read(1000000)
        wave_data = wave_data[24:]
        # print(wave_data[1:20])
        with open(self.output_txt, mode='wb') as f:
            f.write(wave_data)
        if verbose:
            with open(self.output_txt, mode='rb') as f:
                print(f.read())

    def response_to_wav(self, data=None):
        if not data:
            in_file = open("response.txt", 'r')
            data = in_file.read()
            in_file.close()
        else:
            data = data.sub('\x06', '', data)
            data = data.sub('\x04', '', data)

        data = np.fromstring(data, dtype='int16')
        # 1 - mruczenie, 2 - powoli, 3 - internal data stream error, 4 - szybki smerf
        channels = 2
        sampleswidth = 2  # 1: szum + dźwięk, 2  ok, 3- sam szum, 4 - za szybko żeby zrozumieć
        out_file = wave.open(self.output_audio, 'wb')
        out_file.setnchannels(channels)
        out_file.setframerate(16000)
        out_file.setsampwidth(sampleswidth)
        out_file.writeframes(data)
        out_file.close()
