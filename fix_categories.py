import json, re

with open(r"C:\Users\wonde\gh\exercises-dataset\fitness-site\data\exercises.json", encoding="utf-8") as f:
    data = json.load(f)

category_rules = {
    "upper arms": ["bicep", "tricep", "curl", "extension", "arm", "concentration"],
    "lower arms": ["wrist", "forearm", "grip"],
    "chest": ["bench", "press", "fly", "push-up", "pushup", "dip", "chest"],
    "back": ["pull-up", "pull up", "row", "deadlift", "lat", "back", "shrug", "hyper"],
    "waist": ["crunch", "sit-up", "plank", "abdominal", "twist", "side bend", "windmill", "figure 8"],
    "shoulders": ["lateral raise", "front raise", "overhead", "military press", "arnold", "clean and jerk", "press"],
    "upper legs": ["squat", "lunge", "leg curl", "leg extension", "leg press", "glute", "hamstring", "step up"],
    "lower legs": ["calf", "ankle"],
    "cardio": ["running", "jumping", "cardio", "aerobic", "bike", "elliptical"],
    "neck": ["neck"]
}

def find_category(name):
    name_lower = name.lower()
    for cat, keywords in category_rules.items():
        if any(kw in name_lower for kw in keywords):
            return cat
    return None

fixed = 0
errors = []
for ex in data:
    name = ex["name"]
    current_cat = ex["category"]
    suggested_cat = find_category(name)
    
    if suggested_cat and suggested_cat != current_cat:
        fixed += 1
        ex["category"] = suggested_cat
        errors.append({
            "id": ex["id"],
            "name": name,
            "old_category": current_cat,
            "new_category": suggested_cat,
            "equipment": ex["equipment"]
        })

with open(r"C:\Users\wonde\gh\exercises-dataset\fitness-site\data\exercises.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Fixed {fixed} category mismatches")
print("\nFirst 15 fixes:")
for err in errors[:15]:
    print(f"ID {err['id']} | {err['name']}: {err['old_category']} -> {err['new_category']}")
