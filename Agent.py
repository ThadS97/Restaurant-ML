""" The Agent class is a rudimentary artifical intelligence agent
that has four attributes: money (int), boughtReservation (Boolean),
isTodayTheWeekend (Boolean), and knowledgeBase (list). The knowledgeBase
list is a general list used for the agent to 'remember' its previous actions.
The __init__ function initializes the agent in the program while the addKnowledge
function adds knowledge of the agent's environment to the agent's 'memory.'
The knowledgeBase is currently not used in the program; will be incorporated at a
later date. """

class Agent:
    money = 100
    boughtReservation = False
    isTodayTheWeekend = False
    knowledgeBase = []

    def __init__(self, money):
        self.money = money

    def addKnowledge(self, info):
        self.knowledgeBase.append(info)
        return self.knowledgeBase
