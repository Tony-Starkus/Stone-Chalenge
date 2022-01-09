
def format_price(value: float):
    """
    Format the price to brazillian format. Ex: R$ 1,00
    :param value: a dict with the name or the person and the value to pay
    :return: Formated price string
    """
    return "R$ {:.2f}".format(value / 100).replace(".", ",")


def show_expenditure(values: dict) -> None:
    """

    :param values:
    :return:
    """
    for key, value in values.items():
        print("------------\n"
              f"{key}: {format_price(value)}")


def calculate_expenses(expenditure_list: list, people: list) -> dict:
    """
    THis function sum the expenditure and create a dict.
    The dict keys are the people name, and the value is the expense that the person is going to pay
    :param expenditure_list: list os expense objects
    :param people: list of string that represents the name of a person.
    :return: A dict. The key is the person name, and value is the price of expense to pay
    """
    response = dict()
    person_quantity = len(people)

    for expense in expenditure_list:
        total = expense.price * expense.quantity  # total of expense
        value_to_pay = total / person_quantity  # price tha each person is going to pay
        rest = total % person_quantity  # Check if the expense total can be divided equally.

        for index, person in enumerate(people):
            if str(person) in response:
                response.update({str(person): value_to_pay + response[person]})
            else:
                response.update({str(person): value_to_pay})

            if index == (len(people) - 1) and rest != 0:
                # If this person is the last one, and there is rest in the expense, the rest go to this person
                response.update({str(person): response[person] + rest})

    # Check if last person value is greater than others
    rebalance = round((list(response.values())[-1] / 100) - (list(response.values())[0] / 100), 2)
    if rebalance > 0.01:
        while rebalance > 0.01:
            for key in response.keys():
                response[str(key)] = response[str(key)] + 1  # Add R$ 0,01 to this key

                # Remove R$ 0,01 from last person
                response[str(list(response.keys())[-1])] = response[str(list(response.keys())[-1])] - 1
                rebalance = rebalance - 0.01
                if rebalance == 0.01:
                    break
            if rebalance == 0.01:
                break
    show_expenditure(response)
    return response
