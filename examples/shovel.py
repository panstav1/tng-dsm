from shovel import task
import requests

@task
def insert_tests():

    port = 'localhost:4010'

    print(requests.post('http://' + port + '/api/tests/user1/item1').content)
    print(requests.post('http://' + port + '/api/tests/user1/item2').content)
    print(requests.post('http://' + port + '/api/tests/user1/item3').content)
    print(requests.post('http://' + port + '/api/tests/user1/item5').content)
    print(requests.post('http://' + port + '/api/tests/user1/item6').content)
    print(requests.post('http://' + port + '/api/tests/user1/item8').content)
    print(requests.post('http://' + port + '/api/tests/user2/item3').content)
    print(requests.post('http://' + port + '/api/tests/user2/item2').content)
    print(requests.post('http://' + port + '/api/tests/user2/item6').content)
    print(requests.post('http://' + port + '/api/tests/user2/item7').content)
    print(requests.post('http://' + port + '/api/tests/user3/item1').content)
    print(requests.post('http://' + port + '/api/tests/user3/item2').content)
    print(requests.post('http://' + port + '/api/tests/user3/item3').content)
    print(requests.post('http://' + port + '/api/tests/user3/item5').content)