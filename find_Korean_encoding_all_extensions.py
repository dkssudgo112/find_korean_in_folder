from distutils import extension
from itertools import count
import os
import codecs
import json
#import pprint

extensions = []
dict_extensions = {}

print("------------------------------Start : check encoding Korean seq-------------------------------------")
for base_path, dir_names, file_names in os.walk("."):
    for file_name in file_names:
        file_path = os.path.join(base_path, file_name)   

        loc = file_name.rfind('.')
        extensions.append(file_name[loc+1:])
        #extensions = list(dict.fromkeys(extensions))

        file_data = open(file_path, "rb").read()
        if file_data.startswith(codecs.BOM_UTF8):
            print(f"utf8_bom_file: {file_path}")
            continue

        try:
            file_data.decode('cp949')
        except UnicodeDecodeError as exc:
            try:
                file_data.decode('utf8')
                print(f"utf8_file: {file_path}")
            except UnicodeDecodeError as exc:
                print(f"unknown_file: {file_path}")

            continue
            
        
        if any(file_byte for file_byte in file_data if file_byte > 127):
            print(f"NOT_PURE_ASCII_FILE: {file_path}") # pure ascii file
print("------------------------------End : check encoding Korean seq-------------------------------------")




print("------------------------------Start : check all extensions seq-------------------------------------")
for i in extensions:
    try: dict_extensions[i] += 1
    except: dict_extensions[i] = 1

dict_extensions = dict(sorted(dict_extensions.items(), key = lambda item: item[1], reverse = True))

json_val = json.dumps(dict_extensions,ensure_ascii=False ,indent=1)

print(json_val)
#print(json_val)
#print(dict_extensions)
#print(extensions)
print("------------------------------End : check all extensions seq-------------------------------------")