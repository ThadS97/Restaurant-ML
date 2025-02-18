import Attributes
import RestaurantWait as RW
import TimeAndDay

# The functions below act as 'nodes' for the decision tree. This decision tree is a
# representation of the decision-making process for the agent in the program.
# The values of the local variables in each function determine which boolean variable
# or function is returned. When True, False, or None is returned, it is considered to
# be a 'leaf' node and the decision tree stops. The function howManyPatrons() is the
# 'root' node; all subsequent decisions are made based on this node.

def isTodayTheWeekend():
    if (TimeAndDay.currentDay == "Saturday"):
        print("It's Saturday.")
        RW.agent.Agent.isTodayTheWeekend = True
        return True
    elif (TimeAndDay.currentDay == "Sunday"):
        print("It's Sunday.")
        RW.agent.Agent.isTodayTheWeekend = True
        return True
    else:
        print("Too bad it isn't the weekend.")
        return False
    
def isItRaining():
    isThereRainyWeather = Attributes.getRandomChoice()

    if (isThereRainyWeather == "Yes"):
        print("But it's raining outside.")
        return True
    elif (isThereRainyWeather == "No"):
        print("It's sunny outside right now.")
        return False
    
def isBarPresent():
    isThereABar = Attributes.getRandomChoice()

    if (isThereABar == "Yes"):
        print("Thankfully, there's a bar here.")
        return True
    elif (isThereABar == "No"):
        print("There's no bar to sit and drink at.")
        return False

def reservationPrivileges():
    if (RW.agent.Agent.boughtReservation == True):
        print("Good thing I bought a reservation.")
        return None
    elif (RW.agent.Agent.boughtReservation == False):
        print("Too bad I didn't buy that reservation.")
        return isBarPresent()

def isAltRestaurantAround():
    isThereAnotherPlace = Attributes.getRandomChoice()

    if (isThereAnotherPlace == "Yes"):
        print("There's somewhere else to eat at.")
        return isItRaining()
    elif (isThereAnotherPlace == "No"):
        print("This is the only place to eat here.")
        return False

def isAgentHungry():
    isAgentHungry = Attributes.getRandomChoice()

    if (isAgentHungry == "Yes"):
        print("I'm hungry. Is there anywhere else to eat?")
        return isAltRestaurantAround()
    elif (isAgentHungry == "No"):
        print("Not that hungry yet.")
        return False
    
def isAnotherRestaurantAround():
    isThereAnotherPlace = Attributes.getRandomChoice()

    if (isThereAnotherPlace == "Yes"):
        print("Yes. What day is it again?")
        return isTodayTheWeekend()
    elif (isThereAnotherPlace == "No"):
        print("No, there isn't.")
        return reservationPrivileges()

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