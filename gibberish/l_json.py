import json

with open('state.json') as f:
  data = json.load(f)
  
  for state in data['states']:
    del state['area_codes']
    
    
with open('new_data.json', 'w') as f1:
  new_data = json.dump(data, f1, indent=2)
  
# print(data)