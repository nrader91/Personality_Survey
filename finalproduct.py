import webbrowser as wb


show = input("What's your favorite TV show?")

if show == "The Office":
    print("Bears, Beets, Battlestar Galactica.")
    wb.open("https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.wikia.nocookie.net%2Ftheoffice%2Fimages%2Fc%2Fc5%2FDwight_.jpg%2Frevision%2Flatest%3Fcb%3D20170701082424&imgrefurl=https%3A%2F%2Ftheoffice.fandom.com%2Fwiki%2FDwight_Schrute&tbnid=1iVvEoIvxMf-3M&vet=12ahUKEwjD0tKq4Lv0AhUmHjQIHUcOA64QMygAegUIARDUAQ..i&docid=-BkPs_4oWMVQRM&w=2249&h=3000&q=the%20office%20dwight&ved=2ahUKEwjD0tKq4Lv0AhUmHjQIHUcOA64QMygAegUIARDUAQ")

elif show == "Breaking Bad":
    print("You know my name... Heisenburg")

elif show == "The Flash":
    print("I hear that's a great one, but I haven't seen it yet.")

else:
    print("Your favorite show is " + show) 


food = input("What's your favorite food?")

if food == "pasta":
    print("I like pasta too.")

elif food == "sushi":
    print("Sushi is my favorite!")

else:
    print("You like to eat " + food)


