import json, os
from collections import Counter

root = r'C:\Users\wonde\gh\exercises-dataset\fitness-site'
data_path = os.path.join(root, 'data', 'exercises.json')

with open(data_path, encoding='utf-8') as f:
    data = json.load(f)

# Show final category distribution
cats = Counter(ex['category'] for ex in data)
print('Final category distribution:')
for cat, count in cats.most_common():
    print(f'  {cat}: {count}')

# Check remaining conflicts
category_rules = {
    'upper arms': ['bicep', 'tricep', 'curl', 'extension', 'arm', 'concentration'],
    'lower arms': ['wrist', 'forearm', 'grip'],
    'chest': ['bench', 'press', 'fly', 'push-up', 'pushup', 'dip', 'chest'],
    'back': ['pull-up', 'pull up', 'row', 'deadlift', 'lat', 'back', 'shrug', 'hyper'],
    'waist': ['crunch', 'sit-up', 'plank', 'abdominal', 'twist', 'side bend', 'windmill', 'figure 8'],
    'shoulders': ['lateral raise', 'front raise', 'overhead', 'military press', 'arnold', 'clean and jerk', 'press'],
    'upper legs': ['squat', 'lunge', 'leg curl', 'leg extension', 'leg press', 'glute', 'hamstring', 'step up'],
    'lower legs': ['calf', 'ankle'],
    'cardio': ['running', 'jumping', 'cardio', 'aerobic', 'bike', 'elliptical'],
    'neck': ['neck']
}

remaining_conflicts = []
for ex in data:
    name = ex['name'].lower()
    cat = ex['category']
    
    # If the current category's keywords are present -> OK
    if any(kw in name for kw in category_rules.get(cat, [])):
        continue
    
    # Check if another category has keywords that match better
    for other_cat, keywords in category_rules.items():
        if other_cat != cat and any(kw in name for kw in keywords):
            remaining_conflicts.append(ex)
            break

print(f'\nRemaining name-category conflicts after fix: {len(remaining_conflicts)}')
if remaining_conflicts:
    print('\nExamples (first 15):')
    for ex in remaining_conflicts[:15]:
        print(f"  {ex['id']} | {ex['name']} | cat={ex['category']} | eq={ex['equipment']}")

# Count by equipment now
eq_cats = {}
for ex in data:
    key = f"{ex['equipment']}|{ex['category']}"
    eq_cats[key] = eq_cats.get(key, 0) + 1

print('\nTop Equipment+Category combinations:')
for key, count in sorted(eq_cats.items(), key=lambda x: -x[1])[:20]:
    print(f'  {key}: {count}')
