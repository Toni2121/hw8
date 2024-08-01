def my_ascending(a: int = 0, b: int = 0) -> None:
    if a > b:
        print(b, a)
    else:
        print(a, b)

    """
    gets two int parameters and print them in ascending order
    """

def my_details(str1: str = "") -> None:
    middle_letter = len(str1) // 2
    letters = [str1[0], str1[-1]] + ([str1[middle_letter - 1:middle_letter + 1]] if len(str1) % 2 == 0 else [str1[middle_letter]])
    print(letters)
    """
    gets a string and prints the first letter, the middle letter and the last letter of the string
    """

def bool_say(bool1: bool = None) -> None:
    if bool1 == True:
        print("yes")
    else:
        print("no")
    """
    gets a boolean and checks whether its value is True or False and gets a print accordingly
    """


def print_zugi(list1: list[int] = []) -> None:
    if not list1:
        print("empty list")
        return
    print(["even" if num % 2 == 0 else "odd" for num in list1])
    """
    gets a list of integers and prints whether the number (inside the list) is odd or even
    """


def my_statistics(grades: list[int] = []) -> None:
    if not grades:
        print("empty list")
        return
    highest_grade = max(grades)
    lowest_grade = min(grades)
    amount_grades = len(grades)
    avg = sum(grades) / amount_grades
    excellent_count = sum(1 for grade in grades if grade > 90)
    failing_count = sum(1 for grade in grades if grade < 55)
    print(f"The highest garde is: {highest_grade}")
    print(f"The lowest garde is: {lowest_grade}")
    print(f"Amount םf grades entered:{amount_grades}")
    print(f"The average grade is: {avg}")
    print(f"Amount of excellent grades: {excellent_count}")
    print(f"Amount of failing grades: {failing_count}")
    """
    gets grades and print the highest grade, the lowest one, amount of grades and the average.
    and check how many excellent grades there are and how many failing grades there are.
    """

print(help(my_ascending()))
print(help(bool_say()))
print(help(print_zugi()))
print(help(my_statistics()))