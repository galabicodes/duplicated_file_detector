import os
import hashlib
import shutil
folderp = os.path.expanduser("~/Desktop/level")
duplicate_folder = os.path.expanduser("~/Desktop/syf")
hashes = {}
for filename in os.listdir(folderp):
    filep = os.path.join(folderp, filename)
    if not os.path.isfile(filep):
        continue
    with open(filep, "rb") as f:
        fileh = hashlib.md5(f.read()).hexdigest()
    if fileh in hashes:            
        os.makedirs(duplicate_folder, exist_ok=True)
        newp = os.path.join(duplicate_folder, filename)
        shutil.move(filep, newp)
        print(f"moved duplicate file: {filename}")
    else:
        hashes[fileh] = filename
