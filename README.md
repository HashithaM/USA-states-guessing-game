# USA-states-guessing-game
This is a simple game for remembering states of USA
This Python code utilizes the Turtle module to create a simple game where the user guesses the names of U.S. states. It reads state data from a CSV file and displays a map of the U.S. states. As the user correctly guesses state names, the program marks them on the map. If the user types "Exit," the program ends, and a CSV file named "states_to_learn.csv" is created, containing the names of the states the user failed to guess.

The main parts of the code are:

1. Importing necessary libraries: `turtle` for graphics and `pandas` for data handling.
2. Setting up the Turtle screen and loading a map image.
3. Reading state data from a CSV file ("50_states.csv") into a DataFrame.
4. Creating lists to store guessed states (`guessed_states`) and states yet to be guessed (`missing_states`).
5. Running a while loop until all 50 states are guessed or the user exits.
6. Inside the loop:
   - Prompting the user to input a state name.
   - Checking if the input matches a state name, if it does, marking it on the map using Turtle graphics.
   - If the user inputs "Exit," the loop ends, and missing states are collected and stored in a CSV file.
   - Utilizing list comprehension to find missing states efficiently.
7. Saving the list of missing states to a CSV file ("states_to_learn.csv").
8. Using Turtle graphics to display state names on the map.

The `.item()` function is used to extract a single value from a Pandas DataFrame cell. In this case, it's used to extract the state name from the DataFrame `state_data`.
