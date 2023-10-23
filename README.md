# Valorant-Instalocker
In this repository you can find a valorant instalocker that automatically locks your agents for you

It was created in Python and the only requirement you need except having Python installed is "pyautogui" because this detects pictures of your agents and clicks on them

To install Python visit https://www.python.org/ and to install pyautogui open Powershell and type in "pip install pyautogui"

Most of the coordinates in here are already up to date but everytime the gamedesign changes you can update them yourself

Step 1: Take a Screenshot of the Agent Select Screen in Fullscreen and save it while no agent is chosen yet (I recommend doing this in a private match)

Step 2: Run "tracker" to get the coordinates of the middle of the lock button and write them in "box_coords.txt" (X first row, Y second row)

Step 3: Add every Agent you want to be able to use in "agent_names.txt" (Preferably in alphabetical order but not necessary)

I recommend adding all of them immediately so you don't have to setup multiple times

Step 4: Save a Screenshot of the agents you want to use with their name written in lowercase in this folder, for example: reyna.png (Should look like the agent example)

Just like on Step 3 I recommend adding all of them so you don't have to set up multiple times when you want to use other agents

Step 5: Start "tracker_for_locker" while having the Screenshot of the Agent Select Screen opened in Fullscreen and wait till it closes automatically (may take a minute for slower PCs)

Step 5.1: The tracker closes by itself when it finishes, then you can close the Screenshot and delete it if you want when everything is setup correctly

Step 6: Start the "locker" then enter the agent and the program will instalock for you!

The locker will list all the agents, that you've set up and are ready to be used

Step 7: Have fun!

Some in Game stuff like agent portraits may change over time, when that happens just repeat the steps till everything works again

The Randomizer is the same to set up and it will change the agent you randomly instalock after every game

It will also only use the ones that are setup so if you only have one agent ready it will only choose that agent

The mouse should not be moved in the agent select because otherwise it may not instalock correctly
