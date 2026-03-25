from jcds import eda
import pandas as pd
import numpy as np


def test_show_shape_returns_correct_shape(sample_df):
    rows, cols = eda.show_shape(sample_df)
    assert rows == 10
    assert cols == 5


def test_show_dupes_returns_zero_for_clean_samples(sample_df):
    assert eda.show_dupes(sample_df) == 0


def test_show_catvar_returns_object_columns(sample_df):
    cat_vars = eda.show_catvar(sample_df)
    assert "Gender" in cat_vars
    assert "Age" not in cat_vars
    assert isinstance(cat_vars, list)


def test_show_convar_returns_numerical_columns(sample_df):
    con_vars = eda.show_convar(sample_df)
    assert "ID" in con_vars
    assert "Subscribed" in con_vars
    assert "Gender" not in con_vars
    assert isinstance(con_vars, list)


def test_show_convar_excludes_datetime(datetime_parsed_df):
    result = eda.show_convar(datetime_parsed_df)
    assert "timestamp" not in result


def test_show_lowcardvars_filters_by_cardinality(lowcard_df):
    result = eda.show_lowcardvars(lowcard_df, max_unique=3)
    assert isinstance(result, list)
    assert ("City", 3) in result
    assert ("State", 2) in result
    assert ("Zip", 3) in result
    assert not any(col for col in result if col[0] == "ID")


def test_count_rows_with_any_na(na_test_df):
    assert eda.count_rows_with_any_na(na_test_df) == 4


def test_count_rows_with_all_na(na_test_df):
    assert eda.count_rows_with_all_na(na_test_df) == 0


def test_count_cols_with_any_na(na_test_df):
    assert eda.count_cols_with_any_na(na_test_df) == 3


def test_count_cols_with_all_na(na_test_df):
    assert eda.count_cols_with_all_na(na_test_df) == 1


def test_count_total_na(na_test_df):
    assert eda.count_total_na(na_test_df) == 8


def test_count_unique_values_basic(unique_test_df):
    result = eda.count_unique_values(unique_test_df, ["Category", "Numeric"])
    assert result["Category"]["unique_count"] == 3
    assert result["Category"]["top_modes"] == [("A", 2), ("B", 2)]


def test_count_unique_values_with_empty_column(empty_col_df):
    result = eda.count_unique_values(empty_col_df, ["Empty"])
    assert result["Empty"]["unique_count"] == 1
    assert result["Empty"]["top_modes"] == [(None, 4)]


def test_count_unique_values_with_mixed_types(unique_test_df):
    result = eda.count_unique_values(unique_test_df, ["Mixed"])
    assert result["Mixed"]["unique_count"] == 4
    assert result["Mixed"]["top_modes"] == [(1, 2), ("1", 1)]


def test_show_binary_list(binary_list_df):
    result = eda.show_binary_list(binary_list_df)
    assert isinstance(result, dict)
    assert "binary_columns" in result
    assert "binary_with_nan" in result
    assert set(result["binary_columns"]) == {"bin_clean"}
    assert set(result["binary_with_nan"]) == {"bin_with_nan"}
    excluded = {"not_bin_3vals", "not_bin_unique", "all_nan"}
    combined = set(result["binary_columns"]) | set(result["binary_with_nan"])
    assert excluded.isdisjoint(combined)


def test_show_highcardvars(unique_test_df):
    result = eda.show_highcardvars(unique_test_df, percent_unique=60)
    assert isinstance(result, list)
    assert ("Mixed", 60.0) in result
    assert ("Category", 60.0) in result


def test_show_highcardvars_all_unique(highcard_unique_df):
    result = eda.show_highcardvars(highcard_unique_df, percent_unique=90)
    assert ("ID", 100.0) in result
    assert len(result) == 1


def test_show_highcardvars_all_same(highcard_same_df):
    result = eda.show_highcardvars(highcard_same_df, percent_unique=90)
    assert result == []


def test_show_highcardvars_exact_threshold(highcard_threshold_df):
    result = eda.show_highcardvars(highcard_threshold_df, percent_unique=80)
    assert ("Code", 80.0) in result


def test_show_highcardvars_with_nan(highcard_with_nan_df):
    result = eda.show_highcardvars(highcard_with_nan_df, percent_unique=60)
    assert "State" in [col for col, _ in result]


def test_show_constantvars_basic(constantvars_df):
    result = eda.show_constantvars(constantvars_df)
    assert "A" in result
    assert "B" in result
    assert "C" not in result
    assert len(result) == 2


def test_show_datetime_columns(datetime_parsed_df):
    result = eda.show_datetime_columns(datetime_parsed_df)
    assert result == ["timestamp"]


