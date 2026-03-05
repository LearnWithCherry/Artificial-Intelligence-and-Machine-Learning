# JSON - JavaScript object notation 
#                  |
#              (format)
# JSON modules - 
# json.loads()
# json.dumps() - for string
# json.load()
# json.dump() - for file

import json 

json_str = '{"name" : "Rajat", "IsStudent" : "true"}'

python_obj = json.loads(json_str)

# print(type(python_obj), python_obj)


py_obj = {
    "name" : "Rajat",
    "age" : 19,
    "Student" : True
}

json_obj = json.dumps(py_obj)

# print(type(json_obj), json_obj)


# with open("X:\\VScode\\PYTHON\\06_Prime_Batch\\33_data.json", 'r') as file:
#     python_object = json.load(file)
#     # print(python_object)


with open("X:\\VScode\\PYTHON\\06_Prime_Batch\\33_data.json", 'w') as file:
    json.dump(py_obj, file, indent=4, sort_keys=4)