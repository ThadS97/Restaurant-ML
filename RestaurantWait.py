import Agent
import Decisions as D

# Machine Learning Project: Deciding whether the agent should wait for a table at a restaurant
# First, the end user must decide whether or not the agent should buy a reservation for a table.
# After that, the function howManyPatrons() is invoked; this function is the root of the
# decision tree. Probability, uncertainity, and the user's previous decision to buy a reservation
# all factor in to make the agent make a final decision whether or not to wait for a table at the
# restaurant. The main() function is used to begin the program.

agent = Agent

def main():
    print("I want to eat at a restaurant and I have $" + str(agent.Agent.money) + ".")

    print("Should I order a reservation at the restaurant? It costs $20.")

    userChoice = None

    while (userChoice != "Yes" and userChoice != "yes" and userChoice != "YES" and 
           userChoice != "No" and userChoice != "no" and userChoice != "NO"):
        try:
            userChoice = input("Type either 'Yes' or 'No': ")

            if (userChoice == "Yes" or userChoice == "yes" or userChoice == "YES"):
                print("Okay, I'll buy it just in case.")
                agent.Agent.money -= 20
                agent.Agent.boughtReservation = True
                print("Current money: $" + str(agent.Agent.money))
            elif (userChoice == "No" or userChoice == "no" or userChoice == "NO"):
                print("No, I'll take my chances.")
        except ImportError:
            print("A module needed for this program is missing")
        except OSError:
            print("System-related Operation Error")

    print("I'm at the restaurant!")

    willWait = D.howManyPatrons()

    if (willWait == True):
        print("I'll wait for a table.")
    elif (willWait == False):
        print("I'll have a seat.")
    elif (willWait == None):
        print("My reservation has got me a table.")

if __name__ == "__main__":
    main()