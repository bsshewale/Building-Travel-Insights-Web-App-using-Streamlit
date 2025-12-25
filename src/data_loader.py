import pandas as pd
import random
from .config import DATA_PATH, RANDOM_SEED, SAMPLE_SIZE

def load_data():
    random.seed(RANDOM_SEED)

    df = pd.read_csv(
        DATA_PATH,
        on_bad_lines='skip',
        skiprows=lambda i: i > 0 and random.random() > (SAMPLE_SIZE / 100000)
    )
    return df
