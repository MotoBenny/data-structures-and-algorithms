from data_structures.hashtable import Hashtable


def left_join(table_a, table_b):
    table = []

    for key, value in table_a.items():
        if table_b.get(key):
            table.append([key, value, table_b.get(key)])

        else:
            table.append([key, value, 'NONE'])

    print(table)
    return table
