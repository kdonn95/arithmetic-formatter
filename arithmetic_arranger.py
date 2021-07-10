def arithmetic_arranger(problems, show=None):

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    answer = ""
    arranged_problems = ""

    # maximum number of problems is 5
    if len(problems) > 5:
        return "Error: Too many problems."

    # splitting up the given string
    for problem in problems:
        first_number = problem.split(" ")[0]
        second_number = problem.split(" ")[2]
        operator = problem.split(" ")[1]

        # only accepts addition and subtraction
        if not ((operator == "+") or (operator == "-")):
            return "Error: Operator must be '+' or '-'."

        # only accepts digits of length <= 4
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # doing required sums
        if operator == "+":
            answer = str(int(first_number) + int(second_number))
        elif operator == "-":
            answer = str(int(first_number) - int(second_number))

        # formatting answer as per requirements
        width = max(int(len(first_number)), int(len(second_number))) + 2
        dashes = "-" * width
        spaces = "    "

        line1 += str(first_number).rjust(width)
        line2 += operator + str(second_number).rjust(width - 1)
        line3 += dashes
        line4 += answer.rjust(width)

        # adds spaces at the end of each digit/character except last (as per requirements)
        if problem in problems[:-1]:
            line1 += spaces
            line2 += spaces
            line3 += spaces
            line4 += spaces

        # shows answer if required
        if show:
            arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        else:
            arranged_problems = line1 + "\n" + line2 + "\n" + line3

    return arranged_problems
