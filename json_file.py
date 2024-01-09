import json

# Function to load data from a JSON file
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dict if file doesn't exist

#cool recursive to deal with the nested data structure
def recursive_merge(current_data, new_data):
    for key, value in new_data.items():
        if key not in current_data:
            current_data[key] = value  # Add new key-value pair
        elif isinstance(value, dict):
            # If both values are dictionaries, recurse
            recursive_merge(current_data[key], value)
        # If the key exists but is not a dictionary, we leave the current_data unchanged

def update_json_file(file_path, new_data):
    # Load the current data
    current_data = load_data(file_path)

    # Merge new data into current data
    recursive_merge(current_data, new_data)

    # Save the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(current_data, file, indent=4)

