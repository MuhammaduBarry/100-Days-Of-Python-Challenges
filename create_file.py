import os


for number in range(4,101):
    directory_path = f"./test_problems/test_day_{number:02d}_solutions.py"
    os.rename(directory_path, f"./test_problems/test_day_{number:03d}_solutions.py")