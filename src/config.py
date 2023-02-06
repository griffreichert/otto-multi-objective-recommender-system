from pathlib import Path

# Define paths to input data
DATA_PATH = Path('../data')

TRAIN_PATH = DATA_PATH / 'train.jsonl'
TEST_PATH = DATA_PATH / 'test.jsonl'

OPT_DATA_PATH = DATA_PATH / 'optimized'
OPT_TRAIN_PATH = OPT_DATA_PATH / 'train.parquet'
OPT_TEST_PATH = OPT_DATA_PATH / 'test.parquet'