import os
import shutil

# ==========================
# Paths
# ==========================
SRC_BASE  = r"C:\Users\deshp\Downloads\archive (1)"
DEST_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset", "Skin_Disease")

FOLDERS = [
    ("train", "benign"),
    ("train", "malignant"),
    ("test",  "benign"),
    ("test",  "malignant"),
]

# ==========================
# Copy
# ==========================
for split, cls in FOLDERS:
    src  = os.path.join(SRC_BASE,  split, cls)
    dest = os.path.join(DEST_BASE, split, cls)
    os.makedirs(dest, exist_ok=True)

    files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f))]
    already = set(os.listdir(dest))
    to_copy = [f for f in files if f not in already]

    print(f"Copying {split}/{cls}: {len(to_copy)} new files ({len(already)} already exist)...")
    for f in to_copy:
        shutil.copy2(os.path.join(src, f), os.path.join(dest, f))

# ==========================
# Summary
# ==========================
print("\n" + "=" * 35)
print("   Skin Disease Dataset Summary")
print("=" * 35)
for split, cls in FOLDERS:
    count = len([f for f in os.listdir(os.path.join(DEST_BASE, split, cls))
                 if os.path.isfile(os.path.join(DEST_BASE, split, cls, f))])
    print(f"  {split:5s} / {cls:10s} : {count}")
print("=" * 35)
print("\n✅ Skin Disease dataset copy complete.")
print(f"   Location: {DEST_BASE}")
