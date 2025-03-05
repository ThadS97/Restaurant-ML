# Restaurant-ML

This Python project uses an example of an agent deciding whether to wait for a table at a restaurant.
Machine learning is used to help the agent make choices in order to come to a final decision. The use of a
decision tree, probability, and uncertainty allows for different scenarios and choices. A brief description for each
Python file in the repository is below.

**Agent.py:** The Agent module is the rudimentary AI agent used in the program. It makes its decisions based on certain factors
and its previous choices. The only choice that the end user can determine for the agent is whether to buy a reservation for
the restaurant in the beginning.

**Attributes.py:** The Attributes module contains enumerations and functions used in the Decisions.py module. The enumerations
are used to signify different situations or conditions in the program. The two functions in the module allow for uncertainity
in the program when it comes to the environment's conditions.

**Decisions.py:** The Decisions module has the functions that are used as 'nodes' for the decision tree. The 'root' node is
the howManyPatrons() function. All 'leaf' nodes are the values True, False, or None. When a leaf node is reached, the decision tree stops
and the agent has made their final decision.

**RestaurantScenario.py:** The RestaurantScenario module is where the main() function is; this is where the end user determines whether to
buy a reservation or not. After that, the howManyPatrons() function is invoked which goes through the decision tree. When True, False,
or None is returned, the program stops.

**TimeAndDay.py:** The TimeAndDay.py module provides the current day and time for the program.

## How to Run Program
1. Ensure that all modules needed to run the program are within the same folder.
2. Open up the terminal and navigate to where the folder that contains the modules.
3. Type and enter 'python RestaurantWait.py' in the terminal.
4. Decide whether or not to buy a reservation for the agent and observe the results.
5. If need be, repeat steps 3 and 4 to see different results within the decision tree. 
