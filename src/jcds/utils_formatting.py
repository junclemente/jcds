from IPython.display import display, HTML


def render_html_block(content_blocks, title=None):
    """
    Display a stylized HTML report block in a Jupyter Notebook.

    Parameters
    ----------
    content_blocks : list of dict
        Each dict should have:
            - label : str
            - value : str or int
            - icon  : str (emoji, optional)
            - label_color : str (CSS color or hex)
            - value_color : str (CSS color or hex)
    title : str, optional
        Title of the block. If provided, displayed at the top.

    Returns
    -------
    None
        Displays HTML directly in the notebook.

    Docstring generated with assistance from ChatGPT.
    """
    rows = ""
    for block in content_blocks:
        icon = block.get("icon", "")
        label = block["label"]
        value = block["value"]
        label_color = block.get("label_color", "#333")
        value_color = block.get("value_color", "#000")

        rows += f"""
        <p>
            <strong style='color: {label_color};'>{icon} {label}:</strong>
            <span style='color: {value_color}; font-weight: 500;'>{value}</span>
        </p>
        """

    html = f"""
    <div style='font-family: "Segoe UI", sans-serif; font-size: 16px; line-height: 1.6;
                border: 1px solid #ddd; border-radius: 8px; padding: 1em; background: #fefefe;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05); margin: 1em 0;'>
        {f"<h3 style='margin-top: 0; color: #2e7d32;'>{title}</h3>" if title else ""}
        {rows}
    </div>
    """
    display(HTML(html))
