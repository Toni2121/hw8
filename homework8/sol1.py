import func_without_return as fwr

fwr.my_ascending(-12, 7)

fwr.my_details("AI is the best")

fwr.bool_say(True)
fwr.bool_say(False)

fwr.print_zugi([5, 3, 2, 10, 15, 14, 14])

fwr.my_statistics([])
grades2 = []
while True:
    try:
        user_input = int(input("Please enter a grade (enter -99 to exit): "))
    except Exception as e:
        print(f"Something went wrong ---{e}--- try again")
        continue

    if user_input == -99:
        break
    if 0 <= user_input <= 100:
        grades2.append(user_input)
        print(grades2)
    else:
        print("Grade must be between 0 and 100. Try again.")
        continue
fwr.my_statistics(grades2)

