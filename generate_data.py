import os
import sys
import shutil
import ast

def rename_wav_files(folder, prefix="sj", digits=3):
    i = 0
    for f in sorted(os.listdir(folder)):
        if True:
            os.rename(os.path.join(folder, f),
                      os.path.join(folder, (prefix + '_{}.wav').format(str(i).zfill(digits))))
            i += 1
    print('{} files renamed'.format(i))

def generate_txt_files():
        txtdir = 'txt/'
        if not os.path.exists(txtdir):
                os.makedirs(txtdir)
        List = open("data.txt").readlines()
        for li in List:
                item = ast.literal_eval(li)
                save_location = txtdir + item[0] + ".txt"
                f = open(save_location, "w+")
                f.write(item[1])
                f.close()
                print(save_location + ": " + item[1])
if __name__ == '__main__':
        arguments = sys.argv[1:]

        if(len(arguments) > 3):
                raise IOError("Arguments must not be greater than %d" % 3)
        original_folder, processed_folder, prefix = arguments[:]
        if not os.path.exists(processed_folder):
                shutil.copytree(original_folder, processed_folder)

        rename_wav_files(processed_folder, prefix)
        generate_txt_files();
