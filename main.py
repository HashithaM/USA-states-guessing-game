import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # ######################################
guessed_states = []
missing_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states name ?").title()
    print(answer_state)
    if answer_state == "Exit":
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states] # ###################### list comprehension
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())  # I can't understand the .item() function #####################
        guessed_states.append(answer_state)



# with open("./weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("./weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv") ###########################################

# print(type(data))
# print(data)
# print(data["temp"])
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
# print(type(data_dict['temp'][1]))

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(round(data["temp"].mean(), 2))
# print(data["temp"].max())

# print(data.condition)
# print(data["condition"])

# print(data[data.day == "Monday"])
# print(data[data.temp == 12])
# print(data[data.temp == data.temp.max()])
# print(data[data.condition == 'Sunny'])
# print(type(data[data.condition == 'Sunny']))
# print(len(data[data.condition == 'Sunny']))
# print(data["temp"])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# print(data[data.day == "Monday"].condition)

# monday_temperature = int(data[data.day == "Monday"].temp)
# monday_temp_f = monday_temperature * 9/5 + 32
# print(monday_temp_f)

# tuesday_temperature = int(data[data.day == "Tuesday"].temp)
# tuesday_temp_f = tuesday_temperature * 9/5 + 32
# print(tuesday_temp_f)

# Crate a dataframe from scratch

# import pandas
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)  # ############################################################
# data.to_csv("new_data.csv")
# print(data)

# import pandas
# data = pandas.read_csv("squirrel_data.csv")

# num_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# print(num_black_squirrels)
# num_gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# print(num_gray_squirrels)
# num_cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(num_cinnamon_squirrels)

# data_dic = {
#     "Color": ["Black", "Gray", "Cinnamon"],
#     "Count": [num_black_squirrels, num_gray_squirrels, num_cinnamon_squirrels]
# }

# new_data = pandas.DataFrame(data_dic)  # ###############################################
# new_data.to_csv("squirrel_count.csv")  # #################################################################

