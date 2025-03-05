import Attributes
import RestaurantScenario as RS
import TimeAndDay

""" The functions below act as 'nodes' for the decision tree. This decision tree is a
representation of the decision-making process for the agent in the program.
The values of the local variables in each function determine which boolean variable
or function is returned. When True, False, or None is returned, it is considered to
be a 'leaf' node and the decision tree stops. The function howManyPatrons() is the
'root' node; all subsequent decisions are made based on this node. """

# If it is either Saturday or Sunday, the agent decides to go to
# a different restaurant; otherwise, the agent stays in the
# original restaurant and the function returns False
def isTodayTheWeekend():
    if (TimeAndDay.currentDay == "Saturday"):
        print("It's Saturday.")
        RS.agent.Agent.isTodayTheWeekend = True
        return True
    elif (TimeAndDay.currentDay == "Sunday"):
        print("It's Sunday.")
        RS.agent.Agent.isTodayTheWeekend = True
        return True
    else:
        print("Too bad it isn't the weekend.")
        return False

# If it is not raining, the agent decides to eat elsewhere;
# if it's raining, the function returns True
def isItRaining():
    isThereRainyWeather = Attributes.getRandomChoice()

    if (isThereRainyWeather == "Yes"):
        print("But it's raining outside.")
        return True
    elif (isThereRainyWeather == "No"):
        print("It's sunny outside right now.")
        return False

# If there is a bar, the function returns True;
# if not, it returns False. This function is a leaf node
def isBarPresent():
    isThereABar = Attributes.getRandomChoice()

    if (isThereABar == "Yes"):
        print("Thankfully, there's a bar here.")
        return True
    elif (isThereABar == "No"):
        print("There's no bar to sit and drink at.")
        return False

# If the agent bought a reservation, then the decision tree returns
# None; otherwise, the program moves on to the next subtree
def reservationPrivileges():
    if (RW.agent.Agent.boughtReservation == True):
        print("Good thing I bought a reservation.")
        return None
    elif (RW.agent.Agent.boughtReservation == False):
        print("Too bad I didn't buy that reservation.")
        return isBarPresent()

# If there is another restaurant, then the decision tree goes to the
# next subtree; if there isn't, the function returns False
def isAltRestaurantAround():
    isThereAnotherPlace = Attributes.getRandomChoice()

    if (isThereAnotherPlace == "Yes"):
        print("There's somewhere else to eat at.")
        return isItRaining()
    elif (isThereAnotherPlace == "No"):
        print("This is the only place to eat here.")
        return False

# If the agent is hungry, then they attempt to find another restaurant
# and the function moves down to the next subtree;
# if the agent isn't hungry, the function returns False
def isAgentHungry():
    isAgentHungry = Attributes.getRandomChoice()

    if (isAgentHungry == "Yes"):
        print("I'm hungry. Is there anywhere else to eat?")
        return isAltRestaurantAround()
    elif (isAgentHungry == "No"):
        print("Not that hungry yet.")
        return False

# If the agent finds another place to eat, the function goes to the next subtree
# to learn what day is it; otherwise, the function moves on the other subtree to
# determine if the agent has a reservation
def isAnotherRestaurantAround():
    isThereAnotherPlace = Attributes.getRandomChoice()

    if (isThereAnotherPlace == "Yes"):
        print("Yes. What day is it again?")
        return isTodayTheWeekend()
    elif (isThereAnotherPlace == "No"):
        print("No, there isn't.")
        return reservationPrivileges()

# This function gives the agent a random wait time for a table.
# If it is a short wait, the function returns True; if it is an
# average wait time, the function goes to the next subtree to
# determine the agent's hunger; if it's a long wait, the function
# moves to the other subtree to find another restaurant, if any
def estimatedWaitTime():
    numberOfMinutes = Attributes.getRandomRange(1, 90)

    if (numberOfMinutes == 1):
        waitTime = Attributes.WaitEstimate.SHORT
        print("I have to wait " + str(numberOfMinutes) + " minute.")
    elif (numberOfMinutes >= 2 and numberOfMinutes <= 10):
        waitTime = Attributes.WaitEstimate.SHORT
        print("I have to wait " + str(numberOfMinutes) + " minutes.")
    elif (numberOfMinutes >= 11 and numberOfMinutes <= 29):
        waitTime = Attributes.WaitEstimate.AVERAGE
        print("I have to wait " + str(numberOfMinutes) + " minutes.")
    elif (numberOfMinutes >= 30 and numberOfMinutes <= 59):
        waitTime = Attributes.WaitEstimate.LONG
        print("I have to wait " + str(numberOfMinutes) + " minutes.")
    elif (numberOfMinutes >= 60):
        waitTime = Attributes.WaitEstimate.TOO_LONG
        print("I have to wait " + str(numberOfMinutes) + " minutes?")

    if (waitTime.value == "SHORT"):
        print("Not much time to wait.")
        return True
    elif (waitTime.value == "AVERAGE"):
        print("It's going to be a while.")
        return isAgentHungry()
    elif (waitTime.value == "LONG"):
        print("It's a long wait. Is there somewhere else to eat at?")
        return isAnotherRestaurantAround()
    elif (waitTime.value == "TOO LONG"):
        print("Ugh, you got to be joking.")
        return False

# This function is the root node; the number of patrons is
# randomly determined; if there's only a few people in the
# restaurant, the function returns False. If there are some,
# the function returns True. If the restaurant is full, the
# function begins moving through the subtree of the root node
def howManyPatrons():
    numberOfPatrons = Attributes.getRandomRange(0, 50)

    if (numberOfPatrons >= 0 and numberOfPatrons <= 15):
        occupancy = Attributes.Patrons.FEW
    elif (numberOfPatrons >= 16 and numberOfPatrons <= 30):
        occupancy = Attributes.Patrons.SOME
    elif (numberOfPatrons >= 31 and numberOfPatrons <= 50):
        occupancy = Attributes.Patrons.FULL
    
    if (occupancy.value == "FEW"):
        print("Not many people here.")
        return False
    elif (occupancy.value == "SOME"):
        print("There are some people eating here already.")
        return True
    elif (occupancy.value == "FULL"):
        print("This place is packed!")
        return estimatedWaitTime()
