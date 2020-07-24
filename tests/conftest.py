import pytest

@pytest.fixture()
def data_for_new_entry():
    data = {'userId': '1', 'id': '101', 'title': 'test_title', 'body': 'test_body'}
    return data
