# Introduction

This repository contains a simple web application consisting of a server script (`server.py`), a Chrome extension with background script (`background.js`), a manifest file (`manifest.json`), and a popup script (`popup.js`). The application's primary functionality revolves around checking URLs against a database and updating the user via a Chrome extension popup.

## Installation

### Clone the Repository

Clone this repository to your local machine using `git clone <repository-url>`.

### Setting Up the Server

- Navigate to the directory containing `server.py`.
- Run `python server.py` to start the server.
- Ensure the server is running properly.

### Installing the Chrome Extension

- Open Google Chrome.
- Go to `chrome://extensions/`.
- Enable "Developer mode" at the top right.
- Click "Load unpacked" and select the folder containing the `manifest.json` file.
- The extension should now appear in your Chrome extensions list.

## Usage

### Using the Server

- The server script (`server.py`) should be running in the background.
- Run the following command to run the file: `python server.py`.
- It interacts with the Chrome extension to check URLs against a database.

### Using the Chrome Extension

- Navigate to any website in Chrome.
- The popup will display if the url is found in the database. Else nothing will be shown.

## Troubleshooting

- If the extension does not appear, ensure you have selected the correct folder and that "Developer mode" is enabled.
- If the popup does not show the expected result, verify that `server.py` is running and there are no errors in the console.

## Contributing

Contributions are welcome. If you have suggestions or want to add features, feel free to create a pull request or open an issue.
