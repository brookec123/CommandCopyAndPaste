import os
import subprocess
from pyautogui import typewrite

def parse_commands_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return[line.strip() for line in file]

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")

def execute_commands_from_list(commands):
    for c in commands:
        print("Please edit and press enter to run the command: ", end="")
        typewrite(c)
        response = input()
        try:
            if response.startswith("cd"):
                new_directory = response.split(" ")[-1]
                subprocess.run(response, shell=True, check=True)
                os.chdir(new_directory)
            else:
                subprocess.run(response, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

if __name__ == "__main__":
    cmds = parse_commands_from_file("output.txt")
    execute_commands_from_list(cmds)
