
from utility import log
from data import load_train_data
from preprocessing import preprocess, to_tensor
from validation import split_train_test

def main() -> None:
  train_df = load_train_data()
  images = preprocess(train_df)

  log(f"pixels_normalized min: {images.min()}")
  log(f"pixels_normalized max: {images.max()}")

  images_train, images_valid, labels_train, labels_valid = [to_tensor(ndarray) for ndarray in split_train_test(train_df, images)]

  log(f"images_train shape: {images_train.shape}")
  log(f"images_valid shape: {images_valid.shape}")
  log(f"labels_train shape: {labels_train.shape}")
  log(f"labels_train shape: {labels_valid.shape}")

  return None

if __name__ == "__main__":
  main()