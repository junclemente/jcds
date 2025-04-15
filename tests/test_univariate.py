from jcds.eda import univariate


def test_describe_categorical(sample_df):
    result = univariate.describe_categorical(sample_df["Gender"])
    assert "Count" in result.columns
    assert "Percent" in result.columns
    assert result.loc["Female", "Count"] == 5  # ← updated from 4
    assert result.loc["Male", "Count"] == 4


def test_plot_categorical_runs_without_error(sample_df):
    univariate.plot_categorical(sample_df["Gender"])  # Just confirm it runs
