import sqlite3

def import_pict_binary(pict_path):
    with open(pict_path, 'rb') as f:
        return f.read()


def sqlite3_pict_import(data_base, table, pict_path):
    con = sqlite3.connect(data_base)
    cur = con.cursor()

    query_creation = f"CREATE TABLE IF NOT EXISTS {table}(id TEXT, description TEXT, path TEXT, data BLOB)"
    cur.execute(query_creation)
    binary_pict = import_pict_binary(pict_path)
    data = ('1', "my first imported picture", pict_path, binary_pict)
    query = f"INSERT INTO {table} VALUES(?, ?, ?, ?)"
    cur.execute(query, data)
    con.commit()
    cur.close()
    con.close()

def write_pict_from_binary(file_path, pict_binary):
    with open(file_path, 'wb') as f:
        f.write(pict_binary)

def sqlite3_read_pict_from_db(data_base, table, id):
    con = sqlite3.connect(data_base)
    cur = con.cursor()

    query = f"SELECT data, path FROM {table} WHERE id = '{id}'"
    cur.execute(query)
    record = cur.fetchone()
    pict_binary = record[0]
    pict_path_init = record[1]
    new_path = "//home//alex//PycharmProjects//owl_from_db.png"
    write_pict_from_binary(new_path, pict_binary)
    return pict_binary


data_base = "sqlite3_pict_db.db"
table = "table_with_pic"
pict_path = "owl.png"
id = '1'

sqlite3_pict_import(data_base, table, pict_path)
sqlite3_read_pict_from_db(data_base, table, id)


