import torch as T
import argparse
import logging
from functools import partial
import numpy as np

from helpers import parse_cli
from utils.data_helpers import load_data, transform_start_field


def main(args: argparse.Namespace):
    """
    Begin setup and context before the training / testing loops are done
    """
    if args.verbose:
        # set up logger
        logger = logging.getLogger()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    # load data from disk
    data = load_data()
    train = data["train"]
    test = data["test"]

    train.set_transform(partial(transform_start_field, freq=args.freq))
    test.set_transform(partial(transform_start_field, freq=args.freq))


if __name__ == "__main__":
    args = parse_cli()
    main(args)
