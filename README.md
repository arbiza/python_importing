# Notes

Some additional functions were added. The following changes were made to make the child_1's module function accessible to child2, and the other way around:

```python
# dir_1's __init__.py
from .dir_1 import *

# dir_2's __init__.py
from .dir_2 import *
```

In the main.py file, the imports were changed to:

```python
import dir_1
import dir_2

from dir_1 import child_1
from dir_2 import child_2
```

The main function makes the calls to the functions that are accessing neighbour modules, like the ones below:

```python
dir_1.access_dir_2()
child_1.access_child_2()
dir_2.access_dir_1()
child_2.access_child_1()
```

# Running

From the root directory, run:

```
python main.py
```
