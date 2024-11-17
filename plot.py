from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random

# api to plot dynamically 3 rgb lines on a graph with the history of the plot from the last 1000 rolling operations

# create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1000)
ax.set_ylim(0, 255)
ax.set_title('RGB values')
ax.set_xlabel('Time')
ax.set_ylabel('Value')

# create a list to store the history of the plot
history = [[], [], []]

# create 3 lines
lines = [ax.plot([], [])[0] for _ in range(3)]
# assing colors 
lines[0].set_color('red')
lines[1].set_color('green')
lines[2].set_color('blue')

# display the plot

# create a function to update the plot
def update_plot(r,g,b):
    global history
    global lines

    # append the new values to the history
    history[0].append(r)
    history[1].append(g)
    history[2].append(b)

    # update the data of the lines
    for i, line in enumerate(lines):
        line.set_data(range(len(history[i])), history[i])

    # update the limits of the plot
    ax.set_xlim(0, len(history[0]))
    ax.set_ylim(0, 255)

    # return the lines
    return lines

# function tu update the plot whitout blocking th emain thread
def update_plot_non_blocking(r,g,b):
    # update the plot
    lines = update_plot(r,g,b)
    # draw the plot
    plt.draw()
    # pause to make the plot visible
    plt.pause(0.01)
    


