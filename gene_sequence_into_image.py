#AB059661.1.fna
# import necessary libraries 
import numpy as np
# numpy to work with numbers
import matplotlib.pyplot as plt
#pyplot for plotting
import matplotlib.animation as animation
#animation for plotting
from matplotlib import colors
#colors used for color map

# Function to reads a FASTA file and returns converted binary sequence.
def read_fasta_file(fasta_filename):
    sequence = ""
    with open(fasta_filename, "r") as fasta_file:
        for line in fasta_file:
            if not line.startswith(">"):  # Skip header lines
                               # Create a dictionary for the characters to replace and their replacements

                # if your sequence is a gene sequence then uncomment the bellow line
                # replacements = {'A': '00', 'T': '01', 'G': '10','C':'11'}

                # if your sequence is a RNA sequence then uncomment the bellow line
                # replacements = {'A': '00', 'U': '01', 'G': '10','C':'11'}
                
                # if your sequence is a protein sequence then uncomment the bellow line
                # replacements = {'P': '00001', 'Q': '00100', 'R': '00110','Y':'01100', 'W': '01110', 'T': '10000','M': '10011','N': '10101', 'V': '11010', 'E' : '11101', 'L': '00011', 'H': '00101', 'S': '01001', 'F': '01011', 'C': '01111', 'I': '10010', 'K': '10100', 'A': '11001', 'D' : '11100', 'G': '11110'}
                # Create a translation table using str.maketrans()
                translation_table = str.maketrans(replacements)
                # Use the translate method to replace the characters
                sequence += line.strip().translate(translation_table)
    return sequence
    
def initial_matrix(n_cells, n_generations,first_row):
    spacetime = np.zeros(shape=(n_generations, n_cells))
#np.zeros: This is a function from the NumPy library used to create arrays filled with zeros.
#shape=(n_generations, n_cells): This argument specifies the shape of the array as a tuple.    
    spacetime[0] = list(map(int, first_row)) #first_row
    return spacetime

# This function initializes the animation.
def initialize(first_row, n_cells=0, n_generations=100, rule={}):
# number of cells innitially zero but gets set in main() function
# number of generations is by default 100    
# the variable rule is a python dictionary which is empty now    
        initial_state = initial_matrix(n_cells, n_generations,first_row)
# calling the just above defined function to get the innitial state
        cmap = colors.ListedColormap(['yellow', 'green'])
# It defines a color map for visualizing the cell states ('yellow', 'green').        
        bounds = [ 0, 1]
#The line bounds = [0, 1 ] defines a list named bounds that is used for color mapping in the cellular automata animation.A colormap is a function that maps numerical values to colors.The bounds list defines these transitions between colors.
        norm = colors.BoundaryNorm(bounds, cmap.N)
#The line norm = colors.BoundaryNorm(bounds, cmap.N) creates a color normalization object named norm using the BoundaryNorm class from the matplotlib.colors library. This object plays a crucial role in mapping the cell states.BoundaryNorm class is used for color mapping in situations where data has discrete values (like cell states in your case) instead of continuous values. It maps these discrete values to specific colors in a colormap. 
        fig = plt.figure()
#The line  fig = plt.figure()  creates a new figure object for the cellular automata animation using the matplotlib.pyplot library (imported as plt). plt.figure(): This calls the figure function from the plt (matplotlib.pyplot) module. figure(): This function creates a new empty figure object. A figure is the top-level container for a matplotlib plot. It can hold one or more axes (areas where data is plotted). We can create multiple figures in your program using plt.figure() multiple times. Each call will create a new independent figure window.
        frame = plt.gca()
#This calls the gca() function from the plt module.This function stands for "get current axes". It retrieves a handle to the current axes object associated with the most recently created figure.In your code, you previously created a new figure using plt.figure(). This line assumes that you want to work with the axes (plotting area) associated with that newly created figure. It checks if there are any existing axes on the current figure. In your code, since you just created a new figure with plt.figure(), there should be no existing axes yet. It creates a new set of axes as a child of the current figure. This new set of axes becomes the "current axes" for subsequent plotting operations.      
        frame.axes.get_xaxis().set_visible(False)
        # hide x axis
        frame.axes.get_yaxis().set_visible(False)
        # hide y axis
        grid = plt.imshow(initial_state, interpolation='nearest', cmap=cmap, norm=norm)
#It displays the initial state using plt.imshow.The line  grid = plt.imshow(initial_state, interpolation='nearest', cmap=cmap, norm=norm)  creates an image visualization of the initial state of the cellular automata grid using matplotlib.pyplot (imported as plt). Grid variable will store a reference to the created Matplotlib image object representing the cellular automata grid.the imshow is a function from plt to display an image. This function is used to display a two-dimensional data array as an image. In this case, the data array is initial_state, which represents the initial configuration of cells in the cellular automata simulation (0s and 1s).
        ani = animation.FuncAnimation(fig, next_generation,
                                      fargs=(grid, initial_state, rule),
                                      frames=n_generations - 1,
                                      interval=50,
                                      blit=False)
