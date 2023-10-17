import pyautogui
import os
import time
import random

with open("agent_names.txt", "r") as file:
    list = file.readlines()
for i in range(len(list)):
    for n in range(len(list[i])):
        if list[i][n] == "\n":
            list[i] = list[i][:n]
            break

with open("box_coords.txt", "r") as file:
    box_coords = file.readlines()
for i in range(len(box_coords)):
    for n in range(len(box_coords[i])):
        if box_coords[i][n] == "\n":
            box_coords[i] = int(box_coords[i][:n])
            break

coords_list = []
try:
    with open("coords.txt", "r") as file:
        for line in file:
            coords_list.append(line)
except:
        print("Setup was not completed!")
        print("Please setup correctly before usage!")
        time.sleep(3)
        exit()

agent_list = {}
for i in range(len(coords_list)):
    whole_coord = coords_list[i]
    if whole_coord == "Not found\n" or whole_coord == "None\n":
        continue
    final_coord = []
    index_x1 = 9
    index_x2 = 0
    for n in range(len(whole_coord)):
        if whole_coord[n] == ",":
            index_x2 = n
            break
    index_y1 = index_x2 + 6
    for n in range(len(whole_coord)):
        if whole_coord[index_y1 + n] == ",":
            index_y2 = (index_y1 + n)
            break
    index_z1 = index_y2 + 8
    for n in range(len(whole_coord)):
        if whole_coord[index_z1 + n] == ",":
            index_z2 = (index_z1 + n)
            break
    index_w1 = index_z2 + 9
    for n in range(len(whole_coord)):
        if whole_coord[index_w1 + n] == ")":
            index_w2 = (index_w1 + n)
            break
    final_coord.append(whole_coord[index_x1:index_x2])
    final_coord.append(whole_coord[index_y1:index_y2])
    final_coord.append(whole_coord[index_z1:index_z2])
    final_coord.append(whole_coord[index_w1:index_w2])
    agent_list[list[i]] = final_coord

actual_list = []
for name in list:
    try:
        agent_list[name]
        actual_list.append(name)
    except:
        continue

def start_menu():
    if agent_list == {}:
        print("Setup was not completed!")
        print("No Agents found!")
        time.sleep(3)
        exit()
    os.system("cls") 
    print("Program running...")
    agent = random.choice(actual_list)
    return agent.lower()

agent_selected = start_menu()

try:
    while True:
        if pyautogui.locateOnScreen(agent_selected + ".png", confidence= 0.9, region=(int(agent_list[agent_selected][0]), int(agent_list[agent_selected][1]), int(agent_list[agent_selected][2]), int(agent_list[agent_selected][3]))):
            location_x = int(agent_list[agent_selected][0]) + 40 # Muss maybe angepasst werden bei Änderungen am Gamedesign
            location_y = int(agent_list[agent_selected][1]) + 35 # Muss maybe angepasst werden bei Änderungen am Gamedesign
            pyautogui.click(location_x, location_y)
            pyautogui.moveTo(box_coords[0], box_coords[1], 0.001)
            pyautogui.click()
            print("\nYou've rolled " + agent_selected.title() + "!\n")
            while True:
                if pyautogui.locateOnScreen(agent_selected + ".png", confidence= 0.9, region=(int(agent_list[agent_selected][0]), int(agent_list[agent_selected][1]), int(agent_list[agent_selected][2]), int(agent_list[agent_selected][3]))):
                    agent_selected = start_menu()
                    break
except KeyboardInterrupt:
    print("\nProgram stopped!\n")
except Exception as err:
    print(err)