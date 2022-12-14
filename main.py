import json
from random import randint, uniform

# Reading the JSON file
with open("data.json", encoding='utf-8') as json_file:
    data = json.load(json_file)
data_len = len(data)

# Database table variables
to_insert_table = "pedido_has_vegetais"
fields = "(id_pedido, id_vegetal, qtd_kg)"

# Building SQL insert query
insert_string = f"INSERT INTO {to_insert_table}{fields} VALUES"


def to_register_people():

    count = 0
    for people in data:
        count += 1
        # Getting the data from JSON file
        name = people["nome"]
        address = f'{people["bairro"]}, {people["endereco"]}, {people["numero"]}'
        email = people["email"]
        phone_number = str(people["celular"]).replace(" ", "")
        # Adding data at SQL insert query
        mysql_string = insert_string + f'\n("{name}", "{address}", "{email}", "{phone_number}"),' \
                                       if count < data_len else \
                                       f'\n("{name}", "{address}", "{email}", "{phone_number}");'
        mysql_string = mysql_string.replace("'", "")
        return mysql_string


def to_register_requests():
    mysql_string = insert_string
    for cliente in range(1, 16):
        id_pedido = cliente
        already_bought_vegetables = []
        pedido = range(1, randint(3, 12))
        for item_pedido in pedido:
            to_buy_vegetable = randint(1, 14)
            if to_buy_vegetable not in already_bought_vegetables:
                already_bought_vegetables.append(to_buy_vegetable)
            else:
                to_buy_vegetable = randint(1, 14)
            mysql_string += f'\n("{id_pedido}", "{to_buy_vegetable}", "{float(str(uniform(0.0, 2.5))[0:4])}"),'
    mysql_string = mysql_string[:-1] + ";"
    return mysql_string


# Writing the query file
with open("generated_code.sql", "w") as to_write_file:
    to_write_file.write(str(to_register_requests()))
