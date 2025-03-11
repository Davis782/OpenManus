import pandas as pd
from taipy.gui import Gui
# import taipy as tp

# Data model for a to-do item


class Todo:
    def __init__(self, task, done=False):
        self.task = task
        self.done = done

    def __repr__(self):  # for debugging purposes
        return f"Todo(task='{self.task}', done={self.done})"


# List to store to-do items
todos = []

# Function to add a new task


def add_todo(state):
    new_todo = Todo(state.new_task)
    state.todos.append(new_todo)
    state.new_task = ""
    update_dataframe(state)

# Function to toggle the state of a todo


def toggle_todo(state, var_name, id, action):
    state.todos[id].done = not state.todos[id].done
    update_dataframe(state)

# Function to update the dataframe


def update_dataframe(state):
    data = [{"Task": todo.task, "Done": todo.done} for todo in state.todos]
    state.df = pd.DataFrame(data)


# Initial dataframe
data = [{"Task": todo.task, "Done": todo.done} for todo in todos]
df = pd.DataFrame(data)

# Taipy GUI definition
gui_layout = """
< | {df} | table | on_action = toggle_todo | not editable = True | >

New task: < | {new_task} | text | label = "Task name" | >
< | Add | button | on_action = add_todo | >
"""

# Create the GUI
gui = Gui(gui_layout)

# Initialize the state
gui.state.todos = todos
gui.state.df = df
gui.state.new_task = ""

# Run the GUI
gui.run()
