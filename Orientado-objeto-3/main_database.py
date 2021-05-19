"""
public, protected, private
"""


class Database:
    def __init__(self):
        self._data = {}

    def insert_client(self, id_client, name_client):
        if 'clientes' not in self._data:
            self._data['clientes'] = {id_client: name_client}
        else:
            self._data['clientes'].update({id_client: name_client})

    def list_customers(self):
        for id_client_dict, name_client_dict in self._data['clientes'].items():
            print(id_client_dict, name_client_dict)

    def delete_client(self, id_client):
        del self._data['clientes'][id_client]


database_test = Database()
database_test.insert_client(1, 'Joamir')
database_test.insert_client(2, 'Moraes')
database_test.insert_client(3, 'Silveira')
database_test.list_customers()

print(database_test._data)
