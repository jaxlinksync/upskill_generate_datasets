"""This file prepares Merlin"""
from subprocess import check_call
from tempfile import mkstemp
from shutil import move
from os import remove
import config


def replace(source_file_path, pattern, substring):
    fh, target_file_path = mkstemp()
    with open(target_file_path, 'w') as target_file:
        with open(source_file_path, 'r') as source_file:
            for line in source_file:
                target_file.write(line.replace(pattern, substring))
    remove(source_file_path)
    move(target_file_path, source_file_path)


if __name__ == '__main__':
    check_call(['./01_setup.sh', 'myvoice'], cwd='./merlin/egs/build_your_own_voice/s1')

    path = 'merlin/egs/build_your_own_voice/s1/conf/global_settings.cfg'

    replace(path, 'SamplingFreq=16000', 'SamplingFreq={}'.format(config.SAMPLING_RATE))
    replace(path, 'bin/htk', 'htk/HTKTools')
