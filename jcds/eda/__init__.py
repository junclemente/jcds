import inspect

# Import your functions from internal files
from .reports import dqr_cat, dqr_cont, quick_report, long_report, display_all_col_head

from .lists import get_cat_list, get_cont_list

# Declare what this module exports
__all__ = [
    "dqr_cat",
    "dqr_cont",
    "quick_report",
    "long_report",
    "display_all_col_head",
    "get_cat_list",
    "get_cont_list",
    "help",
]


# Dynamically generated help function
def help(func_name=None):
    """
    Help function for this submodule.

    - Call help() to list all public functions.
    - Call help('function_name') to view its documentation.
    """
    functions = {
        name: globals()[name]
        for name in __all__
        if name != "help" and callable(globals().get(name))
    }

    if func_name is None:
        print("Available functions in this module:")
        for name in sorted(functions):
            print(f"  - {name}")
        print('\nUse help("function_name") to see its documentation.')
    else:
        func = functions.get(func_name)
        if func:
            print(f"\nHelp for '{func_name}':\n")
            print(inspect.getdoc(func) or "(No docstring provided)")
        else:
            print(f"Function '{func_name}' not found.")
