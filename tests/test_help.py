import jcds


def test_help_lists_functions(capsys):
    """Test that jcds.help() prints available functions."""
    jcds.help()
    captured = capsys.readouterr()
    assert "Available functions in jcds:" in captured.out
    assert "data_info" in captured.out
    assert "data_quality" in captured.out


def test_help_shows_docstring(capsys):
    """Test that jcds.help(func_name) shows a docstring."""
    jcds.help("data_info")
    captured = capsys.readouterr()
    assert "Help for 'data_info'" in captured.out


def test_help_unknown_function(capsys):
    """Test that jcds.help() handles unknown function gracefully."""
    jcds.help("nonexistent_function")
    captured = capsys.readouterr()
    assert "not found" in captured.out


def test_help_includes_transform_functions(capsys):
    """Test that jcds.help() includes transform module functions."""
    jcds.help()
    captured = capsys.readouterr()
    assert "to_int" in captured.out
    assert "clean_column_names" in captured.out


def test_help_includes_charts_functions(capsys):
    """Test that jcds.help() includes charts module functions."""
    jcds.help()
    captured = capsys.readouterr()
    assert "correlation_heatmap" in captured.out
    assert "outlier_boxplots" in captured.out
    assert "missing_data_heatmap" in captured.out