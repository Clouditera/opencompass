import json

# 读取 JSON 文件
with open('fuzz.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 将 JSON 数据写入 JSONL 文件
with open('fuzz.jsonl', 'w', encoding='utf-8') as file:
    for item in data:
        json_string = json.dumps(item)
        file.write(json_string + '\n')