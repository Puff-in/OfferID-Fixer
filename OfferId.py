import json

with open("FurnitureData.json", "r") as file:
    data = json.load(file)

for item in data.get("roomitemtypes", {}).get("furnitype", []):
    item["offerid"] = item["id"]

for item in data.get("wallitemtypes", {}).get("furnitype", []):
    item["offerid"] = f"{item['id']}97"

with open("new_FurnitureData.json", "w") as file:
    json.dump(data, file, indent=4)

print("Updated Furniture Data has been saved to 'new_FurnitureData.json'")
