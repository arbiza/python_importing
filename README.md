# Notes

By adding the __init__.py files to the directories dir_1 and dir_2, we can import these directories as modules in main.py, as below:

```python
import dir_1
import dir_2
```

The __init__.py files import the functions from the file in the current directory (.dir_X).

```python
from .dir_1 import func_dir_1
```

# Running

From the root directory, run:

```
python main.py
```
