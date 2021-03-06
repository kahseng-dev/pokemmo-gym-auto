try:
    import pydirectinput as di
    from time import sleep
    import utilities.action as action

except ModuleNotFoundError:
    print("Please install pydirectinput library using 'pip install pydirectinput'")

def menu():
    print("Select your Kanto Gym")
    menu_options = ["Pewter", "Cerulean", "Vermillion", "Celadon", "Fuchsia", "Saffron", "Cinnabar", "Viridian (Unavailable)", "Back"]

    for i in range(len(menu_options)):
        print("[{}] {}".format(i+1, menu_options[i]))

def pewter_pathing_in():
    di.keyDown('d')
    sleep(0.4)
    di.keyUp('d')
    di.keyDown('w')
    sleep(1.1)
    di.keyUp('w')
    di.keyDown('a')
    sleep(1.15)
    di.keyUp('a')
    di.keyDown('s')
    sleep(0.4)
    di.keyUp('s')
    di.keyDown('d')
    sleep(0.535)
    di.keyUp('d')
    di.keyDown('w')
    sleep(0.2)
    di.keyUp('w')
    print("Entering Pewter City Gym...")

def approach_brock():
    di.keyDown('w')
    sleep(1.4)
    di.keyUp('w')

def pewter_pathing_out():
    di.keyDown('s')
    sleep(1.5)
    di.keyUp('s')

def cerulean_pathing_in():
    di.keyDown('s')
    sleep(0.02)
    di.keyUp('s')
    di.keyDown('d')
    sleep(0.64)
    di.keyUp('d')
    di.keyDown('w')
    sleep(0.32)
    di.keyUp('w')
    print("Entering Cerulean City Gym...")

def approach_misty():
    di.keyDown('d')
    sleep(0.2)
    di.keyUp('d')
    di.press('shift')
    di.keyDown('w')
    sleep(1.3)
    di.keyUp('w')
    di.keyDown('d')
    sleep(0.4)
    di.keyUp('d')
    di.keyDown('w')
    sleep(0.4)
    di.keyUp('w')
    di.keyDown('a')
    sleep(0.6)
    di.keyUp('a')
    di.press('w')

def cerulean_pathing_out():
    di.keyDown('d')
    sleep(0.6)
    di.keyUp('d')
    di.keyDown('s')
    sleep(0.6)
    di.keyUp('s')
    di.keyDown('a')
    sleep(0.4)
    di.keyUp('a')
    di.keyDown('s')
    sleep(1.4)
    di.keyUp('s')
    di.press('a')
    di.press('s')

def vermillion_pathing_in():
    di.keyDown('d')
    sleep(1)
    di.keyUp('d')
    di.keyDown('s')
    sleep(0.5)
    di.keyUp('s')
    di.keyDown('a')
    sleep(0.3)
    di.keyUp('a')
    di.keyDown('s')
    sleep(0.56)
    di.keyUp('s')
    di.keyDown('a')
    sleep(0.364)
    di.keyUp('a')
    di.keyDown('s')
    sleep(0.1)
    di.keyUp('s')
    action.cut_tree()
    di.keyDown('s')
    sleep(0.45)
    di.keyUp('s')
    di.keyDown('a')
    sleep(0.302)
    di.keyUp('a')
    di.keyDown('w')
    sleep(0.2)
    di.keyUp('w')
    print("Entering Vermillion City Gym...")

def approach_surge():
    di.press('d')
    di.keyDown('w')
    sleep(3)
    di.keyUp('w')
    di.press('a')

def vermillion_pathing_out():
    di.keyDown('s')
    sleep(3)
    di.keyUp('s')
    di.press('a')
    di.press('s')

def celadon_pathing_in():
    sleep(0.1)
    di.press('s')
    di.keyDown('a')
    sleep(0.452)
    di.keyUp('a')
    di.keyDown('s')
    sleep(0.74)
    di.keyUp('s')
    di.keyDown('a')
    sleep(0.791)
    di.keyUp('a')
    di.keyDown('s')
    sleep(0.7)
    di.keyUp('s')
    di.keyDown('d')
    sleep(0.65)
    di.keyUp('d')
    di.keyDown('s')
    sleep(0.2)
    di.keyUp('s')
    action.cut_tree()
    di.keyDown('s')
    sleep(0.345)
    di.keyUp('s')
    di.keyDown('a')
    sleep(2.23)
    di.keyUp('a')
    di.keyDown('w')
    sleep(1)
    di.keyUp('w')
    print("Entering Celadon City Gym...")

def approach_erika():
    di.keyDown('w')
    sleep(1.4)
    di.keyUp('w')
    action.cut_tree()
    di.keyDown('w')
    sleep(0.8)
    di.keyUp('w')

def celadon_pathing_out():
    di.keyDown('s')
    sleep(2.8)
    di.keyUp('s')

def fuchsia_pathing_in():
    di.press('s')
    di.keyDown('a')
    sleep(1.2)
    di.keyUp('a')
    di.keyDown('w')
    sleep(0.4)
    di.keyUp('w')
    print("Entering Fuchsia City Gym...")

def approach_koga():
    di.keyDown('d')
    sleep(1.3)
    di.keyUp('d')
    di.keyDown('w')
    sleep(3.8)
    di.keyUp('w')
    di.keyDown('a')
    sleep(0.8)
    di.keyUp('a')
    di.keyDown('s')
    sleep(1.3)
    di.keyUp('s')
    di.keyDown('a')
    sleep(1.25)
    di.keyUp('a')
    di.keyDown('s')
    sleep(0.25)
    di.keyUp('s')
    di.keyDown('d')
    sleep(0.85)
    di.keyUp('d')
    di.press('s')

