from . import eda
from . import aws
from . import dataio
from . import reports
from . import transform
from . import charts 


__all__ = ["eda", "aws", "dataio", "reports", "transform", "charts","help"]




def help(func_name=None, namespace=None):
    import inspect as pyinspect
    from jcds import eda, aws, dataio, reports, transform, charts

    if namespace is None:
        namespace = {}

        for mod in [eda, aws, dataio, reports, transform, charts]:
            # Use __all__ if available, otherwise fall back to dir()
            names = getattr(mod, "__all__", dir(mod))
            for name in names:
                if name.startswith("__") and name.endswith("__"):
                    continue
                if name == "help":
                    continue
                obj = getattr(mod, name, None)
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