import math
import random
from enum import Enum

# The various enumerations and functions below are used in the Decisions.py file
# to help with the functionality on the functions. As of now, classes Price and
# RestaurantType are not used in the project yet.

class Price(Enum):
    CHEAP = "$"
    MID_PRICE = "$$"
    EXPENSIVE = "$$$"

class RestaurantType(Enum):
    FRENCH = "FR"
    ITALIAN = "IT"
    JAPANESE = "JP"
    CHINESE = "CH"
    THAI = "TH"
    BURGER = "BG"

class Patrons(Enum):
    FEW = "FEW"
    SOME = "SOME"
    FULL = "FULL"

choices = ["Yes", "No"]

def getRandomRange(x, y):
    return math.floor(random.randint(x, y))

def getRandomChoice():
    return random.choice(choices)

class WaitEstimate(Enum):
    SHORT = "SHORT"
    AVERAGE = "AVERAGE"
    LONG = "LONG"
    TOO_LONG = "TOO LONG"