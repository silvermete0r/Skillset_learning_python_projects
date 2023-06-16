import os
import shutil
import json

topics = ["counting_and_probability", "geometry", "intermediate_algebra", "number_theory", "prealgebra", "precalculus"]

for topic in topics:
    math_folder = f"MATH/{topic}"
    try:
        difficulty_levels = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]
        for level in difficulty_levels:
            folder_path = os.path.join(math_folder, level)
            os.makedirs(folder_path, exist_ok=True)

        for file_name in os.listdir(math_folder):
            if file_name.endswith(".json"):
                file_path = os.path.join(math_folder, file_name)
                with open(file_path, "r") as file:
                    try:
                        data = json.load(file)
                        difficulty_level = data["level"]
                        destination_folder = os.path.join(math_folder, difficulty_level)
                        shutil.copy(file_path, destination_folder)
                    except json.JSONDecodeError:
                        print(f"Failed to load JSON file: {file_name}")
                        continue
                    except KeyError:
                        print(f"Failed to extract difficulty level from: {file_name}")
                        continue
    except Exception as e:
        print("Something went wrong, ERROR: {}".format(e))
    else:
        print("Files filtered, copied, and pasted successfully!")
    finally:
        print("{} is Finished!".format(topic))