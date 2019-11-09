import sqlite3


def sqlite3_create_db():
    con = sqlite3.connect('sqlite3_base.db')

    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS core_fes(Well TEXT,'
                'Sample TEXT,'
                'Porosity REAL,'
                'Swr FLOAT,'
                'Permeability FLOAT)')

    cur.execute('INSERT INTO core_fes VALUES("Yellow snake creek", "Sample #666", 25.5, 34, 16)')

    data1 = ["Green snake creek", "Sample #111", 12, 44, 11]
    data2 = ["Blue snake creek", "Sample #123", 90, 60, 90]
    cur.execute('INSERT INTO core_fes VALUES(?, ?, ?, ?, ?)', data1)
    cur.execute('INSERT INTO core_fes VALUES(?, ?, ?, ?, ?)', data2)
    con.commit()
    cur.close()
    con.close()


def print_data_2d(columns_names, data):
    print(columns_names)
    for row in data:
        print(row)


def sqlite3_data_read_db(data_base, table, column_name=None):
    con = sqlite3.connect(data_base)
    cur = con.cursor()

    query_columns = f'pragma table_info({table})'
    cur.execute(query_columns)

    columns_description = cur.fetchall()
    columns_names = []
    for column in columns_description:
        columns_names.append(column[1])

    if column_name is None:
        query = f'SELECT * FROM {table}'
        cur.execute(query)
        data = cur.fetchall()
    else:
        query = f'SELECT {column_name} FROM {table}'
        cur.execute(query)
        data = cur.fetchall()
        new_data = []
        for element in data:
            new_data.append(element[0])

        data = new_data
        del new_data
        cur.close()
        con.close()
    print_data_2d(columns_names, data)


def sqlite3_delete_table(data_base, table):
    con = sqlite3.connect(data_base)
    cur = con.cursor()

    query = f'DROP TABLE IF EXISTS {table}'
    cur.execute(query)
    cur.close()
    con.close()


def sqlite3_delete_record(data_base, table, id_column, record_id):
    con = sqlite3.connect(data_base)
    cur = con.cursor()

    query = f"DELETE FROM {table} WHERE {id_column} = '{record_id}'"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()


def sqlite3_update_record(data_base, table, id_column, record_id, param_column, param_val):
    con = sqlite3.connect(data_base)
    cur = con.cursor()

    query = f"UPDATE {table} SET {param_column} = {param_val} WHERE {id_column} = '{record_id}'"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()


data_base = 'sqlite3_base.db'
table = 'core_fes'
id_column = 'Sample'
record_id = 'Sample #111'
param_column = 'Porosity'
param_val = 7

# sqlite3_example_create_db()
sqlite3_data_read_db(data_base, table)
# sqlite3_delete_table(data_base, table)
# sqlite3_delete_record(data_base, table, id_column, record_id)
sqlite3_update_record(data_base, table, id_column, record_id, param_column, param_val)

