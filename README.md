# Local Map
A library which allows you to persist key value pairs easily on a (preferably, local) server.

## Requirements
requests library.
Run the following to install it.
```
pip install requests
```

## Usage
#### Server Side
On server side run the local_map_server.py
```
python local_map_server.py
```
The above command runs the server on **port 12222** which is the default port that I've selected for this app. If the server needs to be run on a different port, specify the port number as the first argument on the command line like so
```
python local_map_server.py 6543
```
Now, the server will run on port 6543

#### Client Side
```
import local_map_client

client = local_map_client.LocalMapClient('192.168.0.103', 12222)
# replace 192.168.0.103 with your server's IP Address. The second argument is the port number. 
# Now, we're set to interact with the server.

value = client.get('some_key') # gets the value associated with the key. If key not present, returns None
status_code = client.post('some_key', 'some_val') # inserts the key value pair into the server and returns 
                                                  # the status code got from the server
status_code = client.update('some_key', 'some_val') # replaces the value associated with some key with new value
status_code = client.delete('some_key')           # deletes the key - value pair associated with the specified key
```
**NOTE** : For now, the key value pairs are stored and returned as strings. (even if you pass in a different object, str(object) is stored). Might have support for different objects in the future.
