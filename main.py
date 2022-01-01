from expense import Expense


def show_expenditure(values: dict) -> None:
    for key, value in values.items():
        print("------------\n"
              f"{key}: {format_price(value)}")


def format_price(value: float):
    """
    Format the price to brazillian format. Ex: R$ 1,00
    :param value: a dict with the name or the person and the value to pay
    :return: None
    """
    return "R$ {:.2f}".format(value / 100).replace(".", ",")


def calculate_expenses(expenditure_list: list, people: list):
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
        print(f"{total=}")
        print(f"{value_to_pay=}")
        print(f"{rest=}")

        for index, person in enumerate(people):
            if str(person) in response:
                response.update({str(person): value_to_pay + response[person]})
            else:
                response.update({str(person): value_to_pay})

            if index == (len(people) - 1) and rest != 0:
                # If this person is the last one, and there is rest in the expense, the rest go to this person
                response.update({str(person): response[person] + rest})
    print(response)
    show_expenditure(response)


lista = [
    {
        "nome": "Passeio de escuna",
        "quantidade": 5,
        "valor_unitario": "R$ 80,00"
    },
    {
        "nome": "Diária do hotel",
        "quantidade": 3,
        "valor_unitario": "R$ 337,99"
    },
    {
        "nome": "Almoço self-service",
        "quantidade": "0,757",
        "valor_unitario": "R$ 45,99"
    }
]

lista1 = [
    {
        "nome": "Almoço self-service",
        "quantidade": "1",
        "valor_unitario": "R$ 1,00"
    }
]

expenditure = list()
person_names = ["Thalixo", "Trindadé", "Jhol pow pow", "Ita pou pou"]
for item in lista:
    expenditure.append(Expense(item["nome"], item["quantidade"], item["valor_unitario"]))

calculate_expenses(expenditure, person_names)
