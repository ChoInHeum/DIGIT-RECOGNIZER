import torch

from utility import log
from data import load_train_data
from preprocessing import preprocess, to_tensor
from validation import split_train_test

def main() -> None:
  train_df = load_train_data()
  images = preprocess(train_df)

  log(f"pixels_normalized min: {images.min()}")
  log(f"pixels_normalized max: {images.max()}")

  images_train, images_valid, labels_train, labels_valid = split_train_test(train_df, images)
  images_train, images_valid = to_tensor(images_train, dtype=torch.float32), to_tensor(images_valid, dtype=torch.float32)
  labels_train, labels_valid = to_tensor(labels_train, dtype=torch.long), to_tensor(labels_valid, dtype=torch.long)

  log(f"images_train shape: {images_train.shape}")
  log(f"images_valid shape: {images_valid.shape}")
  log(f"labels_train shape: {labels_train.shape}")
  log(f"labels_train shape: {labels_valid.shape}")

  return None

if __name__ == "__main__":
  main()