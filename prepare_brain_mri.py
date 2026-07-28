import os
import random
import shutil

# ==========================
# Paths
# ==========================
SOURCE_YES = r"C:\Users\deshp\Downloads\archive\brain_tumor_dataset\yes"
SOURCE_NO  = r"C:\Users\deshp\Downloads\archive\brain_tumor_dataset\no"

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
DEST_ROOT  = os.path.join(BASE_DIR, "dataset", "Brain_MRI")

TRAIN_YES  = os.path.join(DEST_ROOT, "train", "yes")
TRAIN_NO   = os.path.join(DEST_ROOT, "train", "no")
TEST_YES   = os.path.join(DEST_ROOT, "test", "yes")
TEST_NO    = os.path.join(DEST_ROOT, "test", "no")

SPLIT_RATIO = 0.8
SEED        = 42

# ==========================
# Helper: split and copy
# ==========================
def split_and_copy(source_dir, train_dir, test_dir):
    files = [
        f for f in os.listdir(source_dir)
        if os.path.isfile(os.path.join(source_dir, f))
    ]

    random.seed(SEED)
    random.shuffle(files)

    split_idx   = int(len(files) * SPLIT_RATIO)
    train_files = files[:split_idx]
    test_files  = files[split_idx:]

    for f in train_files:
        shutil.copy2(os.path.join(source_dir, f), os.path.join(train_dir, f))

    for f in test_files:
        shutil.copy2(os.path.join(source_dir, f), os.path.join(test_dir, f))

    return len(train_files), len(test_files)


# ==========================
# Run
# ==========================
print("Preparing Brain MRI dataset...\n")

train_yes, test_yes = split_and_copy(SOURCE_YES, TRAIN_YES, TEST_YES)
train_no,  test_no  = split_and_copy(SOURCE_NO,  TRAIN_NO,  TEST_NO)

# ==========================
# Summary
# ==========================
print("=" * 30)
print("   Brain MRI Dataset Summary")
print("=" * 30)
print(f"  Train")
print(f"    YES : {train_yes}")
print(f"    NO  : {train_no}")
print(f"  Test")
print(f"    YES : {test_yes}")
print(f"    NO  : {test_no}")
print("=" * 30)
print(f"  Total Train : {train_yes + train_no}")
print(f"  Total Test  : {test_yes  + test_no}")
print(f"  Grand Total : {train_yes + train_no + test_yes + test_no}")
print("=" * 30)
print("\n✅ Brain MRI dataset prepared successfully.")
print(f"   Location: {DEST_ROOT}")
