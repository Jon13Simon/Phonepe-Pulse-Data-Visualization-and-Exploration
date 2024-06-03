import psycopg2


def connect_to_pg():
    mydb= psycopg2.connect(host= 'localhost',
                        user= 'postgres',
                        password= 'Joshie@0910',
                        database= 'phonepe_data',
                        port= '5432')
    return mydb

def close_pg(cursor, db):
    cursor.close()
    db.close()

def query_table(table, column):
    mydb= connect_to_pg()

    cursor= mydb.cursor()

    query= 'SELECT {} FROM {}'.format(column, table)
    cursor.execute(query)
    
    close_pg(cursor, mydb)

    return cursor.fetchall()

def query_table_by_column(table, column, column_value):
    mydb= connect_to_pg()

    cursor= mydb.cursor()

    query= 'SELECT * FROM {} WHERE {} = {}'.format(table, column, column_value)
    cursor.execute(query)
    
    close_pg(cursor, mydb)

    return cursor.fetchall()

