from product import Expense


def show_expenditure(values: list) -> None:
    for data in values:
        print("------------\n"
              f"Nome: {data.get('name')}\n"
              f"Preço: {data.get('value')}")


def format_price(value: float):
    """
    Show the result
    :param value: a dict with the name or the person and the value to pay
    :return: None
    """
    return "R$ {:.2f}".format(value / 100).replace(".", ",")


def calculate_expenses(expenditure_list: list, people: list):
    response = list()
    person_quantity = len(people)

    for expense in expenditure_list:
        value_to_pay = (expense.price * expense.quantity) / person_quantity

        for person in people:
            response.append({"name": person, "value": format_price(value_to_pay)})

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

expenditure = list()
person_names = ["Thalixo", "Trindadé", "Jhol pow pow", "Ita pow pow"]
for item in lista:
    expenditure.append(Expense(item["nome"], item["quantidade"], item["valor_unitario"]))

calculate_expenses(expenditure, person_names)
