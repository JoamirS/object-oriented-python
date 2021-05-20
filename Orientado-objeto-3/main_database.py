"""
public, protected, private
"""


class Database:
    def __init__(self):
        self.__data = {}

    @property
    def get_data(self):
        return self.__data

    def insert_client(self, id_client, name_client):
        if 'clientes' not in self.__data:
            self.__data['clientes'] = {id_client: name_client}
        else:
            self.__data['clientes'].update({id_client: name_client})

    def list_customers(self):
        for id_client_dict, name_client_dict in self.__data['clientes'].items():
            print(id_client_dict, name_client_dict)

    def delete_client(self, id_client):
        del self.__data['clientes'][id_client]


database_test = Database()
database_test.insert_client(1, 'Joamir')
database_test.insert_client(2, 'Moraes')
database_test.insert_client(3, 'Silveira')
database_test.list_customers()
print(database_test.get_data)


