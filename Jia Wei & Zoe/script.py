import os, json
import shutil

path_to_json = './'
path_to_output='./images/'
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  with open(path_to_json + file_name) as json_file:
    data = json.load(json_file)
    if(data['node']['edge_media_preview_like']['count'] >= 200):
      data2 = data['node']
      if  ('edge_sidecar_to_children' in data2):
        print (len(data2['edge_sidecar_to_children']['edges']))
        for x in range(1,(len(data2['edge_sidecar_to_children']['edges']))+1):
          image_file_name = os.path.splitext(file_name)[0]+'_'+str(x)+'.jpg'
          print(os.path.splitext(file_name)[0]+'_'+str(x)+'.jpg' )
          shutil.copyfile(image_file_name, path_to_output+image_file_name)
      else:
        image_file_name = os.path.splitext(file_name)[0]+'.jpg'
        print(os.path.splitext(file_name)[0]+'.jpg' )
        shutil.copyfile(image_file_name, path_to_output+image_file_name)