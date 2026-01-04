** start of main.py **

def add_setting(settings, pair):
    # 1. Extract and convert to lowercase
    key, value = pair
    key = key.lower()
    value = value.lower()

    # 2. Check if the key is already present
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    # 3. If not present, add it and confirm
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
    # 1. Unpack and lowercase
    key, value = pair
    key = key.lower()
    value = value.lower()

    # 2. Check if the key IS in the dictionary
    if key in settings:
        settings[key] = value 
        return f"Setting '{key}' updated to '{value}' successfully!"

    # 3. If key is NOT found
    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    #1. Convert the input key to lowercase
    key = key.lower()

    #2. Check if the key exists IN the dictionary
    if key in settings:
        #3. Remove the key-value pair
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    #4. If key is NOT found
    else:
        return f"Setting not found!"

def view_settings(settings):
    #1. Check if the dictionary is empty
    if not settings:
        return "No settings available."

    #2. Start the setting withthe header
    #We include \n to move the first setting to the next line 
    output = "Current User Settings:\n"

    #3. Loop the dictionary and build the string
    for key, value in settings.items():
        # .capitalize() makes the first letter uppercase (e.g theme -> Theme)
        output += f"{key.capitalize()}: {value}\n"
    
    #4. Return the final formatted string
    # .strip() removes the very last \n at the end so it stays neat
    return output
# Create the dictionary with some initial key-value pairs
test_settings = {
    "Theme": "dark",
    "Notifications": "enable",
    "Volume": "high"

}


** end of main.py **

