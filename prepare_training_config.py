"""This file prepares config files for training"""
import os
from subprocess import check_call
from prepare_merlin import replace


if __name__ == '__main__':

    global_settings_path = 'merlin/egs/build_your_own_voice/s1/conf/global_settings.cfg'

    label_folder = 'merlin/egs/build_your_own_voice/s1/database/labels/label_state_align'
    num_labels = len(os.listdir(label_folder))

    replace(global_settings_path, 'Train=1000', 'Train={}'.format(num_labels - 5))
    replace(global_settings_path, 'Valid=50', 'Valid={}'.format(4))
    replace(global_settings_path, 'Test=50', 'Test={}'.format(1))

    check_call(['./04_prepare_conf_files.sh',
                'conf/global_settings.cfg'],
               cwd='./merlin/egs/build_your_own_voice/s1')
