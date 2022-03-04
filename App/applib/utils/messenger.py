# Talks with json to store and retrieve data

import json
import os

def get_user_settings():
    path_to_json_settings = os.path.join('', 'App/applib/Json-lib/user_settings.json')

    with open(path_to_json_settings, 'r') as openfile:

        user_settings = json.load(openfile)
    
    return user_settings



path_to_json_wave = os.path.join('', 'App/applib/Json-lib/user_data.json')

with open(path_to_json_wave, 'r') as openfile:

    # Reading from json file
    user_data = json.load(openfile)


# ! Thing
def get_user_waves() -> list:

    with open(path_to_json_wave, 'r') as openfile:

        user_data = json.load(openfile)

    user_waves = user_data["user-waves"].keys()
    if len(user_waves) != 0:
        return list(user_waves)
    return None



def save_info(wave_arr, wave_name) -> None:
    if wave_name.isspace():
        return
    
    with open(path_to_json_wave, 'r') as openfile:

        user_data = json.load(openfile)

    user_data["user-waves"].update({wave_name: wave_arr})

    with open("App/applib/Json-lib/user_data.json", "w") as outfile:
        json.dump(user_data, outfile, indent=4)


def get_info(wave_name) -> list:

    with open(path_to_json_wave, 'r') as openfile:

        user_data = json.load(openfile)

    return user_data["user-waves"][wave_name]

def del_info(wave_name):
    if wave_name.isspace():
        return

    with open(path_to_json_wave, 'r') as openfile:

        user_data = json.load(openfile)
    try:
        user_data["user-waves"].pop(wave_name)
    except KeyError:
        return 

    with open("App/applib/Json-lib/user_data.json", "w") as outfile:
        json.dump(user_data, outfile, indent=4)
