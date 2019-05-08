import csv, os, json

# JSON Tuto

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)   # formating changes a litle bit, it converts jason data to pyton data


pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)  # it converts python data to jason data
