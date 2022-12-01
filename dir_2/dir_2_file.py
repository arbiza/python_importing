
import os
import dir_1


def func_dir_2():
    print(" |---- This is dir_2.py")


def get_this_filename():
    return os.path.basename(__file__)


def access_dir_1():
    print(" |---- This is {} accessing {}".format(get_this_filename(),
          dir_1.get_this_filename()))
