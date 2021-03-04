import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_txt = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                  prompt="What's another state's name?").title()
    data = pd.read_csv('50_states.csv')
    state_list = data["state"].to_list()

    # Exit functionality
    if answer_txt == "Exit":
        break

    # If state is present in state list
    if answer_txt in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        guessed_states.append(answer_txt)
        state = data[data.state == answer_txt]
        new_x = int(state.x)
        new_y = int(state.y)
        t.penup()
        t.goto(new_x, new_y)
        t.write(answer_txt)

# States not guessed
not_guessed_states = [state for state in state_list if state not in guessed_states]

df = pd.DataFrame(not_guessed_states)
df.to_csv("To_learn.csv")
