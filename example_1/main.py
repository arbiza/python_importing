
import dir_1
import dir_2

from dir_1 import child_1
from dir_2 import child_2

if __name__ == "__main__":

    print(" |")
    print(" |")
    print(" |- This is main.py -- from the root directory")
    print(" |")
    dir_1.func_dir_1()
    dir_1.child_1.func_child_1()
    print(" |")
    dir_2.func_dir_2()
    child_2.func_child_2()
    print(" |")
    print(" |- This is main.py, again, accessing all files")
    print(" |    - ", dir_1.get_this_filename())
    print(" |    - ", child_1.get_this_filename())
    print(" |    - ", dir_2.get_this_filename())
    print(" |    - ", child_2.get_this_filename())
    print(" |")
    dir_1.access_dir_2()
    child_1.access_child_2()
    print(" |")
    dir_2.access_dir_1()
    child_2.access_child_1()
