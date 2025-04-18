# utils.py
import warnings
import functools


def print_code_line(code):
    """
    Print a formatted code line in bold magenta for better visibility.

    Parameters
    ----------
    code : str
        The line of code to print.

    Returns
    -------
    None
        This function prints to the console and does not return a value.

    """

    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    yellow = "\033[1;33m"
    red = "\033[1;31m"
    reset = "\033[0m"

    print(f"{cyan}>>> EXECUTING {yellow}{code}{reset}")


def deprecated(reason: str = "", version: str = "future"):
    """
    A decorator to mark functions as deprecated and show a formatted warning.

    Parameters
    ----------
    reason : str
        Explanation of what to use instead.
    version : str
        Version when the function will be removed.

    Returns
    -------
    Callable
        Wrapped function with DeprecationWarning and banner print.
    """

    def decorator(func):
        msg = f"`{func.__name__}()` is deprecated and will be removed in v{version}."
        if reason:
            msg += f" {reason}"

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Terminal/Notebook banner with yellow color
            YELLOW = "\033[93m"
            RESET = "\033[0m"

            banner = (
                "\n"
                + "=" * 60
                + "\n"
                + "⚠️  DEPRECATION WARNING".center(60)
                + "\n"
                + "-" * 60
                + "\n"
                + msg
                + "\n"
                + "=" * 60
                + "\n"
            )
            print(YELLOW + banner + RESET)

            # Official warning (so tools like pytest pick it up)
            warnings.warn(msg, DeprecationWarning, stacklevel=2)

            return func(*args, **kwargs)

        return wrapper

    return decorator


def _make_module_help(module):
    """
    Returns a help() function bound to the given module.

    Parameters
    ----------
    module : module
        The actual module (e.g., pass in `sys.modules[__name__]` from the caller).

    Returns
    -------
    Callable
        A custom help() function that introspects only the module’s public API.
    """

    def _help(func_name=None):
        from jcds import help as base_help

        # Filter out dunder names and non-callables
        filtered_namespace = {
            k: v
            for k, v in vars(module).items()
            if callable(v) and not (k.startswith("__") and k.endswith("__"))
        }

        return base_help(func_name, namespace=filtered_namespace)

    return _help
