import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

RANDOM_STATE = 42

def split_train_test(
    train_df: pd.DataFrame,
    images: np.ndarray
  ) -> list[np.ndarray]:
  labels = train_df["label"].to_numpy()
  return train_test_split(images, labels, test_size=0.1, stratify=labels, random_state=RANDOM_STATE)