import pkgutil
import importlib
import inspect


def help(func_name=None):
    """
    Global help function for the jcds package.

    - Call help() to list all public functions from submodules.
    - Call help('function_name') to see the docstring for that function.
    """
    import jcds

    functions = {}

    # Iterate over all submodules in the jcds package
    for _, module_name, ispkg in pkgutil.iter_modules(jcds.__path__):
        if ispkg:
            continue  # skip sub-packages, only go one level deep

        try:
            full_module_name = f"jcds.{module_name}"
            module = importlib.import_module(full_module_name)

            # Get public functions (not starting with _)
            for name, obj in inspect.getmembers(module, inspect.isfunction):
                if not name.startswith("_"):
                    functions[name] = obj
        except Exception as e:
            print(f"Warning: Could not inspect module {module_name}: {e}")

    if func_name is None:
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
