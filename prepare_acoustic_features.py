"""This file prepares acoustic features"""
from subprocess import check_call
import config
import os
import shutil


if __name__ == '__main__':
    if os.path.exists('merlin/egs/build_your_own_voice/s1/database/feats'):
        print('deleting database/feats')
        shutil.rmtree('merlin/egs/build_your_own_voice/s1/database/feats')

    check_call(['./03_prepare_acoustic_features.sh',
                '../../../../{}'.format(config.PREPROCESSED_WAV_FOLDER),
                'database/feats'],
               cwd='./merlin/egs/build_your_own_voice/s1')
