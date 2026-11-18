import os
import subprocess

# Ask for the file you want to turn into an exe
file_path = input("Enter the name of your code file (e.g., game.py or app.cpp): ")

# Split the filename to see its extension
name, extension = os.path.splitext(file_path)

if extension == ".py":
    print("Building Python executable...")
    subprocess.run(["pyinstaller", "--onefile", file_path])

elif extension == ".cpp":
    print("Compiling C++ executable...")
    subprocess.run(["g++", file_path, "-o", f"{name}.exe"])

else:
    print(f"Sorry, I don't have a tool set up for {extension} files yet!")
