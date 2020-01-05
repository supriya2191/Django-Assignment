import json

with open("B:\employee.json") as json_data:
    data = json.load(json_data)

    for item in data['Employees']:
        print(item)