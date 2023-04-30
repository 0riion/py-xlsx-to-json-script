import pandas as pd
import json

# Load the Excel file
xlsx_file = pd.read_excel('data.xlsx', sheet_name=None)

# Convert each sheet to a dictionary with 'name' and 'data' keys
sheet_data = [{'name': name, 'data': sheet.to_dict(orient='records')} for name, sheet in xlsx_file.items()]

# Convert the sheet data to a JSON string
json_str = json.dumps(sheet_data)

# Write the JSON string to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_str)

