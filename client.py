import requests
import json
import socket
import time

root_node_address = '192.168.0.161'
my_port = '5000'

def initiate():
    res = requests.post(
        'http://localhost:'+my_port+'/nodes/register',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(
            {
                'nodes': ['http://'+root_node_address+':5000']
            }
        ))
    requests.post(
        'http://'+root_node_address+':5000/nodes/register',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(
            {
                'nodes': ['http://'+socket.gethostbyname(socket.getfqdn())+':'+my_port]
            }
        ))

def mining():
    requests.get('http://localhost:'+my_port+'/update_node')
    requests.get('http://localhost:'+my_port+'/nodes/resolve')
    res = requests.get('http://localhost:'+my_port+'/mine')

    return res.json()



if __name__ == "__main__":
    initiate()
    while True:
        res = mining()
        print(res)
        time.sleep(3)