def test_show_possible_datetime_columns(possible_datetime_df):
    result = eda.show_possible_datetime_columns(possible_datetime_df)
    assert "date_strings" in result
    assert "random_strings" not in result
    assert "mixed" not in result  # Below threshold if default is 80%


def test_show_mixed_type_columns(mixed_type_df):
    result = eda.show_mixed_type_columns(mixed_type_df)
    assert "mixed" in result
    assert "more_mixed" in result
    assert "clean" not in result


def test_show_mixed_type_columns_ignores_nan(sample_df):
    # sample_df has NaN values in string columns — should not be flagged as mixed
    result = eda.show_mixed_type_columns(sample_df)
    assert "Gender" not in result  # Gender has NaN but is still just strings


def test_show_mixed_type_columns_ignores_numpy_str(sample_df):
    # Converting to str can produce numpy.str_ mixed with str — should not be flagged
    df = sample_df.copy()
    df["Gender"] = df["Gender"].astype(str)
    result = eda.show_mixed_type_columns(df)
    assert "Gender" not in result


def test_count_id_like_columns(id_like_df):
    result = eda.count_id_like_columns(id_like_df, threshold=0.95)
    assert result == 2


def test_get_dtype_summary(sample_df):
    result = eda.get_dtype_summary(sample_df)
    assert isinstance(result, dict)
    assert result.get("int", 0) >= 1
    assert result.get("float", 0) >= 1
    assert result.get("object", 0) >= 1


def test_show_memory_use_returns_float(sample_df):
    result = eda.show_memory_use(sample_df)
    assert isinstance(result, float)
    assert result > 0  # assuming non-empty dataframe


def test_get_dtype_summary_keys_are_strings(sample_df):
    result = eda.get_dtype_summary(sample_df)
    assert isinstance(result, dict)
    expected_keys = {"object", "int", "float", "bool", "category", "datetime", "other"}
    assert expected_keys.issubset(result.keys())
    assert all(isinstance(k, str) for k in result)
    assert all(isinstance(v, int) for v in result.values())


def test_show_nearconstvars_detects_near_constant_columns(nearconst_test_df):
    result = eda.show_nearconstvars(nearconst_test_df)
    assert "almost_constant" in result
    ...


def test_show_missing_summary_filters_by_threshold(missing_data_df):
    # Without threshold
    result = eda.show_missing_summary(missing_data_df)
    assert result == {"D": (5, 100.0), "B": (2, 40.0), "A": (1, 20.0)}

    # With threshold = 30%
    result_thresh = eda.show_missing_summary(missing_data_df, threshold=30)
    assert result_thresh == {"D": (5, 100.0), "B": (2, 40.0)}

    # With threshold = 100%
    result_100 = eda.show_missing_summary(missing_data_df, threshold=100)
    assert result_100 == {"D": (5, 100.0)}

    # With threshold = 101% (nothing should pass)
    result_empty = eda.show_missing_summary(missing_data_df, threshold=101)
    assert result_empty == {}


from jcds.eda.inspect import show_dimensions


def test_show_dimensions_returns_correct_values(sample_df):
    rows, cols, size, memory_use = show_dimensions(sample_df)

    assert rows == 10
    assert cols == 5
    assert size == 50
    assert isinstance(memory_use, float)


def test_show_null_rows_returns_only_null_rows(sample_df):
    result = eda.show_null_rows(sample_df)
    assert result.isnull().any(axis=1).all()
    assert len(result) < len(sample_df)


def test_show_null_rows_empty_when_no_nulls(sample_df):
    df = sample_df.dropna()
    result = eda.show_null_rows(df)
    assert len(result) == 0


def test_show_null_cols_returns_only_null_cols(missing_data_df):
    result = eda.show_null_cols(missing_data_df)
    assert result.isnull().any(axis=0).all()
    assert len(result.columns) < len(missing_data_df.columns)


def test_show_null_cols_empty_when_no_nulls(sample_df):
    df = sample_df.dropna()
    result = eda.show_null_cols(df)
    assert len(result.columns) == 0


# --- show_null_rows threshold tests ---
def test_show_null_rows_default_returns_any_null(sample_df):
    """Default threshold=0.0 should return all rows with any null (existing behavior)."""
    result = eda.show_null_rows(sample_df)
    assert result.isnull().any(axis=1).all()


def test_show_null_rows_threshold_filters_rows(na_test_df):
    """threshold=0.5 should only return rows missing >50% of values."""
    result = eda.show_null_rows(na_test_df, threshold=0.5)
    pct_missing = na_test_df.isnull().sum(axis=1) / len(na_test_df.columns)
    assert all(pct_missing[result.index] >= 0.5)


