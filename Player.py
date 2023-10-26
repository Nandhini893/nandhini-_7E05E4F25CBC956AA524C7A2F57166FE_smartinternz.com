#implement a class called that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.
class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Main program
while True:
    try:
        choice = int(input("Enter 1 for Batsman, 2 for Bowler, or 0 to exit: "))
        if choice == 0:
            break
        elif choice == 1:
            player = Batsman()
        elif choice == 2:
            player = Bowler()
        else:
            print("Invalid choice. Please enter 1 for Batsman, 2 for Bowler, or 0 to exit.")
            continue

        player.play()
    except ValueError:
        print("Invalid input. Please enter a valid choice.")

print("Exiting the program.")