import numpy as np
import pandas as pd

from pathlib import Path

# directory
ROOT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_PATH / "data"

# file
TEST_PATH = DATA_PATH / "test.csv"
TRAIN_PATH = DATA_PATH / "train.csv"
SAMPLE_SUBMISSION_PATH = DATA_PATH / "sample_submission.csv"

def load_train_data() -> pd.DataFrame:
  return pd.read_csv(TRAIN_PATH, dtype=np.uint8)