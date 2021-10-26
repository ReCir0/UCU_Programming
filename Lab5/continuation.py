def calculate_expression(expression):
    '''
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    '''
    try:
        numbers = []
        actions = []
        expression = expression[13:len(expression)]
        i = 0
        num_1 = ""

        while True:
            if expression[i] == "?":
                return int(num_1)
            if expression[i] == " ":
                break
            num_1 += expression[i]
            i += 1
        expression = expression[len(num_1) + 1:len(expression)]
        num_1 = int(num_1)
        numbers.append(num_1)

        while True:
            i = 0
            action = ""
            while True:
                if expression[i] == " ":
                    if expression[i + 1] != "н":
                        break
                action += expression[i]
                i += 1
            actions.append(action)
            expression = expression[len(action) + 1:len(expression)]

            i = 0
            num_2 = ""
            while expression[i] != " " and expression[i] != "?":
                num_2 += expression[i]
                i += 1
            numbers.append(int(num_2))
            if expression[i] == " ":
                expression = expression[len(num_2) + 1:len(expression)]
            else:
                break

        result = numbers[0]
        len_actions = len(actions)
        for i in range(len_actions):
            if actions[i] == "плюс" or actions[i] == "додати":
                result = result + numbers[i + 1]
            elif actions[i] == "мінус" or actions[i] == "відняти":
                result = result - numbers[i + 1]
            elif actions[i] == "помножити на":
                result = result * numbers[i + 1]
            elif actions[i] == "поділити на":
                if result % numbers[i + 1] == 0:
                    result = int(result / numbers[i + 1])
                else:
                    result = result / numbers[i + 1]
            else:
                return 'Неправильний вираз!'

        return result
    except:
        return 'Неправильний вираз!'

print(calculate_expression('Скільки буде 10 розділити на 2?'))