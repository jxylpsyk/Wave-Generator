import json

with open('Json-lib/user_data.json', 'r') as openfile:

    # Reading from json file
    user_data = json.load(openfile)


def save_info(wave_arr, wave_name) -> None:
    user_data["user-waves"].update({wave_name: wave_arr})

    with open("Json-lib/user_data.json", "w") as outfile:
        json.dump(user_data, outfile, indent=4)


def get_info(wave_name) -> list:
    return user_data["user-waves"][wave_name]
