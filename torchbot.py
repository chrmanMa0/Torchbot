#!/usr/bin/python
import curses
import curses.wrapper
from adventure import Adventure
from lightsource import Adventurer
from lightsource import LightSource

def print_adventurer_list(window):
    adventure_list = current_adventure.get_adventurer_list()
    for x in (0, len(adventure_list) - 1):
        adventurer = adventure_list[x]
        adventurer_str = str(x) + " " + adventurer.get_name()
        adventurer_str = adventurer_str + " " + adventurer.calculate_lighting()
        adventurer_str = adventurer_str + " " + str(adventurer.torches_available) + " torches"
        adventurer_str = adventurer_str + " " + str(adventurer.candles_available) + " candles"
        if adventurer.lantern_available:
            adventurer_str = adventurer_str + " " + str(adventurer.lantern_oil_available) + " oil flasks"
        window.addstr(x + 1, 1, adventurer_str)


def print_main_command_list(window):
    maxyx = window.getmaxyx()
    maxy = maxyx[0]
    command_list = []
    command_list.append("1. Add Adventurer")
    command_list.append("2. Modify Adventurer")
    command_list.append("3. Use Light Source")
    command_list.append("4. Modify Light Source")
    command_list.append("5. Advance Turn Counter")
    x = len(command_list)
    for command in command_list:
        print x
        window.addstr(maxy - (x + 1), 1, command)
        x -= 1


def print_active_light_sources(window):
    index = 0
    initial_line = (window.getmaxyx()[0] - len(current_adventure.lightsources) + 1) / 2
    window.addstr(initial_line, 1, "Active Light Sources: ")
    initial_line += 1
    for lightsource in current_adventure.lightsources:
        window.addstr(initial_line + index, 1, lightsource.get_type())
        index += 1
current_adventure = Adventure()
stephen = Adventurer("Stephen")
fenring = Adventurer("Fenring")
cellos = Adventurer("Cellos")
stephen.add_lantern()
stephen.add_lantern_oil(3)
cellos.add_torches(4)
fenring.add_candles(8)
current_adventure.add_adventurer(fenring)
current_adventure.add_adventurer(cellos)
current_adventure.add_adventurer(stephen)
torch1 = LightSource("Torch", 2, 2, 2)
torch2 = LightSource("Torch", 2, 2, 2)
current_adventure.add_lightsource(torch1)
current_adventure.add_lightsource(torch2)
myscreen = curses.initscr()
myscreen.border(0)
print_adventurer_list(myscreen)
print_main_command_list(myscreen)
print_active_light_sources(myscreen)
myscreen.refresh()
myscreen.getch()

curses.endwin()
