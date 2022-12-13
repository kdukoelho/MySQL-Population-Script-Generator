import json

# Reading the JSON file
with open("data.json", encoding='utf-8') as json_file:
    data = json.load(json_file)
data_len = len(data)

# Database table variables
to_insert_table = "clientes"
fields = "(nome, endereco, email, num_contato)"

# Building SQL insert query
mysql_string = f"INSERT INTO {to_insert_table}{fields} VALUES"

count = 0
for people in data:
    count += 1
    # Getting the data from JSON file
    name = people["nome"]
    address = f'{people["bairro"]}, {people["endereco"]}, {people["numero"]}'
    email = people["email"]
    phone_number = str(people["celular"]).replace(" ", "")
    # Adding data at SQL insert query
    mysql_string += f'\n("{name}", "{address}", "{email}", "{phone_number}"),' \
                    if count < data_len else \
                    f'\n("{name}", "{address}", "{email}", "{phone_number}");'
    mysql_string = mysql_string.replace("'", "")

# Writing the query file
with open("generated_code.sql", "w") as to_write_file:
    to_write_file.write(mysql_string)
