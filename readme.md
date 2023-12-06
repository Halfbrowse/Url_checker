# Introduction

This repository contains a simple web application consisting of a server script (`server.py`), a Chrome extension with background script (`background.js`), a manifest file (`manifest.json`), and a popup script (`popup.js`). The server script runs in the background and interacts with the Chrome extension to check URLs against a database. The Chrome extension is used to display a popup window with the results of the check.

There is also an admin panel (`app.py`) which allows you to upload a csv file containing URLs to check, as well as create new entries.

## Installation

### Clone the Repository

Clone this repository to your local machine using `git clone https://github.com/Halfbrowse/Url_checker.git`.

### Environment Setup

CD into the repo and run `python -m venv venv` on windows or `python3 -m venv venv` on linux.

Run `source venv/bin/activate` to activate the virtual environment on linux.

Run `venv\Scripts\activate` on windows.

Run `pip install -r requirements.txt` to install the required packages.

### Setting Up the Database

Run `python initialise_db.py` to create the database.

### Admin Panel

Run `streamlit run app.py` to start the admin panel.

The database will be empty so you will need to use the form to populate the database.

If you have a csv file to upload just click/drag & drop onto the file uploader at the bottom of the page.

### Setting Up the Server

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

### Using the Chrome Extension

- Navigate to a website in your database.
- The popup will display if the url is found in the database. Else nothing will be shown.

## Troubleshooting

- If the extension does not appear, ensure you have selected the correct folder and that "Developer mode" is enabled.
- If the popup does not show the expected result, verify that `server.py` is running and there are no errors in the console.

## Contributing

Contributions are welcome. If you have suggestions or want to add features, feel free to create a pull request or open an issue.
