import os
import sys
import subprocess
from pyautogui import typewrite
import time


def open_cmd_window(file_path):
    try:
        # Get the directory name without the filename
        folder_path = os.path.dirname(file_path)

        # Open the command window in the specified folder
        platform = sys.platform
        if platform == "win32":
            cmd_command = f'start cmd /K cd /D "{folder_path}"'
        else:
            raise NotImplementedError("Opening command window on non-Windows platforms is not implemented.")

        # Capture the output of the command
        process = subprocess.Popen(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, _ = process.communicate()

        # Print the output to the VSCode terminal
        print(output)
        

    except Exception as e:
        print(f"Error: {e}")
    
def save_commands():
    
    pass

def find_command_file_in_current_directory(current_dir: str) -> str:
    pass

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
    print("fedwfwe", file=sys.stderr)
    time.sleep(1)
    lst = parse_commands_from_file(sys.argv[1])
    print(lst)
    execute_commands_from_list(lst)