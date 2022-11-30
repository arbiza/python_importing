
import os
from dir_2 import child_2


def func_child_1():
    print("       |---- This is child_1.py")


def get_this_filename():
    return os.path.basename(__file__)


def access_child_2():
    print("       |---- This is {} accessing {}".format(get_this_filename(),
          child_2.get_this_filename()))
