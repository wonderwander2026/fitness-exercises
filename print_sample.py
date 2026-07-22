import json, sys

with open('data/exercises.json', encoding='utf-8') as f:
    data = json.load(f)

sys.stdout.write(json.dumps(data[0], ensure_ascii=False, indent=2))
sys.stdout.write('\n---\n')
sys.stdout.write(json.dumps(data[1], ensure_ascii=False, indent=2))
