import os, json
from pickle import TRUE
import shutil
import csv

path_to_json = './'
flags = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        data = json.load(json_file)
        flag = 0
        for x in data:
            if(x['Name'] == "Human" or x['Name']=="Person"):
                flag = 1
        flags.append(flag)
with open('flags.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(flags)