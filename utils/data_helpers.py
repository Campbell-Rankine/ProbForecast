import pandas as pd
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from functools import lru_cache
from datasets import load_from_disk


@lru_cache(10_000)
def convert_date_to_period(date, freq):
    return pd.Period(date, freq)


def transform_start_field(batch, freq):
    batch["start"] = [convert_date_to_period(date[0], freq) for date in batch["start"]]
    return batch


def load_data(path="./data"):
    # load and return dataset from the path above
    try:
        return load_from_disk("./data")
    except Exception as e:
        raise ValueError(f"Unable to load dataset from disk: {e}")
