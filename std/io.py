import csv
import json

import pandas


def write_into_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as file:
        file.write(text)


def read_from_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def read_from_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)


def write_into_json(file_path: str, jsons: dict) -> None:
    jsons_text_representation = json.dumps(jsons, indent=4)
    json.loads(jsons_text_representation)

    with open(file_path, "w") as file:
        file.write(jsons_text_representation)


def write_into_csv(file_path: str, data: dict) -> None:
    fieldnames = data.keys()
    filtered_fieldnames = [
        field
        for field in fieldnames
        if not (isinstance(field, dict) or isinstance(field, list))
    ]

    values = data.values()

    with open(file_path, "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=filtered_fieldnames)
        csv_writer.writeheader()
        csv_writer.writerow(dict(zip(fieldnames, values)))


def read_csv_df(file_path: str) -> pandas.DataFrame:
    return pandas.read_csv(file_path)
