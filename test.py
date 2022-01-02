from expense import Expense
from main import calculate_expenses, format_price

test1 = {
    "people": ["João", "José", "Camila"],
    "expenditures": [
        {
            "nome": "Bombom",
            "quantidade": 1,
            "valor_unitario": "R$ 1,00"
        }
    ]
}


def test_test1():
    expenditure = list()
    for item in test1.get("expenditures"):
        expenditure.append(Expense(item["nome"], item["quantidade"], item["valor_unitario"]))

    response = calculate_expenses(expenditure, test1.get("people"))
    assert response.get("João") == 33.333333333333336
    assert response.get("José") == 33.333333333333336
    assert response.get("Camila") == 34.333333333333336
