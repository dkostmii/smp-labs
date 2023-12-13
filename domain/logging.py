import logging
from os import makedirs
from os.path import exists, join


def init_logging():
    logs_dir = join(".data", "logs")
    logs_file = join(logs_dir, "smp-labs.log")

    if not exists(logs_dir):
        makedirs(logs_dir)

    logging.basicConfig(
        filename=logs_file,
        filemode="w",
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )
