# Stone-Chalenge

This algorithm was created to resolve a Stone' challenge.

To run the code, you need to set up these variables:

| Name | Description                              | Type |
|---|------------------------------------------|------|
| people_names | Array of strings to save the people name | list |
| input_values | Array of dicts. Each dict represents an expense| list |

### Expense
An expense dict has 3 values

| Name | Description                   | Type                        |
|---|-------------------------------|-----------------------------|
| nome | Name of expense               | list                        |
| quantidade | The expense quantity          | string or number            |
| valor_unitario | The expense value of one item | string formated in BR price |

#### Expense Example
```
    {
        "nome": "Passeio de escuna",
        "quantidade": 5,
        "valor_unitario": "R$ 80,00"
    }
```
