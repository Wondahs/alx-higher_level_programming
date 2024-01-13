#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    curr = conn.cursor()
    query = '''
        SELECT cities.name
        FROM cities
        WHERE cities.state_id LIKE
        (SELECT states.id FROM states WHERE states.name LIKE %s)
        ORDER BY cities.id ASC
        '''
    curr.execute(query, (argv[4],))

    result = []
    for row in curr.fetchall():
        result += row
    print(", ".join(result))

    curr.close()
    conn.close()
