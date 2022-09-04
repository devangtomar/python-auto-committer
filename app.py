import glob
import random
import os
import datetime
import argparse
from datetime import timedelta

def generate_commit(dir, startcdata):
    print('Inside the generate_commit function!')

    # * Changing into the target dir
    os.chdir(dir)

    dividing_date = startcdata.split('-',2)
    captured_date = datetime.datetime(int(dividing_date[0]), int(dividing_date[1]), int(dividing_date[2]))
    print(captured_date)

    commit_msg = ['updating ', 'adding ', 'creating ', 'modifying ', 'generating ', 'making ', 'attaching ', 'prepend ', 'adjoining ', 'affix ']
    # get_dir_file = 'find . -maxdepth 2 -type f | xargs -I {} git add {} && git commit -m \'' + random.choice(commit_msg) + ' file : {} \' --date 2017-06-20'

    captured_files = []
    for path, subdirs, files in os.walk(dir):
        for name in files:
            # print(os.path.join(path, name))
            captured_files.append(os.path.join(path, name))

    commit_date = captured_date
    for file in captured_files:
        commit_date = commit_date + timedelta(days=random.randint(0,1))
        print(str(commit_date)[:10])
        print(os.path.basename(file))
        os.system('git add ' + file + ' && git commit -m \'' + random.choice(commit_msg) + ' the file ' + os.path.basename(file) + ' \' --date ' + str(commit_date)[:10])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, required=True)
    parser.add_argument('--startcdata', type=str, required=True)

    try:
        args = parser.parse_args()
        dir = args.dir
        startcdata = args.startcdata

        generate_commit(dir, startcdata)

    except Exception as e:
        print('Error encountered : ' + str(e))
