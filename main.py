import time

def introduction():
    print("Welcome to 'The Galactic Odyssey'!")
    time.sleep(1)
    print("You are a space explorer on a mission to find the lost artifact known as the Stellar Beacon.")
    time.sleep(1)
    print("Your spaceship is ready, and the galaxy awaits your exploration. Your journey begins...\n")

def make_choice(options):
    while True:
        print("Choose your action:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def space_station():
    print("You start your journey at the Space Explorer's Station.")
    time.sleep(1)
    print("You have three planets to choose from. Each planet is rumored to hold clues about the Stellar Beacon.")
    time.sleep(1)
    choice = make_choice(["Visit the Luminous Planet", "Explore the Nebula World", "Land on the Icebound Moon"])

    if choice == 1:
        print("You set course for the Luminous Planet, known for its radiant landscapes.")
        time.sleep(1)
        return "luminous_planet"
    elif choice == 2:
        print("You head towards the Nebula World, surrounded by colorful cosmic clouds.")
        time.sleep(1)
        return "nebula_world"
    else:
        print("You choose to land on the Icebound Moon, a frozen celestial body.")
        time.sleep(1)
        return "icebound_moon"

def luminous_planet():
    print("As you approach the Luminous Planet, you encounter a space anomaly.")
    time.sleep(1)
    print("You must navigate through the anomaly to reach the planet's surface.")
    time.sleep(1)
    choice = make_choice(["Activate the shields and power through", "Attempt to navigate around the anomaly"])

    if choice == 1:
        print("You activate the shields and power through the anomaly successfully.")
        time.sleep(1)
        print("You land on the Luminous Planet, where ancient ruins might hold clues about the Stellar Beacon.")
        time.sleep(1)
        return "ancient_ruins"
    else:
        print("You try to navigate around the anomaly but get caught in its gravitational pull.")
        time.sleep(1)
        print("Your ship suffers minor damage, but you manage to land on the Luminous Planet.")
        time.sleep(1)
        return "ancient_ruins"

def nebula_world():
    print("The Nebula World is known for its ever-shifting cosmic clouds.")
    time.sleep(1)
    print("You must choose a route through the nebula to reach the planet's surface.")
    time.sleep(1)
    choice = make_choice(["Navigate through the densest part of the nebula", "Take a longer route around the nebula"])

    if choice == 1:
        print("You bravely navigate through the dense nebula, avoiding obstacles skillfully.")
        time.sleep(1)
        print("You land on the Nebula World, where a scientific outpost might have information about the Stellar Beacon.")
        time.sleep(1)
        return "scientific_outpost"
    else:
        print("You take a longer route around the nebula, encountering a mysterious anomaly.")
        time.sleep(1)
        print("Your scanners detect an abandoned spaceship. Investigate or continue?")
        time.sleep(1)
        choice = make_choice(["Investigate the abandoned spaceship", "Continue to the Nebula World"])

        if choice == 1:
            print("You investigate the abandoned spaceship and find valuable resources.")
            time.sleep(1)
            print("You continue to the Nebula World with extra supplies.")
            time.sleep(1)
            return "scientific_outpost"
        else:
            print("You decide to continue to the Nebula World without investigating the anomaly.")
            time.sleep(1)
            return "scientific_outpost"

def icebound_moon():
    print("The Icebound Moon is covered in icy landscapes, and visibility is low.")
    time.sleep(1)
    print("You must choose a safe landing site to avoid damaging your spaceship.")
    time.sleep(1)
    choice = make_choice(["Land in the open icy plains", "Search for a sheltered cave to land"])

    if choice == 1:
        print("You choose to land in the open icy plains and successfully touch down.")
        time.sleep(1)
        print("You explore the frozen surface, hoping to find clues about the Stellar Beacon.")
        time.sleep(1)
        return "frozen_surface"
    else:
        print("You search for a sheltered cave to land but struggle with low visibility.")
        time.sleep(1)
        print("Your spaceship sustains minor damage, but you find a cave to explore.")
        time.sleep(1)
        return "frozen_cave"

def ancient_ruins():
    print("You explore the ancient ruins on the Luminous Planet.")
    time.sleep(1)
    print("You discover a holographic message that reveals the location of the Stellar Beacon.")
    time.sleep(1)
    print("Congratulations! You uncovered a crucial piece of the puzzle.")
    time.sleep(1)
    return "completed"

def scientific_outpost():
    print("You reach the scientific outpost on the Nebula World.")
    time.sleep(1)
    print("Scientists provide information about the Stellar Beacon's energy signature.")
    time.sleep(1)
    print("Your mission is one step closer to success.")
    time.sleep(1)
    return "completed"

def frozen_surface():
    print("Exploring the icy plains on the Icebound Moon, you encounter a native alien species.")
    time.sleep(1)
    print("Communicating with them, you learn about a hidden cave with ancient artifacts.")
    time.sleep(1)
    print("You decide to investigate the cave for more information about the Stellar Beacon.")
    time.sleep(1)
    return "frozen_cave"

def frozen_cave():
    print("You enter the frozen cave and find ancient hieroglyphs that lead to the Stellar Beacon.")
    time.sleep(1)
    print("Congratulations! You've successfully decoded the ancient message.")
    time.sleep(1)
    return "completed"

# Main game loop
def main():
    introduction()
    levels = ["space_station", "luminous_planet", "nebula_world", "icebound_moon"]
    current_level = 0

    while current_level < len(levels):
        current_location = globals()[levels[current_level]]()

        if current_location == "completed":
            print("Congratulations! You completed the level.")
            current_level += 1

if __name__ == "__main__":
    main()
