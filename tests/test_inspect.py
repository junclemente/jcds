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
    assert result["Category"] == 3
    assert result["Numeric"] == 3


def test_count_unique_values_with_empty_column(empty_col_df):
    result = eda.count_unique_values(empty_col_df, ["Empty"])
    assert result["Empty"] == 1


def test_count_unique_values_with_mixed_types(unique_test_df):
    result = eda.count_unique_values(unique_test_df, ["Mixed"])
    assert result["Mixed"] == 4


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


def test_count_id_like_columns(id_like_df):
    result = eda.count_id_like_columns(id_like_df, threshold=0.95)
    assert result == 2


def test_get_dtype_summary(sample_df):
    result = eda.get_dtype_summary(sample_df)
    assert isinstance(result, dict)
    assert result.get(np.dtype("int64"), 0) >= 1
    assert result.get(np.dtype("float64"), 0) >= 1
    assert result.get(np.dtype("object"), 0) >= 1
