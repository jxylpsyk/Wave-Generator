import pyaudio
import numpy as np

from .constants import SAMPLE_RATE, CHUNK, CHANNELS

FORMAT = pyaudio.paInt16


class Detector:

    # IMPORTANT!!!!!!
    # ========================================================================================================================
    # TO USE FREQUENCY DETECTION, IT HAS TO BE USED AS A GENERATOR
    # FORMAT GIVEN BELOW

    # detection_generator = detector.start_detection()
    # while True:
    #     print(detection_generator.__next__())

    # ========================================================================================================================
    # EVEN MORE IMPORTANT!!!!!!!
    # ========================================================================================================================
    # ALWAYS, AND I REPEAT, ALWAYS
    # CALL detector.stop_detection() AFTER USING THIS.
    # IMPERATIVE

    def __init__(self):
        self.__stop_detection = False
        self.most_probable_frequency = 0

    def __find_highest_probable_frequency(self, noisy_array) -> int:
        array_length = len(noisy_array)

        f_hat = np.fft.fft(noisy_array, SAMPLE_RATE)

        PSD = (f_hat * np.conj(f_hat)) / array_length
        PSD = np.real(PSD)
        PSD = PSD[:array_length // 2]

        return np.argmax(PSD)

    def stop_detection(self) -> None:
        self.__stop_detection = True

    def start_detection(self) -> None:
        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=SAMPLE_RATE,
                            input=True,
                            output=True,
                            frames_per_buffer=CHUNK)

        while not self.__stop_detection:
            data = stream.read(CHUNK)
            data_np = np.frombuffer(data, dtype=np.int16)

            self.most_probable_frequency = self.__find_highest_probable_frequency(
                data_np)

            yield self.most_probable_frequency

        self.__stop_detection = False
        stream.close()
        audio.terminate()