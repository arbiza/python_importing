# Notes

In this branch, the project is split in two directories:

- __example\_1__ contains the files worked up to this point
- __example\_2__ contains a 'src' and 'test' structure, that is closer to a real project.

The objective is to test a function in a file in the 'src' directory using a test in the 'tests' directory.

The 'src' directory has the only one \__init\__.py file in this example with the following content:

```python
# src/__init__.py
from .main import dumb_echo
```

In tests/test_example_2.py there is the following import:

```python
from example_2 import src
```

And then, the function in 'src/main.py' can be accessed below from 'tests/test_example_2.py' as follows:

```python
src.main.dumb_echo('some string')
```

At this point, running 'test_example_2.py' may result in the __following error__:

```
Traceback (most recent call last):
  File "~/projects/python_importing/example_2/tests/test_example_2.py", line 6, in <module>
    from example_2 import src
ModuleNotFoundError: No module named 'example_2'
```

This happens when Python can't find the directory to be imported, 'example_2' in this case.

The PYTHONPATH environment variable helps to solve this issue. Before setting the path, let's make use of the file 'list\_python\_path.py' to check what Python has as path:

```bash
~/projects/python_importing/example_2/tests $ python list_python_path.py

~/projects/python_importing/example_2/tests
/usr/lib/python310.zip
/usr/lib/python3.10
/usr/lib/python3.10/lib-dynload
~/.local/lib/python3.10/site-packages
/usr/lib/python3.10/site-packages
```

Now, let's add the project's root directory to the PYTHONPATH variable:

```bash
~/projects/python_importing/example_2/tests $ cd ../..
~/projects/python_importing $ export PYTHONPATH="${PYTHONPATH}:$PWD"
```

Now, if we run the same script as before, we see this project as part of the Python's path:

```bash
~/projects/python_importing $ cd example_2/tests
~/projects/python_importing/example_2/tests $ python list_python_path.py

~/projects/python_importing/example_2/tests
~/projects/python_importing
/usr/lib/python310.zip
/usr/lib/python3.10
/usr/lib/python3.10/lib-dynload
~/.local/lib/python3.10/site-packages
/usr/lib/python3.10/site-packages
```

__Why to set the PYTHONPATH from the root directory, and not from 'example_2' or 'tests'?__

_Python needs "to see" the directory being imported. From the root directory, Python "sees" the "example\_2" directory, but it doesn't from "example\_2" or "tests" directories._

# Running

The examples start from the root directory (python_importing):

## Example 1

```
cd example_1
python main.py
```

## Example 2

```bash
export PYTHONPATH="${PYTHONPATH}:$PWD"
cd example_2/tests
python test_example_2.py
# AND/OR
pytest -v --capture=no
```
