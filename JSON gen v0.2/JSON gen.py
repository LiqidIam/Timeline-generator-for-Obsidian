import json

def generate_timeline(start_year=1810, end_year=2100, step=10, width_per_year=25):
	pass
	return json.dumps(canvas, indent=2, ensure_ascii=False)

# Использование
# print(generate_timeline())

# Сохранить в файл .canvas
with open("timeline.canvas", "w", encoding="utf-8") as f:
	json.dump(json.loads(generate_timeline(-200, 200, 10)), f, indent=2, ensure_ascii=False)