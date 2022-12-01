# Notes

After adding a subdirectory (e.g.: child_1) and updating its \__init\__.py file as follows:

```python
from .dir_1_file import func_dir_1
from .child_1 import child_1_file
```

The subdirectories can be used as modules in main.py in two different ways:

```python
from dir_2 import child_2

    child_2.func_child_2()
```

or accessing the function thought the file as follows:

```python
    dir_1.child_1_file.func_child_1()
```

# Running

From the root directory, run:

```
python main.py
```
