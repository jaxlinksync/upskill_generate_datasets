"""This file trains the duration model"""
from subprocess import check_call


if __name__ == '__main__':

    check_call(['./05_train_duration_model.sh',
                'conf/duration_myvoice.conf'],
               cwd='./merlin/egs/build_your_own_voice/s1')
