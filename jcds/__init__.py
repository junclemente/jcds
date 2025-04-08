from . import eda
from . import aws
from . import dataio

__all__ = ["eda", "aws", "dataio", "help"]


def help(func_name=None, namespace=None):
    """
    Unified help system for the jcds package.

    Parameters
    ----------
    func_name : str or None
        If provided, shows the docstring for the named function.
        If None, lists all available public functions.
    namespace : dict or None
        Internal override used to pass a custom namespace.
        If None, collects all callable functions from jcds submodules.
    """
    import inspect as pyinspect
    from jcds import eda, aws, dataio

    if namespace is None:
        namespace = {}

        # Dynamically collect public callables from submodules
        for mod in [eda, aws, dataio]:
            for name in dir(mod):
                # Skip all dunder names like __file__, __name__, etc.
                if name.startswith("__") and name.endswith("__"):
                    continue
                obj = getattr(mod, name)
                if callable(obj):
                    namespace[name] = obj

    functions = {name: obj for name, obj in namespace.items() if name != "help"}

    if func_name is None:
        print("Available functions in jcds:\n")
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
