import os,json
import math

path_to_json = './'
likes = []
counter = 0
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        data = json.load(json_file)
        print(file_name)
        likes.append(int(data['node']['edge_media_preview_like']['count']))
        counter+=1
if(counter%2 == 0):
    upper = math.ceil(counter/2)
    lower = math.floor(counter/2)
    med = (likes[int(upper)]+likes[int(lower)])/2
    print("Median is : "+str(med))
else:
    med = likes[counter/2]
    print("Median is : "+str(med))


