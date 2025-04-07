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

    Docstring generated with assistance from ChatGPT.
    """

    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    yellow = "\033[1;33m"
    red = "\033[1;31m"
    reset = "\033[0m"

    print(f"{cyan}>>> EXECUTING {yellow}{code}{reset}")
