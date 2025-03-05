import math
import random
from enum import Enum

""" The various enumerations and functions below are used in the Decisions.py file
to help with the functionality on the functions. As of now, the class Price
is not used in the project yet. """

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

restaurants = ["FR", "IT", "JP", "CH", "TH", "BG"]

# Returns the floor value of a list of integers between x (min value) and y (max value)
def getRandomRange(x, y):
    return math.floor(random.randint(x, y))

# Returns a random choice from a non-empty list of items
def getRandomChoice(list):
    return random.choice(list)

class WaitEstimate(Enum):
    SHORT = "SHORT"
    AVERAGE = "AVERAGE"
    LONG = "LONG"
    TOO_LONG = "TOO LONG"