# ani is an animation object created by using animation.FuncAnimation. This animates the function next_generation for n_generations - 1 frames with a delay of 50 milliseconds between frames.animation.FuncAnimation(...) is the core part that creates the animation.(a) fig is the figure object (fig) created earlier using plt.figure(). The animation will be displayed on this figure.(b)next_generation is the function that will be called for each frame of the animation. Here, it refers to the next_generation function we defined earlier in the code. This function calculates the next generation of the cellular automata based on the current state and the rule.(c) fargs=(grid, initial_state, rule): These are additional arguments passed to the next_generation function at each frame.grid is the Matplotlib image object (grid) created earlier using plt.imshow. It represents the current state of the cellular automata grid that will be updated in each frame.initial_state is the NumPy array (initial_state) containing the overall state of the cellular automata across all generations. The next_generation function will use this to update the grid for the next generation.rule is the dictionary (rule) defining the cellular automata rule used for state transitions. The next_generation function will refer to this rule to determine the new state of each cell.(d) frames=n_generations - 1 is the argument specifies the total number of frames in the animation. Here, it's set to n_generations - 1 because the initial state is already displayed before the animation starts. So, the animation will show n_generations - 1 frames representing the transition between generations.(e)interval=50 is the argument sets the delay (in milliseconds) between frames. Here, it's set to 50, which means there will be a 50ms pause between displaying consecutive frames of the animation.(f) blit=False is the argument controls how the animation updates the image. Here, blit=False is used, which means a full redraw will occur for each frame. This might be less efficient for complex animations, but it ensures a clean update without artifacts in this case.
        plt.show()

# This function calculates the next generation of the cellular automata. The arguments (a) i is the Current generation index. (b) grid is the Matplotlib image object representing the grid. (c) initial_state is the NumPy array containing the current state of all cells across generations. (d) rule is the Dictionary defining the cellular automata rule.
def next_generation(i, grid, initial_state, rule):

    current_generation = initial_state[i]
# It retrieves the current generation from the initial state.
    new_state = initial_state.copy()
# It creates a copy of the initial state to avoid modifying the original.
    new_generation = process(current_generation, rule)
# process() is called to calculate the new generation based on the current generation and rule.
    new_state[i + 1] = new_generation
# It updates the new generation in the initial state copy.
    grid.set_data(new_state)
# It updates the data for the grid image with the new state. 
    initial_state[:] = new_state[:]
# It updates the entire initial state with the new state copy (for next generation calculation).
    return grid
# It returns the updated grid image.

# This function applies the cellular automata rule to a generation.It takes two arguments:(a) generation the NumPy array representing the current generation of cells. (b) rule is the Dictionary defining the cellular automata rule.
def process(generation, rule):
    new_generation = []
# It creates an empty list to store the new generation.
    for i, cell in enumerate(generation):
# It iterates through each cell in the generation.
        neighbours = []
# For each cell, it identifies its neighbors based on its position (edge cells have wraparound neighbors). 
        if i == 0:
# if i == 0:: This checks if the current cell index (i) is 0. In cellular automata, cells are often indexed starting from 0. So, i == 0 indicates that we're dealing with the first cell in the grid.
            neighbours = [generation[len(generation) - 1], cell, generation[1]]
# neighbours = [...]: If the condition is true (i.e., the cell is at the edge), this line assigns a list of neighboring cells to the variable neighbours. This list will be used to determine the next state of the cell.        
#generation[len(generation) - 1]: This refers to the last cell in the current generation. Since indexing starts from 0, this retrieves the element at index len(generation) - 1. This ensures the first cell considers the last cell in the wrap-around fashion (cyclic boundary conditions).
#cell: This refers to the current cell itself (cell). It's included in the neighborhood list.  
# generation[1]: This refers to the second cell in the current generation (index 1).  
        elif i == len(generation) - 1:
            neighbours = [generation[len(generation) - 2], cell, generation[0]]
        else:
            neighbours = [generation[i - 1], cell, generation[i + 1]]

        new_generation.append(rule[tuple(neighbours)])
# It creates a tuple representing the current state of the cell and its neighbors.It looks up the new state for this combination in the rule dictionary. It appends the new state for the cell to the new generation list.
    return new_generation
# It returns the new generation list.


# The function converts a rule number into a rule dictionary.It takes one argument "rule" the integer representing the rule number.
def generate_rule(rule):
    rule_str = format(rule, '08b')       
# It converts the rule number to a binary string.(a)format() is a built-in Python function used for string formatting.(b)rule  is the integer value representing the cellular automata rule.(c) '08b'is the format specifier that tells format() how to convert the integer. Here's the breakdown:(c1) 0 specifies that zeros should be padded before the number (if necessary) to create a specific string length.(c2) 8 specifies the minimum total width of the output string (here, 8).(c4) b specifies that the number should be converted to binary (base 2) representation.
    rule = {
        (1, 1, 1): int(rule_str[0]), 
#(a)(1,1,1):,This part is used to indicate a relationship with the substring of a generation that uses three 1's.(b) rule_str[0] refers to the first character of the binary string representation of the rule_str.(c)int(rule_str[0]), This converts the first character (which should be a binary digit, '0' or '1') to an integer (0 or 1).
        (1, 1, 0): int(rule_str[1]),
        (1, 0, 1): int(rule_str[2]),
        (1, 0, 0): int(rule_str[3]),
        (0, 1, 1): int(rule_str[4]),
        (0, 1, 0): int(rule_str[5]),
        (0, 0, 1): int(rule_str[6]),
        (0, 0, 0): int(rule_str[7])
    }
# It creates a dictionary that maps specific combinations of neighbor states (represented as tuples) to new cell states based on the binary representation of the rule number.
    return rule

# This function is the entry point of the program.
def main():
    fasta_filename = str(input("enter the txt file address of the gene sequance :"))
    first_row = read_fasta_file(fasta_filename)
    n_cells = len(first_row)
    n_generations = 999
    rule = 84 #184
    rule = generate_rule(rule)
    initialize(first_row, n_cells, n_generations, rule)

if __name__ == '__main__':
    main()
