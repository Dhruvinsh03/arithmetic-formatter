def arithmetic_arranger(problems, show_answers=False):
  arranged_problems = []
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    operands = problem.split()
    num1 = operands[0]
    operator = operands[1]
    num2 = operands[2]
    # ...rest of the code
    if len(num1) > 4 and len(num2) > 4:
      print("Error: Numbers cannot be more than four digits.")
    if operator == "+":
      result = int(num1) + int(num2)
    elif operator == "-":
      result = int(num1) - int(num2)
    else:
      print("Error: Operator must be '+' or '-'.")
    width = max(len(num1), len(num2)) + 2
    line1 = num1.rjust(width)
    line2 = operator + num2.rjust(width - 1)
    line3 = "-" * width

    problems.append([line1, line2, line3])
  if show_answers:
    arranged_problems.append(str(result))

  return "\n".join(arranged_problems)
