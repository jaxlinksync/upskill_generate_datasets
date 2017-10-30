"""This file trains the duration model"""
from subprocess import check_call


if __name__ == '__main__':

    check_call(['./06_train_acoustic_model.sh',
                'conf/acoustic_myvoice.conf'],
               cwd='./merlin/egs/build_your_own_voice/s1')
