import os
import subprocess

file_path = input("Enter the name of your code file (e.g., game.py or app.cpp): ")

name, extension = os.path.splitext(file_path)

if extension.lower == ".py":
    print("Building Python executable...")
    subprocess.run(["pyinstaller", "--onefile", file_path])

elif extension.lower == ".cpp":
    print("Compiling C++ executable...")
    subprocess.run(["g++", file_path, "-o", f"{name}.exe"])

else:
    print(f"Sorry, I don't have a tool set up for {extension} files yet!")
