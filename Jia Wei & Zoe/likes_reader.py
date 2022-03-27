import os, json
from pickle import TRUE
import shutil
import csv
path_to_json = './'
likes = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        data = json.load(json_file)
        if(data['node']['edge_media_preview_like']['count'] >= 16242):
            data2 = data['node']
            if  ('edge_sidecar_to_children' in data2):
                print (len(data2['edge_sidecar_to_children']['edges']))
                for x in range(1,(len(data2['edge_sidecar_to_children']['edges']))+1):
                    print(data2['edge_media_preview_like']['count'])
                    likes.append(data2['edge_media_preview_like']['count'])
            else:
                likes.append(data2['edge_media_preview_like']['count'])

with open('likes.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(likes)