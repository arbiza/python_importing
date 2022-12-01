
import os
import dir_2


def func_dir_1():
    print(" |---- This is dir_1.py")


def get_this_filename():
    return os.path.basename(__file__)


def access_dir_2():
    print(" |---- This is {} accessing {}".format(get_this_filename(),
          dir_2.get_this_filename()))
