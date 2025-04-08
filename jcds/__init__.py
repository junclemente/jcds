import inspect as pyinspect

from . import eda
from . import aws
from . import dataio

__all__ = ["eda", "aws", "dataio", "help"]


def help(func_name=None, namespace=None):
    """
    Central help dispatcher.

    Parameters
    ----------
    func_name : str or None
        The function name to get help for. If None, lists available functions.
    namespace : dict or None
        The module namespace (e.g., globals()) to inspect. If None, uses jcds globals.
    """
    if namespace is None:
        namespace = globals()

    functions = {
        name: namespace[name]
        for name in namespace
        if name != "help" and callable(namespace.get(name))
    }

    if func_name is None:
        print("Available functions in jcds:")
        for name in sorted(functions):
            print(f"  - {name}")
        print('\nUse jcds.help("function_name") to see its documentation.')
    else:
        func = functions.get(func_name)
        if func:
            print(f"\nHelp for '{func_name}':\n")
            print(pyinspect.getdoc(func) or "(No docstring provided)")
        else:
            print(f"Function '{func_name}' not found.")
