# Configuration README

Configuration files are listed in the next table:

| Lab   | Config file                                                          |
| ----- | -------------------------------------------------------------------- |
| Lab 1 | [`.calcrc.json.example`](./.calcrc.json.example) (remove `.example`) |
| Lab 2 | [`.calcrc.json.example`](./.calcrc.json.example) (remove `.example`) |
| Lab 3 | [`lab3.json`](./lab3.json)                                           |
| Lab 4 | [`lab4.json`](./lab4.json)                                           |
| Lab 5 | No config file                                                       |
| Lab 6 | No config file                                                       |
| Lab 7 | [`.apirc.json.example`](./.apirc.json.example) (remove `.example`)   |
| Lab 8 | No config file                                                       |

In Labs 1 and 2, the configuration file is created automatically,
when no such exist.

For Lab 3, the list of valid fonts can be obtained via `pyfiglet --list_fonts`,
assuming you are in pipenv shell already.

For Lab 7, obtain API key at
[RapidAPI](https://rapidapi.com/neotank/api/instagram130/)
and replace `TO_BE_MODIFIED` value with it.
