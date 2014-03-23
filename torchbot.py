#!/usr/bin/python
import curses
import curses.wrapper
from adventure import Adventure
from lightsource import Adventurer
from lightsource import LightSource

def print_adventurer_list(window):
    adventurer_list = current_adventure.get_adventurer_list()
    line = 1
    lighting_position = 22
    torches_position = 29
    candles_position = 40
    oil_position = 51
    for adventurer in adventurer_list:
        window.addstr(line, 1, str(line) + " " + adventurer.get_name())
        window.addstr(line, lighting_position, adventurer.calculate_lighting())
        window.addstr(line, torches_position, str(adventurer.torches_available) + " torches")
        window.addstr(line, candles_position, str(adventurer.candles_available) + " candles")
        if adventurer.lantern_available:
            window.addstr(line, oil_position, str(adventurer.lantern_oil_available) + " oil flasks")
        line += 1


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
joe = Adventurer("Joe The Barbarian")
stephen.add_lantern()
stephen.add_lantern_oil(3)
cellos.add_torches(4)
fenring.add_candles(8)
fenring.add_torches(3)
current_adventure.add_adventurer(fenring)
#current_adventure.add_adventurer(cellos)
current_adventure.add_adventurer(stephen)
current_adventure.add_adventurer(joe)
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
