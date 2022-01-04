# Stone-Chalenge

This algorithm was created to resolve a Stone challenge.

### Installation and usage
To run the code, you need to set up these variables on `main.py`:

| Name | Description                              | Type |
|---|------------------------------------------|------|
| people_names | Array of strings to save the people name | list |
| input_values | Array of dicts. Each dict represents an expense| list |

You also need to install the project dependencies. You can find it on <b>requirements.txt</b>.
To install the dependencies, run:
```
$ pip3 install -r requirements.txt
```

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

### Unit test

Unit tests can be founded on `test.py`. You can run it with the following command:
```
$ pytest test.py
```
