# URL Analyzer

URL Analyzer is a Python script designed to assess the risk associated with a given URL by analyzing server insights and capturing snapshots of its homepage. It provides server IP and location information along with screenshots, allowing users to evaluate potential threats before visiting the URL.

## Why Use URL Analyzer?

With the increasing number of malicious websites and phishing attempts, it's essential to have a tool that can help users identify potential risks associated with URLs before visiting them. URL Analyzer aims to fill this gap by providing insights into the server details and capturing home page snapshots, allowing users to make informed decisions about visiting the URL.

## Installation

URL Analyzer requires Python 3.12 or higher.

You can install the requirements using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use URL Analyzer, follow these steps:

-   Clone or download the project repository.

-   Install the dependencies using the provided requirements.txt file.

-   Run the script with the desired URL as the argument:

```bash
python analyse.py --url example.com
```

The script will display the server IP and location information, as well as save screenshots of the homepage and full-length homepage in the project directory.
