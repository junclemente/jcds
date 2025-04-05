import pkgutil
import importlib
import inspect
import jcds


def help(func_name=None):
    """
    Global help function for the jcds package.

    - Call help() to list all public functions from all submodules.
    - Call help('function_name') to view its documentation.
    """
    functions = {}

    # Dynamically import and inspect all top-level jcds submodules
    for _, mod_name, _ in pkgutil.iter_modules(jcds.__path__):
        full_name = f"jcds.{mod_name}"
        try:
            module = importlib.import_module(full_name)

            if hasattr(module, "__all__"):
                for name in module.__all__:
                    obj = getattr(module, name, None)
                    if callable(obj) and name != "help":
                        functions[name] = obj
        except Exception as e:
            print(f"[Warning] Could not load module {full_name}: {e}")

    if func_name is None:
        if not functions:
            print("No functions found in jcds.")
        else:
            print("Available functions in jcds:")
            for name in sorted(functions):
                print(f"  - {name}")
            print('\nUse jcds.help("function_name") to see its documentation.')
    else:
        func = functions.get(func_name)
        if func:
            print(f"\nHelp for '{func_name}':\n")
            print(inspect.getdoc(func) or "(No docstring provided)")
        else:
            print(f"Function '{func_name}' not found.")