def fuchsia_pathing_out():
    di.keyDown('a')
    sleep(1)
    di.keyUp('a')
    di.keyDown('w')
    sleep(0.32)
    di.keyUp('w')
    di.keyDown('d')
    sleep(1.35)
    di.keyUp('d')
    di.keyDown('w')
    sleep(1.8)
    di.keyUp('w')
    di.keyDown('d')
    sleep(1)
    di.keyUp('d')
    di.keyDown('s')
    sleep(3.8)
    di.keyUp('s')
    di.keyDown('a')
    sleep(1.2)
    di.keyUp('a')
    di.press('s')

def saffron_pathing_in():
    di.press('s')
    di.keyDown('d')
    sleep(2.02)
    di.keyUp('d')
    di.keyDown('w')
    sleep(1.96)
    di.keyUp('w')
    di.keyDown('a')
    sleep(0.25)
    di.keyUp('a')
    di.keyDown('w')
    sleep(0.4)
    di.keyUp('w')
    print("Entering Saffron City Gym...")

def approach_sabrina():
    di.keyDown('d')
    sleep(0.8)
    di.keyUp('d')
    di.keyDown('w')
    sleep(1)
    di.keyUp('w')
    di.keyDown('a')
    sleep(8)
    di.keyUp('a')
    di.keyDown('s')
    sleep(1)
    di.keyUp('s')
    sleep(1)
    di.keyDown('a')
    sleep(0.6)
    di.keyUp('a')
    di.keyDown('w')
    sleep(0.8)
    di.keyUp('w')

def saffron_pathing_out():
    di.keyDown('s')
    sleep(0.7)
    di.keyUp('s')
    di.keyDown('d')
    sleep(1)
    di.keyUp('d')
    di.keyDown('w')
    sleep(1.2)
    di.keyUp('w')
    di.keyDown('d')
    sleep(8)
    di.keyUp('d')
    sleep(1)
    di.keyDown('s')
    sleep(0.6)
    di.keyUp('s')
    di.keyDown('a')
    sleep(0.6)
    di.keyUp('a')
    di.keyDown('s')
    sleep(0.2)
    di.keyUp('s')

def cinnabar_pathing_in():
    di.keyDown('d')
    sleep(0.5)
    di.keyUp('d')
    di.keyDown('w')
    sleep(0.6)
    di.keyUp('w')
    di.press('a')
    di.keyDown('w')
    sleep(0.3)
    di.keyUp('w')
    print("Entering Cinnabar City Gym...")

def approach_blaine():
    di.press('d')
    di.keyDown('w')
    sleep(3.5)
    di.keyUp('w')
    di.keyDown('a')
    sleep(1.4)
    di.keyUp('a')
    di.keyDown('s')
    sleep(3.4)
    di.keyUp('s')
    di.keyDown('a')
    sleep(2.2)
    di.keyUp('a')
    di.keyDown('w')
    sleep(3.4)
    di.keyUp('w')

def cinnabar_pathing_out():
    di.keyDown('s')
    sleep(3.2)
    di.keyUp('s')
    di.keyDown('d')
    sleep(2.2)
    di.keyUp('d')
    di.keyDown('w')
    sleep(3.5)
    di.keyUp('w')
    di.keyDown('d')
    sleep(1.34)
    di.keyUp('d')
    di.keyDown('s')
    sleep(3.5)
    di.keyUp('s')
    di.keyDown('a')
    sleep(0.1)
    di.keyUp('a')
    di.keyDown('s')
    sleep(1)
    di.keyUp('s')

def main():
    menu()
    user_input = int(input('\nEnter option: '))

    if user_input == 1:
        action.initialize("Pewter")
        action.goto(806, 499)
        di.press('2')
        pewter_pathing_in()
        sleep(1)
        di.press('shift')
        approach_brock()
        # enter combat
        sleep(1)
        pewter_pathing_out()
    
    elif user_input == 2:
        action.initialize("Cerulean")
        action.goto(1046, 479)
        di.press('2')
        cerulean_pathing_in()
        sleep(1)
        approach_misty()
        # enter combat
        sleep(1)
        cerulean_pathing_out()

    elif user_input == 3:
        action.initialize("Vermillion")
        action.goto(1044, 624)
        di.press('2')
        vermillion_pathing_in()
        sleep(1)
        di.press('shift')
        approach_surge()
        # enter combat
        sleep(1)
        vermillion_pathing_out()

    elif user_input == 4:
        action.initialize("Celadon")
        action.goto(972, 554)
        di.press('2')
        celadon_pathing_in()
        sleep(1)
        di.press('shift')
        approach_erika()
        # enter combat
        sleep(1)
        celadon_pathing_out()

    elif user_input == 5:
        action.initialize("Fuchsia")
        action.goto(996, 696)
        di.press('2')
        fuchsia_pathing_in()
        sleep(1)
        di.press('shift')
        approach_koga()
        # enter combat
        sleep(1)
        fuchsia_pathing_out()

    elif user_input == 6:
        action.initialize("Saffron")
        action.goto(1044, 552)
        di.press('2')
        saffron_pathing_in()
        sleep(1)
        di.press('shift')
        approach_sabrina()
        # enter combat
        sleep(1)
        saffron_pathing_out()

    elif user_input == 7:
        action.initialize("Cinnabar")
        action.goto(804, 745)
        di.press('2')
        cinnabar_pathing_in()
        sleep(1)
        di.press('shift')
        approach_blaine()
        # enter combat
        sleep(1)
        cinnabar_pathing_out()

    elif user_input == 8:
        print("Viridian City Gym is currently not scripted in PokeMMO")

    elif user_input == 9:
        return
