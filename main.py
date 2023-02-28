import turtle
import pandas

data_provinces = pandas.read_csv("Provinces.csv")
my_screen = turtle.Screen()
my_screen.title("Việt Nam Provinces leanring")
image = "VietNam_map.gif"
my_screen.addshape(image)
turtle.shape(image)
my_screen.tracer(0)


print(data_provinces)
john = turtle.Turtle()
john.penup()
john.hideturtle()


print(data_provinces)
john = turtle.Turtle()
john.penup()
john.hideturtle()
is_guessed = []
province_guessed = 0
is_on = True
for provinces in data_provinces.Provinces:
    while is_on:
        answer = my_screen.textinput(
            f"Guess the state {province_guessed}/63", "What are another provinces?"
        )
        if answer in data_provinces.Provinces.to_list() and answer not in is_guessed:
            is_guessed.append(answer)
            new_x = int(data_provinces[data_provinces.Provinces == answer]["x"])
            new_y = int(data_provinces[data_provinces.Provinces == answer]["y"])
            john.goto(new_x, new_y)
            john.write(answer, font=("Arial", 7, "normal"))
            province_guessed += 1
        if answer == "Exit":
            learn = [
                province
                for province in data_provinces.Provinces
                if province not in is_guessed
            ]
            new_data = pandas.DataFrame(learn)
            is_on = False
            new_data.to_csv("learn.csv")
my_screen.exitonclick()
