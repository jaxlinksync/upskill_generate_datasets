"""This file prepares state aligned labels"""
from subprocess import check_call
import config
import os
import shutil


if __name__ == '__main__':
    if os.path.exists('merlin/egs/build_your_own_voice/s1/database/labels'):
        print('deleting database/labels')
        shutil.rmtree('merlin/egs/build_your_own_voice/s1/database/labels')

    check_call(['./02_prepare_labels.sh',
                '../../../../{}'.format(config.PREPROCESSED_WAV_FOLDER),
                '../../../../utts.data',
                'database/labels'],
               cwd='./merlin/egs/build_your_own_voice/s1')
