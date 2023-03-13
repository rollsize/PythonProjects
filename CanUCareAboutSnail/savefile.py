import os
def get_saved_data():
    saved_data = {}
    if os.path.exists("data\snailsave.txt"): # if save file exist
        with open("data\snailsave.txt", "r", encoding="UTF-8") as savefile:
            lines = savefile.read().splitlines()
            for line in lines:
                splited_line = line.split(" = ")
                if splited_line[1] == "False":
                    saved_data[splited_line[0]] = False
                elif splited_line[1] == "True":
                    saved_data[splited_line[0]] = True
                else:
                    saved_data[splited_line[0]] = int(splited_line[1])
    else:
        saved_data["hungry"] = 10
        saved_data["logicCoins"] = 100
        saved_data["years"] = 0
        saved_data["is_ill"], saved_data["is_sick"], saved_data["is_dirty"] = False, False, False

        save_data(saved_data)
    return [saved_data["logicCoins"], saved_data["years"], saved_data["hungry"], saved_data["is_ill"], saved_data['is_sick'], saved_data["is_dirty"]]

def save_data(data:dict):
    with open("data\snailsave.txt", "w", encoding="UTF-8") as savefile:
            for key in data.keys():
                savefile.write(f"{key} = {data[key]}\n")

def delete_file():
    os.remove("data\snailsave.txt")