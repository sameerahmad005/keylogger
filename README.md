# KeyLogger

A simple keylogger implemented in Python for educational purposes. This keylogger logs keystrokes in real-time and saves them to a file. The logging process stops and saves the file when the `Esc` key is pressed.

> **Disclaimer:** This keylogger is for educational purposes only. Ensure you have explicit permission to use such software and comply with all relevant laws and regulations. Unauthorized use of keyloggers is illegal and unethical.

## Features

- **Real-time Logging:** Captures and logs keystrokes as they are pressed.
- **File Saving:** Logs are saved to a file with a timestamp.
- **Stop Logging:** Stops logging and saves the file when `Esc` is pressed.

## Installation

1. **Clone the Repository:**

```markdown
   git clone https://github.com/sameerahmad005/keylogger.git
   cd keylogger
   ```

2. **Install Dependencies:**

   Ensure you have Python installed. Then, install the required dependencies:

   ```bash
   pip install pynput
   ```

## Usage

1. **Run the Keylogger:**

   ```bash
   python KeyLogger.py
   ```

2. **Stop Logging:**

   - Press `Esc` to stop logging and save the log file.
3. **Log File:**

   The log file will be saved with a name like `keylog_YYYYMMDD_HHMMSS.txt` in the same directory as the script.

## Code Explanation

- **KeyLogger Class:** Handles the initialization of the logger and processes key events.
- **Real-time Logging:** Logs each keystroke to the file as it is pressed.
- **Stopping Conditions:** Stops logging when `Esc` or `Ctrl+Q` is pressed.

## Ethical Considerations

- **Permission:** Obtain explicit permission from the device owner before using or deploying this keylogger.
- **Transparency:** Clearly inform users about the keylogger's purpose and how their data will be used.
- **Compliance:** Adhere to all relevant laws and regulations regarding the use of keyloggers.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **pynput Library:** Used for handling keyboard events.

## Contact

For any questions or feedback, please open an issue on the [GitHub repository](https://github.com/sameerahmad005/keylogger/issues).
```
