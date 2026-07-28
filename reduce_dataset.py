import os
import shutil
import random

random.seed(42)

SOURCE = r"C:\Users\deshp\Downloads\archive\chest_xray"
DEST = "dataset"

TRAIN_COUNT = 500
TEST_COUNT = 100


def copy_images(src_folder, dst_folder, count):
    os.makedirs(dst_folder, exist_ok=True)

    images = [f for f in os.listdir(src_folder)
              if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    random.shuffle(images)

    images = images[:count]

    for img in images:
        shutil.copy(
            os.path.join(src_folder, img),
            os.path.join(dst_folder, img)
        )

    print(f"Copied {len(images)} images -> {dst_folder}")


# Delete old dataset
if os.path.exists(DEST):
    shutil.rmtree(DEST)

# TRAIN
copy_images(
    os.path.join(SOURCE, "train", "NORMAL"),
    os.path.join(DEST, "train", "NORMAL"),
    TRAIN_COUNT
)

copy_images(
    os.path.join(SOURCE, "train", "PNEUMONIA"),
    os.path.join(DEST, "train", "PNEUMONIA"),
    TRAIN_COUNT
)

# TEST
copy_images(
    os.path.join(SOURCE, "test", "NORMAL"),
    os.path.join(DEST, "test", "NORMAL"),
    TEST_COUNT
)

copy_images(
    os.path.join(SOURCE, "test", "PNEUMONIA"),
    os.path.join(DEST, "test", "PNEUMONIA"),
    TEST_COUNT
)

print("\nDataset created successfully!")