import re


class Expense:

    def __init__(self, name: str, quantity: str, price: int):
        self.__name = name
        self.__quantity = self.__parse_quantity__(quantity)
        self.__price = self.__parse_price__(price)

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price

    def __parse_quantity__(self, value: str):
        """
        This function check the instance of quantity and return an int or a float that represents the quantity
        of the expense.
        :param value: the quantity of the expense
        :return: a float or a int that represents the quantity of the expense
        """

        if type(value) in [int, float]:
            return value

        if "," in value:
            return float(value.replace(",", "."))
        else:
            return int(value)

    def __parse_price__(self, value: str):
        """
        This function converts the string price to number, removing all not numbers characters.
        :param value: price of expense
        :return: an integer that represents the price
        """
        return int(re.sub("[^0-9]", "", value))

    def __str__(self):
        return "------------\n" \
               f"Nome: {self.__name}\n" \
               f"Quantidade {self.__quantity}\n" \
               f"Preço: {self.__price}"
