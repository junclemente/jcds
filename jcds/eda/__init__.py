import sys
import jcds.utils

# Import your functions from internal files
from .datetime import create_dt_col, create_dt_cols

from .lists import get_cat_list, get_cont_list, list_unique_values

from .inspect import (
    show_shape,
    show_dupes,
    show_catvar,
    show_convar,
    show_lowcardvars,
    count_rows_with_any_na,
    count_rows_with_all_na,
    count_cols_with_any_na,
    count_cols_with_all_na,
    count_total_na,
    count_unique_values,
    show_binary_list,
)

from .reports import dqr_cat, dqr_cont, quick_report, long_report, display_all_col_head

from .transform import rename_col

from .univariate import describe_categorical, plot_categorical

from .multivariate import correlation_matrix, plot_correlation_heatmap


help = jcds.utils._make_module_help(sys.modules[__name__])


# Declare what this module exports
__all__ = [
    "dqr_cat",
    "dqr_cont",
    "quick_report",
    "long_report",
    "display_all_col_head",
    "get_cat_list",
    "get_cont_list",
    "list_unique_values",
    "show_shape",
    "show_dupes",
    "show_catvar",
    "show_convar",
    "show_lowcardvars",
    "count_rows_with_any_na",
    "count_rows_with_all_na",
    "count_cols_with_any_na",
    "count_cols_with_all_na",
    "count_total_na",
    "count_unique_values",
    "show_binary_list",
    "rename_col",
    "create_dt_col",
    "create_dt_cols",
    "describe_categorical",
    "plot_categorical",
    "correlation_matrix",
    "plot_correlation_heatmap",
    "help",
]
