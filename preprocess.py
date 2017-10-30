"""This file contains the functions and main script to preprocess the original wav files"""
import os
import shutil
from subprocess import check_call
import config


def rename_wav_files(folder):
    """Rename wav files in folder alphabetically to 'myvoice_xxxx.wav' e.g. myvoice_0012.wav

    Args:
        folder (str): folder path
    """

    i = 0
    for f in sorted(os.listdir(folder)):
        if True:
            os.rename(os.path.join(folder, f),
                      os.path.join(folder, 'myvoice_{}.wav'.format(str(i).zfill(4))))
            i += 1
    print('{} files renamed'.format(i))


def preprocess_wav_files(folder):
    """Converts wav files in folder to mono 48KHz sampling

    Args:
        folder (str): folder path
    """
    temp_filename = os.path.join('/tmp/sox_processed.wav')

    i = 0
    for f in sorted(os.listdir(folder)):
        command = ['sox', '-v', '0.97', os.path.join(folder, f), '--channels', '1',
                   '--rate', config.SAMPLING_RATE, temp_filename]
        check_call(command)
        os.rename(temp_filename, os.path.join(folder, f))
        i += 1
    print('{} files resampled with sox'.format(i))

if __name__ == '__main__':
    ORIGINAL_WAV_FOLDER = config.ORIGINAL_WAV_FOLDER
    PREPROCESSED_WAV_FOLDER = config.PREPROCESSED_WAV_FOLDER

    if not os.path.exists(PREPROCESSED_WAV_FOLDER):
        shutil.copytree(ORIGINAL_WAV_FOLDER, PREPROCESSED_WAV_FOLDER)

    rename_wav_files(PREPROCESSED_WAV_FOLDER)

    preprocess_wav_files(PREPROCESSED_WAV_FOLDER)
