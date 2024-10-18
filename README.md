# jcds
A collection of functions for use in data science and analysis

# How to Use

This module can be imported into your jupyter notebook by using the `httpimport` library. 

```python
import httpimport

with httpimport.github_repo('junclemente', 'jcds', ref='<branch>'):
    import jcds as jcds
```
For <branch>, enter the branch you want to use. 
The `develop` branch will be constantly changing as I add more features or change some functions. 
The numbered branches, i.e.: 0.1.0, or the `main` branch will not be changed once created. 
So, plan to use a numbered branch so that your code doesn't break when I make changes to the `develop` branch.  

You can also import just the individual folders:
```python
import jcds.eda as eda
```



