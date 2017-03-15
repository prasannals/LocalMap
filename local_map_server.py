from flask import Flask
from flask import request
from flask import abort
import sqlite3
import sys
from flask import jsonify

port_number = None
if len(sys.argv) == 1:
    port_number = 12222
else:
    port_number = int(argv[1])
db_name = 'local_map_server.db'
table_name = 'key_val_table'
host = '0.0.0.0'


conn = sqlite3.connect(db_name)
conn.execute('CREATE TABLE IF NOT EXISTS ' + table_name + ' (key TEXT, val TEXT);')
conn.close()

app = Flask(__name__)

@app.route('/<string:key>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def service(key):
    conn = sqlite3.connect(db_name)

    if request.method == 'GET':
        cursor = conn.execute('SELECT * from ' + table_name + ' where key = \'' + key + '\';' )
        results = []
        for row in cursor:
            k = row[0]
            v = row[1]
            results.append({'key':k, 'value':v})

        conn.close()
        return jsonify({'result':results})
    elif request.method == 'POST':
        if not request.json:
            abort(404)
        value = request.json['value']
        conn.execute('INSERT INTO ' + table_name + ' VALUES (\'' + key + '\', \'' + value  + '\');')
        conn.commit()
        conn.close()
        return jsonify(request.json)
    elif request.method == 'PUT':
        if not request.json:
            abort(404)
        value = request.json['value']
        conn.execute('UPDATE ' + table_name + ' SET val = \''+ value  + '\' WHERE key = \'' + key + '\';')
        conn.commit()
        conn.close()
        return jsonify(request.json)
    elif request.method == 'DELETE':
        conn.execute('DELETE FROM ' + table_name + ' WHERE key = \'' + key + '\';')
        conn.commit()
        conn.close()
        return 'Successfully deleted ' + key

if __name__ == '__main__':
    app.run(host=host, port=port_number)