def test_show_null_rows_threshold_1_returns_empty(sample_df):
    """threshold=1.0 should return no rows since none are 100% missing."""
    result = eda.show_null_rows(sample_df, threshold=1.0)
    assert len(result) == 0


def test_show_null_rows_no_nulls_returns_empty(sample_df):
    df = sample_df.dropna()
    result = eda.show_null_rows(df, threshold=0.0)
    assert len(result) == 0


# --- show_null_cols threshold tests ---
def test_show_null_cols_default_returns_any_null(missing_data_df):
    """Default threshold=0.0 should return all cols with any null (existing behavior)."""
    result = eda.show_null_cols(missing_data_df)
    assert result.isnull().any(axis=0).all()


def test_show_null_cols_threshold_filters_cols(missing_data_df):
    """threshold=0.5 should only return cols missing >50% of values."""
    result = eda.show_null_cols(missing_data_df, threshold=0.5)
    pct_missing = missing_data_df.isnull().sum(axis=0) / len(missing_data_df)
    assert all(pct_missing[result.columns] > 0.5)


def test_show_null_cols_threshold_1_returns_empty(missing_data_df):
    """threshold=1.0 should only return cols that are 100% missing."""
    result = eda.show_null_cols(missing_data_df, threshold=1.0)
    # missing_data_df has col D which is all NaN
    assert "D" in result.columns
    assert "A" not in result.columns


def test_show_null_cols_no_nulls_returns_empty(sample_df):
    df = sample_df.dropna()
    result = eda.show_null_cols(df, threshold=0.0)
    assert len(result.columns) == 0


# --- show_outlier_summary ---
def test_show_outlier_summary_returns_dataframe(sample_df):
    """Should return a DataFrame."""
    result = eda.show_outlier_summary(sample_df)
    assert isinstance(result, pd.DataFrame)


def test_show_outlier_summary_has_correct_columns(sample_df):
    """Should have outlier_count and outlier_pct columns."""
    result = eda.show_outlier_summary(sample_df)
    assert "outlier_count" in result.columns
    assert "outlier_pct" in result.columns


def test_show_outlier_summary_sorted_descending(sample_df):
    """Should be sorted by outlier_count descending by default."""
    result = eda.show_outlier_summary(sample_df)
    assert (
        result["outlier_count"].is_monotonic_decreasing
        or result["outlier_count"].nunique() == 1
    )


def test_show_outlier_summary_custom_threshold(sample_df):
    """Should accept custom threshold."""
    result = eda.show_outlier_summary(sample_df, threshold=3.0)
    assert isinstance(result, pd.DataFrame)


def test_show_outlier_summary_pct_between_0_and_100(sample_df):
    """Outlier percentages should be between 0 and 100."""
    result = eda.show_outlier_summary(sample_df)
    assert (result["outlier_pct"] >= 0).all()
    assert (result["outlier_pct"] <= 100).all()


# --- inspect_row ---
def test_inspect_row_by_position_runs(sample_df):
    """Should run without error using position."""
    eda.inspect_row(sample_df, 0)


def test_inspect_row_by_label_runs(sample_df):
    """Should run without error using label."""
    eda.inspect_row(sample_df, 0, by="label")


def test_inspect_row_shows_column_values(capsys, sample_df):
    """Should print column names and values."""
    eda.inspect_row(sample_df, 0)
    captured = capsys.readouterr()
    assert "Age" in captured.out
    assert "Gender" in captured.out


def test_inspect_row_shows_null_count(capsys, na_test_df):
    """Should show correct null count."""
    eda.inspect_row(na_test_df, 0)
    captured = capsys.readouterr()
    assert "Null values" in captured.out


def test_inspect_row_warns_on_mostly_null(capsys, na_test_df):
    """Should warn when row is mostly null."""
    # row 0 in na_test_df has 2 nulls out of 4 cols = 50%, not enough
    # use a row that is >80% null
    df = pd.DataFrame(
        {
            "A": [None],
            "B": [None],
            "C": [None],
            "D": [None],
            "E": [1.0],
        }
    )
    eda.inspect_row(df, 0)
    captured = capsys.readouterr()
    assert "WARNING" in captured.out


def test_inspect_row_no_warning_on_clean_row(capsys, sample_df):
    """Should not warn when row has mostly non-null values."""
    eda.inspect_row(sample_df, 0)
    captured = capsys.readouterr()
    assert "WARNING" not in captured.out


def test_inspect_row_shows_null_flag(capsys, sample_df):
    """Should flag null values inline."""
    eda.inspect_row(sample_df, 6)  # row 6 has NaN in Age
    captured = capsys.readouterr()
    assert "null" in captured.out
