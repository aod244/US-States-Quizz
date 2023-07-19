import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess_states = 0
guess_states_list = []
states_data = pandas.read_csv("50_states.csv")
while guess_states < 50:
    answer_state = screen.textinput(title=f"{guess_states}/50 States Correct", prompt="What's another state name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if states_data[states_data.state == answer_state].empty:
        pass
    else:
        this_state = states_data[states_data.state == answer_state]
        x_cor = int(this_state['x'].to_string(index=False))
        y_cor = int(this_state['y'].to_string(index=False))
        write_turtle = turtle.Turtle()
        write_turtle.hideturtle()
        write_turtle.penup()
        write_turtle.setposition(x_cor, y_cor)
        write_turtle.write(f"{answer_state}", False, 'left')
        guess_states += 1
        guess_states_list.append(answer_state)

state_to_learn = states_data[~states_data['state'].isin(guess_states_list)]
state_to_learn_list = state_to_learn.state.tolist()
data_frame = pandas.DataFrame(state_to_learn_list)
data_frame.to_csv('states_to_learn.csv')
