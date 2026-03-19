# Changelog

All notable changes to this project will be documented in this file.  
This project follows [Semantic Versioning](https://semver.org/) and loosely follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

## [0.3.0] – 2026-03-18

### Added

- **`jcds.charts` module**
  New visualization module with cleaner API (`jvis`):
  - `missing_data_heatmap()` — heatmap of missing values across the DataFrame
  - `outlier_boxplots()` — boxplots for numeric (non-binary) columns
  - `correlation_heatmap()` — heatmap of feature correlations
  - `categorical_barplot()` — bar chart for categorical variable distributions

- **`jcds.transform` module**
  New transformation module with cleaner API (`jtrf`):
  - `to_int()`, `to_float()`, `to_numeric()`, `to_str()`
  - `to_categorical()`, `to_bool()`, `to_datetime()`, `to_object()`
  - `clean_column_names()`, `rename_column()`, `delete_columns()`

- **`eda` module additions**
  - `show_null_rows()` — returns rows containing at least one null value
  - `show_null_cols()` — returns columns containing at least one null value

### Changed

- **`show_columns` default changed to `True`**
  `data_info()`, `data_cardinality()`, and `data_quality()` now show column lists by default.

- **`jcds.help()` updated**
  Now includes `reports`, `transform`, and `charts` modules in function listing.

- **`clean_column_names()` collision handling**
  Now appends numeric suffix (e.g., `first_name_1`) when two columns clean to the same name.

### Fixed

- **`show_convar()` now excludes datetime columns**
  Previously, datetime columns were incorrectly counted as numerical variables.

- **`show_mixed_type_columns()` now ignores NaN**
  Previously, columns with NaN values were incorrectly flagged as mixed type.

- **`show_mixed_type_columns()` treats `str` and `numpy.str_` as the same type**
  Prevents false positives after `to_str()` conversion.

- **`show_possible_datetime_columns()` FutureWarning suppressed**
  Added `utc=True` to `pd.to_datetime()` call to suppress pandas FutureWarning.

### Deprecated

The following `eda` functions are deprecated and will be removed in v0.4.0.
Use the `jcds.charts` equivalents instead:

- `eda.plot_outlier_boxplots()` → `charts.outlier_boxplots()`
- `eda.plot_correlation_heatmap()` → `charts.correlation_heatmap()`
- `eda.plot_categorical()` → `charts.categorical_barplot()`

The following `eda.transform` functions are deprecated and will be removed in v0.4.0.
Use the `jcds.transform` equivalents instead:

- `eda.convert_to_int()` → `transform.to_int()`
- `eda.convert_to_float()` → `transform.to_float()`
- `eda.convert_to_numeric()` → `transform.to_numeric()`
- `eda.convert_to_categorical()` → `transform.to_categorical()`
- `eda.convert_to_bool()` → `transform.to_bool()`
- `eda.convert_to_datetime()` → `transform.to_datetime()`
- `eda.convert_to_object()` → `transform.to_object()`
- `eda.clean_column_names()` → `transform.clean_column_names()`
- `eda.rename_column()` → `transform.rename_column()`
- `eda.delete_columns()` → `transform.delete_columns()`

### Documentation

- **README updated**
  Added notebook auto-install snippet with `develop`/stable branch switching logic.

### Testing

- **Test suite expanded from 87 to 120 tests**
  Added coverage for all new `charts`, `transform`, and `eda` additions.
  
## [0.2.8] – 2025‑05‑02

### Added

- **catvar_report()**  
  Introduced a new `catvar_report()` function in `reports.py` for detailed categorical-variable profiling. (2025‑04‑30)

- **plot_outlier_boxplots()**  
  Added `plot_outlier_boxplots()` to `eda.outliers` for visualizing IQR-based outliers in non-binary numeric features. (2025‑07‑21)

### Changed

- **catvar_report() display**  
  Finalized and cleaned up the display layout and formatting of `catvar_report()`. (2025‑05‑02)
- **count_unique_values() enhancements**  
  Added an `n_modes` parameter and built-in sorting to the `count_unique_values()` helper. (2025‑05‑01)
- **Tabulate support**  
  Updated code to include the `tabulate` package for nicer table output. (2025‑05‑02)
- **Deprecation messaging**  
  Revised deprecation notices to point users toward `data_info()`, `data_cardinality()`, and `data_quality()`. (2025‑04‑29)
- **Utility functions refactored**  
  Deprecated `get_cont_list()` and `get_cat_list()` in favor of the clearer `show_convar()` and `show_catvar()`. (2025‑04‑29)
- **catvar_reports rename**  
  Tidied up naming and internal references in the `catvar_reports` module to match the new API. (2025‑05‑02)

- **eda.outliers module update**  
  Updated `eda.outliers` to expose the new plotting function via the public interface and `__all__`. (2025‑07‑21)

### Deprecated

- **Automated changelog**  
  Removed the `git-cliff`–based changelog automation and reverted to manual maintenance. (2025‑04‑18)

### Documentation

- **Notebook updates**
  - Updated `eda_workflow.ipynb` with deprecation guidance and new function signatures. (2025‑04‑18)
  - Refreshed example outputs in the project notebook to reflect the latest changes. (2025‑05‑02)

### Testing

- **Test suite**  
  Updated and expanded unit tests for `count_unique_values()` to cover the new modes and sorting options. (2025‑05‑01)

- **Outlier tests**  
  Added basic unit test for `plot_outlier_boxplots()` to ensure it runs without error. (2025‑07‑21)

## [v0.2.7] - 2025-04-15

### ✨ Features

- `transform.py`:
  - Add `convert_to_int()`, `convert_to_categorical()`, `convert_to_object()`, `convert_to_datetime()`, `convert_to_numeric()`, and `convert_to_bool()` functions
  - Add `clean_column_names()` and `delete_columns()` utility functions
- `inspect.py`:
  - Add `show_dimensions()` function for quick dataset shape overview
- `eda/eda_helpers.py`:
  - Create `detect_outliers.iqr()` for outlier detection
- Cardinality Report:
  - Reformat high-cardinality output to display percent uniqueness

### 🧪 Tests

- Added unit tests for:
  - `show_dimensions()`
  - `convert_to_int()`, `convert_to_datetime()`, `convert_to_bool()`, `convert_to_numeric()`
  - `clean_column_names()`, `delete_columns()`
- Updated test suite to match function name changes (`rename_col` → `rename_column`)

### 🛠 Refactoring

- Renamed `rename_col()` to `rename_column()` across codebase and tests

### 🧹 Chores

- Updated `.gitignore` to exclude test-generated CSVs
- Added sample datasets for testing
- Added VS Code dev test notebook template: `dev_test_nb`
- Updated various notebooks for testing and demonstration
- Merged latest `main` into `develop`

### 📜 Documentation & Style

- Added docstrings to `rename_column()` and `data_quality()`
- Adjusted print formatting and divider lengths for improved readability in reports

## [v0.2.6] - 2025-04-16

### 🚀 Features

- Add `data_quality()` report function to generate structured diagnostics on missing values, duplicates, constants, near-constants, mixed types, and high cardinality variables.
- Add `show_missing_summary()` to support missing data analysis by column, with percentage filtering.
- Add `show_dimensions()` to report total entries and memory usage alongside shape.

### 🧪 Tests

- Added unit tests for `data_quality()`, `show_dimensions()`, and `show_missing_summary()` using `conftest.py` fixtures.

### 📝 Documentation

- Added comprehensive docstring for `data_quality()` outlining its use and structure.
- Updated CHANGELOG.md with release details.

## [v0.2.5] - 2025-04-16

### 🚜 Refactor

- Move project layout to use `src/` structure

### ⚙️ Miscellaneous Tasks

- Introduce automated changelog generation with `git-cliff`
- Add Makefile for release automation

---

## [v0.2.4] - 2025-04-15

### 🚀 Features

- Finalize updates for v0.2.4 ([b8574bf…])

### ⚙️ Miscellaneous Tasks

- Add changelog for v0.2.4 ([2263ab6…])

<!-- generated by git-cliff -->

---

## [v0.2.3] - 2025-04-15

### Added

- Example usage notebook: `examples/eda_workflow.ipynb` for demonstrating full EDA flow.
- **New centralized help system**:
  - Unified `help()` entry point in `jcds/__init__.py`.
  - `make_module_help()` utility in `jcds/utils.py` using `globals()`.
  - All submodules (`eda`, `aws`, `dataio`) now support contextual help:
    ```python
    jcds.eda.help("quick_report")
    jcds.aws.help()
    ```
- **New utilities in `eda.inspect`**:
  - Variable inspection: `show_constantvars`, `show_highcardvars`, `get_dtype_summary`, `show_memory_use`
  - Type detection: `show_datetime_columns`, `show_possible_datetime_columns`, `show_mixed_type_columns`, `count_id_like_columns`
- **Comprehensive unit tests for all `eda.inspect` functions** using reusable fixtures in `conftest.py`.
- **New `reports` module** (`jcds.reports`):
  - `data_info(df, show_columns=False)` — detailed dataset summary
  - `data_cardinality(df, show_columns=False)` — variable cardinality diagnostics
  - Includes full docstrings and modular registration in `__init__.py`

### Changed

- Added `DeprecationWarning` to legacy functions scheduled for removal in `v0.3.0`.
- Updated `.gitignore` to exclude test datasets and notebooks.
- Refactored submodule `__init__.py` files to use the centralized `help()` system.
- Updated `jcds/__init__.py` to explicitly expose `eda`, `aws`, and `dataio` via `__all__`.
- Ensured delayed imports in module `help()` functions to prevent circular dependencies.
- Refactored `tests/test_inspect.py` to use shared fixtures in `conftest.py`.
- Registered `data_info`, `data_cardinality`, and `help()` in `jcds/reports/__init__.py`.
- Added module-level docstring to `jcds/reports/__init__.py` to enable API documentation.
- Updated `docs/api.md` to include the `jcds.reports` section.

### Fixed

- Fixed `test_get_dtype_summary` to match string-based dtype format (e.g., `"int"`).
- Corrected test argument for `show_possible_datetime_columns`.
- Silenced deprecation warning in `get_dtype_summary` by avoiding deprecated pandas API.

### Removed

- Deleted obsolete personal test datasets from `tests/datasets/`.
- Deleted unused `tests/integration/` folder.

---

## [v0.2.2] - 2025-04-8

### Added

- **`inspect.py`** module with the following new functions:

  - `show_shape` – returns the shape of a DataFrame
  - `show_dupes` – counts duplicated rows
  - `show_catvar` – returns list of categorical (object/category) columns
  - `show_convar` – returns list of continuous (non-categorical) columns
  - `show_lowcardvars` – identifies categorical columns with low cardinality
  - `show_binary_list` – identifies binary columns (with/without NaNs)
  - `count_rows_with_any_na` – counts rows with at least one missing value
  - `count_rows_with_all_na` – counts rows where all values are missing
  - `count_cols_with_any_na` – counts columns with at least one missing value
  - `count_cols_with_all_na` – counts columns where all values are missing
  - `count_total_na` – returns the total number of missing values
  - `count_unique_values` – returns unique value counts per column  
    (Docstrings included, generated by ChatGPT.)

- **Unit tests** for all `eda_helpers.py` functions.
- Test fixtures: `create_na_test_df()` and `create_unique_test_df()` in `test_utils.py`.

- **`test_s3.py`** unit tests for the `aws/s3` module:

  - `list_s3_contents`
  - `s3_file_to_dataframe`

- **Shared test fixtures** in `tests/conftest.py` for mocking CSV/Excel downloads.

- Added automatic documentation via `mkdocs`

  - Add `docs\` folder
  - `mkdocs.yml`
  - `index.md` and `api.md`

- **`eda/datetime.py`** module with datetime feature engineering functions:

  - `create_dt_col()` – creates a single derived datetime column (e.g., `timestamp_year`)
  - `create_dt_cols()` – supports creation of multiple datetime-derived columns in one call
    - Supports: `"year"`, `"month"`, `"day"`, `"weekday"`, `"weekday_name"`, `"weekofyear"`, `"quarter"`, `"dayofyear"`, `"is_weekend"`, `"is_month_start"`, `"is_month_end"`
    - Includes validation for unsupported types and missing columns
    - Raises error if inconsistent datetime formats (e.g., mixed `"/"` and `"-"`) are detected

- **Unit tests for `eda/datetime.py`**:

  - Test coverage for both single and multi-column expansion
  - Error handling for:
    - Invalid column names
    - Unsupported `col_type`s
    - Mixed datetime formats
    - Auto-conversion of string-formatted dates

- **Refactored and consolidated test fixtures into `tests/conftest.py`**:

  - Moved all fixtures from `test_utils.py` into `conftest.py` for automatic discovery across all test files
  - Includes fixtures: `sample_df`, `na_test_df`, `unique_test_df`, `binary_list_df`, `datetime_df`, `dummy_csv_bytes`, `dummy_excel_bytes`, `mock_requests_get`

- **New test module: `tests/unit/test_datetime.py`**

  - Organized tests specifically for datetime feature extraction utilities

- New `dataio` module with `save_parquet()` and `load_parquet()` functions for reliable Parquet I/O
- Type-safe and documented with NumPy-style docstrings
- Full test coverage using reusable `sample_df` fixture from `conftest.py`
- Unit test file `test_io_utils.py` to validate read/write functionality and nested directory creation

- `save_csv()` function to `dataio` module: cleanly saves DataFrames to CSV with default `index=False` and automatic directory creation
- `load_csv()` function to `dataio` module:
  - Attempts to load a CSV file using multiple common encodings (e.g. `'utf-8'`, `'latin1'`, `'cp1252'`)
  - Provides a helpful raw byte preview if all decoding attempts fail
  - Raises informative `ValueError` for failed loads to assist with debugging corrupted or misencoded files
- Unit tests for both `save_csv()` and `load_csv()` using `sample_df` and `tmp_path`

  - Includes fallback test simulating corrupted file behavior

- `read_s3()` to `dataio.s3_io`: loads public S3-hosted CSV or Excel files into a DataFrame with built-in error handling
- Unit tests for `read_s3()`:
  - CSV and Excel load success
  - Handles unsupported file types (`ValueError`)
  - Graceful fallback on request errors (returns `None`)
- `test_s3_utils.py` to test `list_s3_bucket()` from `aws.s3_utils` with mocked `boto3.client`

### Changed

- `eda/__init__.py` updated to expose all `eda_helpers` functions.
- `list_unique_values()` updated to handle both single column names and lists.

- `test_utils.py` simplified — now only contains helper functions if needed (no more `@pytest.fixture`)
- Updated test files (`test_inspect.py`, `test_transform.py`, etc.) to rely on auto-discovered fixtures via `conftest.py`
- `eda/__init__.py` updated to expose new `datetime` functions

- Renamed `io.py` to `io_utils.py` and moved to `dataio/` to avoid namespace conflict with Python's built-in `io` module
- Updated all related imports to reflect new structure

- Renamed `s3_file_to_dataframe()` ➝ `read_s3()` for consistency with other I/O functions
- Split S3-related code:
  - `list_s3_bucket()` remains in `aws.s3_utils`
  - `read_s3()` moved to new `dataio/s3_io.py`

### Fixed

- Corrected module import paths for internal packages (`from jcds.aws.s3 import ...`).
- Configured `pytest.ini` to include the project root in `PYTHONPATH`.

- Added input validation to `create_dt_cols()` to prevent datetime parsing issues with inconsistent formats

### Notes

- Test discovery is working via `pytest`, and all tests are passing.
- Added `moto` and `requests` to `environment.yml` to support AWS and HTTP mocking.

---

## [v0.2.1] - 2025-04-01

### Added

- `utils.py`
- `print_code_line()` in `utils.py`
- `list_unique_values()` in the `eda` subpackage
- `setup.py` for pip install support
- Optional `aws` dependency group (`[aws]`) to support the `aws` module

### Changed

- Defined core library dependencies in `setup.py`
- Updated `README.md` with pip installation and optional AWS support instructions

---

## [0.2.0] - 2025-03-24

### Added

- `aws` subpackage
- `help()` function to each subpackage and the main library

---

## [0.1.0] - 2024-10-17

### Added

- First tagged version.
