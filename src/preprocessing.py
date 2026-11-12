import numpy as np
import pandas as pd
import torch

from utility import log, get_device

def normalize_pixels(pixels: np.ndarray) -> np.ndarray:
  pixels_normalized = np.astype(pixels, np.float32) / 255
  return pixels_normalized

def to_tensor(ndarray: np.ndarray, dtype: torch.dtype) -> torch.Tensor:
  return torch.tensor(ndarray, dtype=dtype, device=get_device())

def preprocess(train_df: pd.DataFrame) -> np.ndarray:
  pixels = train_df.iloc[:, 1:].to_numpy()
  pixels_normalized = normalize_pixels(pixels)

  images = pixels_normalized.reshape(-1, 1, 28, 28)
  log(f"image layer shape: {images.shape}")
  return images