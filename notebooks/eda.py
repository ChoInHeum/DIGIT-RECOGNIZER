# %% initialize
import sys
from pathlib import Path
from IPython.display import display

ROOT_PATH = Path(__file__).parent

while not (ROOT_PATH / "src").is_dir():
  ROOT_PATH = ROOT_PATH.parent

sys.path.insert(0, str(ROOT_PATH / "src"))

# %% import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data import *
# %%
train_df = pd.read_csv(TRAIN_PATH, dtype=np.uint8)
rows = train_df.iloc[0:10, 0:].to_numpy()

figure, axes = plt.subplots(nrows=2, ncols=5, figsize=(15, 6))
axes = axes.flatten(order="C")

for ax, row in zip(axes, rows):
  image = row[1:].reshape(28, 28)
  ax.imshow(image, cmap="gray")
  ax.set_title(f"label: {row[0]}")

plt.show()

display(train_df.iloc[:, 0].value_counts().sort_index())