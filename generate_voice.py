"""This file trains the duration model"""
import os
from subprocess import check_call
from shutil import copy


if __name__ == '__main__':
    for txt in os.listdir('txt'):
        merlin_txt_folder = 'merlin/egs/build_your_own_voice/' \
                            's1/experiments/myvoice/test_synthesis/txt'
        copy(os.path.join('txt', txt),
             merlin_txt_folder)
        with open(os.path.join(merlin_txt_folder, txt), 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('The ' + content)

    check_call(['./07_run_merlin.sh',
                'experiments/myvoice/test_synthesis/txt',
                'conf/test_dur_synth_myvoice.conf',
                'conf/test_synth_myvoice.conf'],
               cwd='./merlin/egs/build_your_own_voice/s1')

    results_folder = 'merlin/egs/build_your_own_voice/s1/experiments/myvoice/test_synthesis/wav'

    if not os.path.exists('generated_wav'):
        os.mkdir('generated_wav')

    for wav in os.listdir(results_folder):
        copy(os.path.join(results_folder, wav), 'generated_wav')
