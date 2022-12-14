import json
from random import randint, uniform
from datetime import date

# Reading the JSON file
with open("data.json", encoding='utf-8') as json_file:
    data = json.load(json_file)
data_len = len(data)


def to_register_people():
    mysql_query_string = "INSERT INTO clientes(nome, endereco, email, num_contato) VALUES"
    count = 0
    for costumer in data:
        count += 1
        # Getting the data from JSON file
        name = costumer["nome"]
        address = f'{costumer["bairro"]}, {costumer["endereco"]}, {costumer["numero"]}'
        email = costumer["email"]
        phone_number = str(costumer["celular"]).replace(" ", "")
        # Adding data at SQL insert query
        mysql_query_string += f'\n("{name}", "{address}", "{email}", "{phone_number}"),'
    mysql_query_string = mysql_query_string.replace("'", "")
    mysql_query_string = mysql_query_string[:-1] + ";"
    return mysql_query_string


def to_register_order():
    mysql_query_string = "INSERT INTO pedido(id_cliente, data_pedido, data_agendada_entrega, data_efetiva_entrega)" \
                         " VALUES"
    today = date.today()
    for costumer_enum in data:
        order_date = date.fromordinal(today.toordinal() - randint(1, 120))
        scheduled_delivery_date = date.fromordinal(order_date.toordinal() + randint(1, 15))
        if scheduled_delivery_date.month < 12:
            effective_delivery_date = f'"{date.fromordinal(scheduled_delivery_date.toordinal() + randint(0, 3))}"'
        else:
            effective_delivery_date = "NULL"
        mysql_query_string += f'\n("{costumer_enum}", "{order_date}", "{scheduled_delivery_date}", ' \
                              f'{effective_delivery_date}),'
    mysql_query_string = mysql_query_string[:-1] + ";"
    return mysql_query_string


def to_register_order_has_vegetable():
    mysql_query_string = "INSERT INTO pedido_has_vegetais(id_pedido, id_vegetal, qtd_kg) VALUES"
    for costumer_enum in data:
        order_id = costumer_enum  # Assigning an order to each people in data.json.
        already_bought_vegetables = []
        order = range(1, randint(3, 12))  # Defining the amount of vegetables to buy.
        for _ in order:
            to_buy_vegetable = randint(1, 14)  # Defining the vegetables id.
            if to_buy_vegetable not in already_bought_vegetables:
                already_bought_vegetables.append(to_buy_vegetable)
            else:
                to_buy_vegetable = randint(1, 14)
            mysql_query_string += f'\n("{order_id}", "{to_buy_vegetable}", "{float(str(uniform(0.0, 2.2))[0:4])}"),'
    mysql_query_string = mysql_query_string[:-1] + ";"
    return mysql_query_string


# Writing the query file
with open("generated_code.sql", "w") as to_write_file:
    to_write_file.write(str(to_register_people()))
