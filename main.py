from expense import Expense
from utils.functions import calculate_expenses

expenditure = list()

# List of people
people_names = ["Thalixo", "Trindadé", "Jhol pow pow", "Ita pou pou"]

# This variable is an array of dicts. Each dict represents an expense.
input_values = [{"nome": "Passeio de escuna", "quantidade": 5, "valor_unitario": "R$ 80,33"},
                {"nome": "Diária do hotel", "quantidade": 3, "valor_unitario": "R$ 337,33"},
                {"nome": "Almoço self-service", "quantidade": "0,757", "valor_unitario": "R$ 45,33"}]


if len(people_names) == 0:
    print("Sem dados sobre as pessoas. Programa encerrado.")
    exit()

if len(input_values) == 0:
    print("Sem dados de despezas. Programa encerrado.")
    exit()

# Here we are creating an Expense object.
for item in input_values:
    expenditure.append(Expense(item["nome"], item["quantidade"], item["valor_unitario"]))

# Generating results.
data = calculate_expenses(expenditure, people_names)
print(data)
