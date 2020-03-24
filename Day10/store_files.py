import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_dir = os.path.join(BASE_DIR,"images")

# if not os.path.exists(file_dir):
#     print("This is not a valid path")

os.makedirs(file_dir,exist_ok=True)

my_images = range(0, 12)

for i in my_images:
    fname = f"{i}.txt"
    file_path = os.path.join(file_dir,fname)
    if os.path.exists(file_path):
        print(f"skipped {fname}")
        continue
    with open(file_path,"w")as f:
        f.write("Hello world")