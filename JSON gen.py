import json

def generate_timeline(start_year=1810, end_year=2100, step=10, width_per_year=25):
	nodes = []

	# Группа для timeline
	nodes.append({
		"id": "g1", "type": "group",
		"x": 0, "y": 0,
		"width": 2500, "height": 69,
		"label": "XX век", "color": "#5f5f5f"
	})

	# Текстовые узлы для десятилетий
	years = list(range(start_year, end_year + step, step))
	# years.remove(0)
	colors = ["#5f5f5f", "#9f9f9f"] * (len(years) // 2 + 1)  # Чередование цветов

	for i, (year, color) in enumerate(zip(years, colors)):
		x_pos = i * width_per_year * step
		nodes.append({
			"id": f"t{i+1}", "type": "text",
			"text": f"{year}",
			"x": x_pos, "y": 20,
			"width": width_per_year * step, "height": 27,
			"color": color
		})

	canvas = {
		"nodes": nodes,
		"edges": []
	}

	return json.dumps(canvas, indent=2, ensure_ascii=False)

# Использование
# print(generate_timeline())

# Сохранить в файл .canvas
with open("timeline.canvas", "w", encoding="utf-8") as f:
	json.dump(json.loads(generate_timeline(-200, 200, 10)), f, indent=2, ensure_ascii=False)