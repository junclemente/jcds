# Changelog

All notable changes to this project will be documented in this file.
This project follows [Semantic Versioning](https://semver.org/) and loosely follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

---
## [v0.2.2] - (in progress)

### Added

- `eda_helpers.py`
    - `show_shapes`
    - `show_dupes`
    - `show_convar`
    - `show_catvar`
    - `show_lowcardvars`

### Changed
- `eda/__init__.py` updated to include `eda_helpers.py`
- `list_unique_values` updated to handle single column names or list of column names

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
