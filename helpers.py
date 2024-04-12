import argparse


def parse_cli() -> argparse.Namespace:
    # Parse command line arguments for script
    parser = argparse.ArgumentParser()

    ### - Global Params - ###
    parser.add_argument(
        "-freq",
        "--freq",
        dest="freq",
        metavar="freq",
        default="1D",
        type=str,
        help="Override frequency string",
    )

    parser.add_argument(
        "-verbose",
        "--verbose",
        dest="verbose",
        metavar="verbose",
        default=True,
        type=bool,
        help="Toggle logging",
    )

    parser.add_argument(
        "-pred",
        "--pred",
        dest="pred",
        metavar="pred",
        default=7,
        type=int,
        help="Override prediction length",
    )

    parser.add_argument(
        "-con",
        "--context",
        dest="context",
        metavar="context",
        default=30,
        type=int,
        help="Override context length",
    )

    parser.add_argument(
        "-batch",
        "--batch",
        dest="batch",
        metavar="batch",
        default=20,
        type=int,
        help="Override context length",
    )

    parser.add_argument(
        "-test",
        "--test",
        dest="test",
        metavar="test",
        default=True,
        type=bool,
        help="Toggle testing inference",
    )

    args = parser.parse_args()
    return args
