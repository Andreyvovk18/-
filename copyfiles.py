import os
import shutil


SRC = "D:\\test\\Test1"
DST = "D:\\test\\Test2"

FILE_NAMES = os.listdir(SRC)

for filename in FILE_NAMES:
    source_file_path = SRC + "\\" + filename
    path_to_destination_file = DST + "\\" + filename
    shutil.copyfile(source_file_path, path_to_destination_file)
