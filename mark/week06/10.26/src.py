import shutil

with open('test') as f1:
    with open('test2', 'w+') as f2:
        shutil.copytree(f1, f2)


        filter
