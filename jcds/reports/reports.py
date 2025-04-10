from IPython.display import display, HTML
from jcds.eda import show_shape, show_dupes

# from jcds.utils.formatting import render_html_block


def data_quality(dataframe):
    shape = show_shape(dataframe)
    dupes = show_dupes(dataframe)

    print(f"There are {shape[0]} rows and {shape[1]} columns.")
    print(f"There are {dupes} duplicated rows.")
    # html = f"""
    # <div style='font-family: "Segoe UI", sans-serif; font-size: 16px; line-height: 1.6;'>
    #     <p><strong style='color: #6a1b9a;'>🧮 Shape:</strong>
    #     <span style='color: #0277bd;'>{shape[0]}</span> rows and
    #     <span style='color: #0277bd;'>{shape[1]}</span> columns.</p>

    #     <p><strong style='color: #d32f2f;'>🔁 Duplicates:</strong>
    #     <span style='color: #f57c00;'>{dupes}</span> duplicated rows.</p>
    # </div>
    # """
    # display(HTML(html))
    # render_html_block(
    #     title="📊 Data Quality Summary",
    #     content_blocks=[
    #         {
    #             "label": "Rows",
    #             "value": shape[0],
    #             "icon": "📏",
    #             "label_color": "#6a1b9a",
    #             "value_color": "#0277bd",
    #         },
    #         {
    #             "label": "Columns",
    #             "value": shape[1],
    #             "icon": "📐",
    #             "label_color": "#6a1b9a",
    #             "value_color": "#0277bd",
    #         },
    #         {
    #             "label": "Duplicated Rows",
    #             "value": dupes,
    #             "icon": "🔁",
    #             "label_color": "#d32f2f",
    #             "value_color": "#f57c00",
    #         },
    #     ],
    # )
