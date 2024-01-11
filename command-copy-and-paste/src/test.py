import pyautogui
import pytesseract
from PIL import Image
import pygetwindow as gw

def get_active_terminal_title():
    try:
        active_window = gw.getActiveWindow()
        if active_window is not None:
            return active_window.title
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def read_and_save_terminal_output_to_file(file_path):
    try:
        # Get the title of the active terminal window
        terminal_title = get_active_terminal_title()

        if terminal_title:
            # Get the position and size of the terminal window
            terminal_window = gw.getWindowsWithTitle(terminal_title)[0]
            left, top, width, height = terminal_window.left, terminal_window.top, terminal_window.width, terminal_window.height

            # Take a screenshot of the terminal window
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save("terminal_screenshot.png")

            # Use pytesseract to perform OCR on the screenshot
            text = pytesseract.image_to_string(Image.open("terminal_screenshot.png"))

            # Save the text to a .txt file
            with open(file_path, 'w') as output_file:
                output_file.write(text)

            print(f"Text saved to {file_path}")

        else:
            print("No active terminal window found.")

    except Exception as e:
        print(f"Error: {e}")

# Example: Save text from the active terminal window to a file
output_file_path = 'output.txt'
read_and_save_terminal_output_to_file(output_file_path)
