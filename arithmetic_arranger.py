def arithmetic_arranger(problems, show=True):

    answer = ""
    arranged_problems = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        first_number = problem.split(" ")[0]
        second_number = problem.split(" ")[2]
        operator = problem.split(" ")[1]

        if not ((operator == "+") or (operator == "-")):
            return "Error: Operator must be '+' or '-'."

        if not int(first_number) or not int(second_number):
            return "Error: Numbers must only contain digits."

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            answer = str(int(first_number) + int(second_number))
        elif operator == "-":
            answer = str(int(first_number) - int(second_number))

        width = max(int(len(first_number)), int(len(second_number))) + 2
        dashes = "-" * width
        spaces = "    "

        line1 = str(first_number).rjust(width) + spaces
        line2 = operator + str(second_number).rjust(width - 1) + spaces
        line3 = dashes + spaces
        line4 = answer.rjust(width) + spaces

        if show:
            arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        else:
            arranged_problems = line1 + "\n" + line2 + "\n" + line3

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
