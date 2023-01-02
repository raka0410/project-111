import os
import shutil

source="C:/Users/rakar/Downloads"
destination="C:/Users/rakar/Desktop"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    dest=os.path.splitext(i)
    print(dest)