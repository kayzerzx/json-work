import json
from datetime import datetime

def load_shelter():
    with open("shelter.json", "r", encoding="utf-8") as file:

        print("File contents:", repr(file.read()))

        file.seek(0)

        shelter = json.load(file)

    return shelter

try:
    shelter = load_shelter()

except FileNotFoundError:
    print("shelter.json could not be found.")
    exit()

except json.JSONDecodeError:
    print("shelter.json is empty or contains invalid JSON.")
    exit()

print(shelter["shelter_name"])
previous_food = shelter["food"]
shelter["food"] = 35

print(f"Food changed from {previous_food} to {shelter['food']}.")
with open("shelter.json", "w", encoding="utf-8") as file:
    json.dump(shelter, file, indent=4)

current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
entry = f"{timestamp} | food changed from {previous_food} to {shelter['food']}"
with open("shelter.log", "a", encoding="utf-8") as file: 
    file.write(entry + "\n")

try: 
    with open("shelter.log", "r", encoding="utf-8") as file: 
        journal_text = file.read() 
 
    if journal_text.strip(): 
        print(journal_text) 
    else: 
        print("No changes have been recorded yet.") 
except FileNotFoundError: 
    print("No changes have been recorded yet.")


print(timestamp)


