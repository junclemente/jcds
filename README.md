# jcds
A collection of functions for use in data science and analysis

# How to Use

This module can be imported into your jupyter notebook by using the `httpimport` library. 

```python
import httpimport

with httpimport.github_repo('junclemente', 'jcds', ref='<branch'):
    import jcds as jcds
```

You can also import just the individual folders:
```python
import jcds.eda as eda
```



