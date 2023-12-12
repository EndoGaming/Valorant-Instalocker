import pyautogui
import time
with open("agent_names.txt", "r") as file:
    agent_list = file.readlines()
for i in range(len(agent_list)):
    for n in range(len(agent_list[i])):
        if agent_list[i][n] == "\n":
            agent_list[i] = agent_list[i][:n].lower()
            break

timer = 3
while True:   
    print(f"Starts in {timer} seconds!")
    time.sleep(1)
    timer -= 1
    if timer == 0:
        break

coordinates = []
for agent_selected in agent_list:
    try:
        location = pyautogui.locateOnScreen(agent_selected + ".png", confidence= 0.9)
        if location == None:
            print(agent_selected.title() + " not found!")
        else:
            print(agent_selected.title() + " found!")
        coordinates.append(location)
    except:
        coordinates.append("Not found")
        print(agent_selected.title() + " not existing!")
        continue

with open("coords.txt", 'w') as final_coords:
   for i in range(len(agent_list)):
       final_coords.write(f"{coordinates[i]}\n")
