
import dir_1
import dir_2

from dir_2 import child_2

if __name__ == "__main__":

    print("This is main.py -- from the root directory")
    dir_1.func_dir_1()
    dir_1.child_1.func_child_1()

    dir_2.func_dir_2()
    child_2.func_child_2()
