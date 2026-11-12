from pathlib import Path

# directory
ROOT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_PATH / "data"

# file
TEST_PATH = DATA_PATH / "test.csv"
TRAIN_PATH = DATA_PATH / "train.csv"
SAMPLE_SUBMISSION_PATH = DATA_PATH / "sample_submission.csv"

