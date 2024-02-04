from collections import Counter

from matplotlib import pyplot as plt

from std.io import read_csv_df
from std.read import (read_choose_from_list, read_filename, read_single_int,
                      read_until_pred, read_until_pred_custom, read_yes_no)

valid_colors = ["red", "green", "blue", "magenta", "cyan", "yellow"]


def main():
    df = read_csv_df(
        file_path=read_filename(
            "Enter a dataset file path: ", check_readable=True, check_writable=False
        )
    )

    col = read_until_pred(
        pred=lambda col: df.columns.isin([col]).any(),
        title="Enter a column to count from: ",
        invalid_msg="Invalid column",
    )

    df = df[col]
    sample = Counter(df)
    sample_items = sample.items()
    sample_items_len = len(sample_items)

    max_quantity = read_until_pred_custom(
        custom_src=read_single_int,
        pred=lambda n: n > 0 and n <= sample_items_len,
        title=f"How many {col} bars should be included in diagram?: ",
        invalid_msg=f"There must be at least 1 and at most {sample_items_len} bars",
    )

    bar_color = read_choose_from_list(
        options=["default"] + valid_colors,
        title="Pick a color for bar chart",
    )

    if bar_color == "default":
        bar_color = None

    sorted_dict_values = dict(
        sorted(sample_items, key=lambda item: item[1], reverse=True)[:max_quantity]
    )

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(30, 15))

    ax0.bar(
        [key for key in sorted_dict_values],
        [sorted_dict_values[key] for key in sorted_dict_values],
        color=bar_color,
    )
    ax0.set_title(f"{col} bar chart")
    ax0.set_xlabel(col)
    ax0.set_ylabel("Frequency")
    ax0.tick_params(axis="x", rotation=45)
    fig.suptitle(f"Top {max_quantity} {col} charts", fontsize=14)

    labels = list(sorted_dict_values.keys())
    sizes = list(sorted_dict_values.values())
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax1.set_title(f"{col} pie chart")

    save_diagram = read_yes_no("Do you want to save diagram?", default=False)

    if save_diagram:
        filename = read_filename(
            "Enter image file name, where diagram should be saved: ",
            check_readable=False,
            check_writable=True,
        )
        plt.savefig(filename)

    plt.show()


if __name__ == "__main__":
    main()
