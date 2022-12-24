import pandas as pd
import turtle as t

def main():
    #screen setup
    screen=t.Screen()
    screen.title('U.S.States Quiz')
    image='.\\projects\\us-states-game-start\\blank_states_img.gif'
    screen.addshape(image)
    t.shape(image)

    #reading csv
    data=pd.read_csv('.\\projects\\us-states-game-start\\50_states.csv')
    states=data.state.to_list()

    guessed_states=[]
    #user input answer_state
    while len(guessed_states)<50:
        answer_state=screen.textinput(title=f'{len(guessed_states)}/50 States Correct',prompt="Whats another state's name--").title()

        if answer_state in states:
            tom=t.Turtle()
            tom.hideturtle()
            tom.penup()
            state_data=data[data.state==answer_state]
            tom.goto(int(state_data.x),int(state_data.y))
            tom.write(answer_state)
            guessed_states.append(answer_state)

        elif answer_state=='Exit':
            #states not guessed by the user
        

            missing_states=[i for i in states if i not in guessed_states]

            new_data=pd.DataFrame(missing_states)
            new_data.to_csv('.\\projects\\us-states-game-start\\missing_states.csv')
            break



if __name__=='__main__':
    main()