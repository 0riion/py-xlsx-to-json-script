
## XLSX to JSON Converter

This is a Python script that converts an XLSX file with multiple sheets to a single JSON file. The resulting JSON file contains data from all sheets, where each sheet is an object with a name property and a data property that contains an array of dictionaries representing the rows in the sheet.

## Installation

To use this script, you'll need to have Python 3.x installed on your system. You'll also need to install the pandas library, which can be installed using pip or install from the `requirements.txt`:

```bash
pip install -r requirements.txt
```

Replace data.xlsx with the path to your actual XLSX file.

The resulting JSON file will be written to the same directory as the XLSX file, with the same name but a `.json` file extension.

Note: personal script

