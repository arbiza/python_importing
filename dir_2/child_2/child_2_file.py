
import os
from dir_1 import child_1


def func_child_2():
    print("       |---- This is child_2.py")


def get_this_filename():
    return os.path.basename(__file__)


def access_child_1():
    print("       |---- This is {} accessing {}".format(get_this_filename(),
          child_1.get_this_filename()))
