import json

import colorama
import pyfiglet
from colorama import Fore
from prettytable import PrettyTable

colorama.init(autoreset=True)

fonts = dict(enumerate(sorted(pyfiglet.FigletFont.getFonts())))
colors = dict(enumerate(sorted(Fore.__dict__.keys())))


def convert_to_table(json_data: str) -> str:
    data = json.loads(json_data)
    outer_table = PrettyTable()
    outer_table.field_names = ["Attribute", "Value"]
    for key, value in data.items():
        if key in {
            "id",
            "biography",
            "full_name",
            "is_business_account",
            "category_name",
            "is_private",
            "username",
        }:
            outer_table.add_row([f"{Fore.GREEN + key + Fore.RESET}", value])

    return outer_table.get_string()
