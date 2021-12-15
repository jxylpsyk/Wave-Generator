import json

# refactor to avoid multiple calls
with open('Json-lib/user_data.json', 'r') as openfile:

    # Reading from json file
    user_wave_d = json.load(openfile)


def save_wave(wave_arr, wave_name) -> None:
    user_wave_d["user-waves"][wave_name] = wave_arr

    json_object = json.dumps(user_wave_d, indent=4)

    with open("Json-lib/user_data.json", "w") as outfile:
        outfile.write(json_object)


def get_wave(wave_name) -> list:
    try:
        return user_wave_d["user-waves"][wave_name]
    except (KeyError):
        raise KeyError("Invalid wave name")
