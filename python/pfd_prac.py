# from pathlib import Path

# Current directory
# print(Path.cwd())

# Build a path
# p = Path("folder") / "subfolder" / "file.txt"
# print(p)  # folder/subfolder/file.txt

with open("text1.txt", "x") as f:
    print(f.write('New file created'))

