def print_code_line(code):
    """
    Prints a formatted code line in bold magenta for better visibility.

    Args:
        code (str): The line of code to print.
    """
    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    yellow = "\033[1;33m"
    red = "\033[1;31m"
    reset = "\033[0m"

    print(f"{cyan}>>> EXECUTING {yellow}{code}{reset}")
