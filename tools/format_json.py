import json
import os

def format_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 只保留指定的字段
    keys_to_keep = ["msg", "code", "data"]
    data_keys_to_keep = ["recordMileage", "recodePace", "recodeCadence", "recodeDislikes", "duration", "pointsList", "schoolId", "manageList"]
    filtered_data = {key: data[key] for key in keys_to_keep}
    filtered_data["data"] = {key: data["data"][key] for key in data_keys_to_keep}
    
    # 去除 pointsList 中的 ts 字段
    for point in filtered_data["data"]["pointsList"]:
        if "ts" in point:
            del point["ts"]
    
    formatted_json = json.dumps(filtered_data, indent=4, ensure_ascii=False)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_json)

if __name__ == "__main__":
    json_folder = os.path.join(os.path.dirname(__file__), '..', 'tasks_else')
    for filename in os.listdir(json_folder):
        if filename.endswith(".json"):
            format_json_file(os.path.join(json_folder, filename))



