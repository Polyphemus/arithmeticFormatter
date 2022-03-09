import re

def arithmetic_arranger(problems, answers=False):
    # User errors:
    if len(problems) > 5:
        return 'Error: Too many problems.'

    problemsRegex = re.compile(r'(\d+) ([\+-]) (\d+)')
    problemsLoL = []

    for prob in problems:
        if '*' in prob or '/' in prob:
            return "Error: Operator must be '+' or '-'."  # must use double quotes b/c single quotes in text
        if re.search('[a-zA-Z]', prob):
            return 'Error: Numbers must only contain digits.'
        # if prob.upper().isupper() # converts all alpha chars to upper, returns true if all upper
        # stackoverflow says this would be faster but need to practice regex
        # https://stackoverflow.com/questions/9072844/how-can-i-check-if-a-string-contains-any-letters-from-the-alphabet
        # TODO add list of digits/operators to list of lists
        mo = problemsRegex.search(prob)
        if len(mo.group(1)) > 4 or len(mo.group(3)) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        problemsLoL.append([mo.group(1), mo.group(2), mo.group(3), max(len(mo.group(1)), len(mo.group(3)))+2, str(eval(mo.group(1) + mo.group(2) + mo.group(3)))])

    print(problemsLoL)

    arranged_probList = []
    for probs in problemsLoL:
        arranged_probList.append(" "*(probs[3] - len(probs[0])))
        arranged_probList.append(probs[0])
        arranged_probList.append("    ")

    arranged_probList[len(arranged_probList)-1] = "\n"

    for probs in problemsLoL:
        arranged_probList.append(probs[1])
        arranged_probList.append(" "*(probs[3] - len(probs[2]) - 1))
        arranged_probList.append(probs[2])
        arranged_probList.append("    ")

    arranged_probList[len(arranged_probList) - 1] = "\n"

    for probs in problemsLoL:
        arranged_probList.append("-"*probs[3])
        arranged_probList.append("    ")

    arranged_probList[len(arranged_probList) - 1] = "\n"

    if answers:
        for probs in problemsLoL:
            arranged_probList.append(" "*(probs[3] - len(probs[4])))
            arranged_probList.append(probs[4])
            arranged_probList.append("    ")

    arranged_probList[len(arranged_probList) - 1] = ""

    # print(arranged_probList)

    arranged_problems = ''.join(arranged_probList)
    # print(arranged_problems)
    return arranged_problems