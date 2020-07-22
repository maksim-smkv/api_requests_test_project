import requests
from itertools import groupby

url = 'https://jsonplaceholder.typicode.com/posts/'


def get_json():
    res = requests.get(url)
    if res:
        print("Response OK - resource is available.")
    else:
        print("Response failed. Code:", res.status_code)
    json_file_from_site = res.json()
    return json_file_from_site


def test_get_count_the_number_of_users():   # check that there are 10 users
    json_file_from_site = get_json()

    user_ids = list(element['userId'] for element in json_file_from_site)
    sorted_user_id_list = [el for el, _ in groupby(user_ids)]

    assert len(sorted_user_id_list) == 10


def test_get_count_the_number_of_entities():    # check that there are only 100 records
    json_file_from_site = get_json()

    number_of_entities = [element['id'] for element in json_file_from_site]

    assert len(number_of_entities) == 100


def test_get_count_the_number_of_entities_per_user():   # check the number of records per user and that each record can be obtained separately
    json_file_from_site = get_json()

    user_ids = list(element['userId'] for element in json_file_from_site)
    sorted_user_id_list = [el for el, _ in groupby(user_ids)]

    for userId in sorted_user_id_list:
        response = requests.get(url+'?userId='+str(userId)).json()
        number_of_entities_per_user = [element['id'] for element in response]
        assert len(number_of_entities_per_user) == 10
        for entity_id in number_of_entities_per_user:
            response = requests.get(url + '?userId=' + str(userId) + '&id=' + str(entity_id))
            assert response.status_code == 200


def test_post_new_entry():  # check the status code after saving a new entry
    data = {'userId': '1', 'id': '101', 'title': 'test_title', 'body': 'test_body'}

    new_entry = requests.post(url, data=data)

    assert new_entry.status_code == 201

