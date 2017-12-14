import json

with open('category_dict.json', 'r') as f:
    cats = json.load(f)
    print(json.dumps(cats, indent=2))
