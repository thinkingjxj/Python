import shutil

file_names = []
def ignore(src, file_names):
    return set(filter(lambda x: x.startwith('a'), file_names))

shutil.copytree('e:/tmp', 'e:/ttmp/o', ignore=ignore)


# lambda src, names: set(filter(lambda x: x.startwith('t'), file_names))
# lambda src, names: set(filter(lambda x: not x.startwith('t'), file_names))



