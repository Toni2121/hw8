def my_avg(a: int = 0, b: int = 0) -> float:
    avg1 = (a + b) / 2
    print(f"The average is: {avg1}")
    """
    gets two parameters and calculates its average
    """

def my_headline(str1: str = "") -> str:
    head1 = str1.upper()
    print(head1 + "!")
    print(head1 + "!")
    """
    gets a string and converts the letter to upper case and adds a exclamation mark at the end, prints twice
    """

def concat_list(list1: list[int] = [], list2: list[int] = [], list3: list[int] = []) -> list[int]:
    total_list = []
    total_list.extend(list1)
    total_list.extend(list2)
    total_list.extend(list3)
    print(total_list)
    print(len(total_list))
    return total_list

print(help(my_avg()))
print(help(my_headline()))
print(help(concat_list()))
"""
gets 3 list parameters and returns one with all of them combined in one list. prints the list and its length
"""

def bool_say(bool1: bool = None) -> str:
    if bool1 == True:
        print("yes")
        return str(bool1)
    else:
        print("no")
        return str(bool1)
    """
    gets a boolean and checks whether its value is True or False and gets a print accordingly and return it as a string
    """

def print_zugi(list1: list[int] = []) -> list[str]:
    if not list1:
        print("empty list")
        return list[str](list1)
    print(["even" if num % 2 == 0 else "odd" for num in list1])
    """
    gets a list of integers and prints whether the number (inside the list) is odd or even and returns it as a string
    """

def get_int(str1: str = "") -> int:
    while True:
        try:
            user_input: int = int(input(str1))
            if user_input is int:
                break
                return user_input
            else:
                return str(user_input)
                break
        except Exception as e:
            print(f"something went wrong ---{e}--- please try again")
            user_input: int = int(input(str1))
    """
    gets a string parameter, then gets an int input from the user and shows the string. function getting input all over
    again until it inputs an int
    """

# Ex 6

"""
if we print what we got from a function that has no return we will get None
if we print what we got from a function that has return None we will get None
both break and return allow us to exit either a loop or a conditional execution
"""