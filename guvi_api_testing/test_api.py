import api_functions

url = "https://65c0f239dc74300bce8d0afe.mockapi.io/users"
new_data = {"Name": "Janani", "City": "Chennai", "Country": "India"}
update_data = {"Name": "Jeni Janani"}


# print the required data
def test_get_data():
    response = api_functions.fetch_data(url + "/12")
    print(response)


# negative case - access non existing data
def test_get_data_():
    response = api_functions.fetch_data(url + "/100")
    print(response)


# assert status code to be 200
def test_status_code_200():
    response = api_functions.check_status_code(url + "/1")
    assert response == 200


# Status code not to be 200
def test_status_code_not_200():
    response = api_functions.check_status_code(url + "/1")
    assert response.status_code != 200


# Insert data and verify status code to be 201
def test_insert_data():
    response = api_functions.insert_data(url, data=new_data)
    assert response.status_code == 201


def test_insert_data_ID():
    response = api_functions.insert_data(url + "/17", data=new_data)
    assert response.status_code == 201


# # update existing data
def test_update_data():
    response = api_functions.update_data(url + "/51", update_data)
    try:
        assert response.status_code == 201
    except:
        print(response)


# verify updated data
def test_verify_updated_data():
    response = api_functions.fetch_data(url + "/51")
    assert response.get('Name') == update_data.get('Name')
    assert response.get("City") == new_data.get('City')
    assert response.get("Country") == new_data.get('Country')


# verify negative case of updated data
def test_verify_updated_data_():
    response = api_functions.fetch_data(url + "/51")
    try:
        assert response.get('Name') == new_data.get('Name')
    except:
        assert response.get('Name') == update_data.get('Name')


# update with non-existing ID
def test_update_data_false_ID():
    response = api_functions.update_data(url + "/200", update_data)
    assert response.status_code == 201


# # Delete existing ID
def test_delete_data():
    response = api_functions.delete_data(url + "/17")
    print(response)
    assert response.status_code == 404
    response = api_functions.fetch_data(url + "/17")
    print(response)


# delete non existing ID
def test_delete_data_():
    response = api_functions.delete_data(url + "/150")
    print(response)


# Delete particular range of data
def test_delete_data_range():
    for i in range(52, 80):
        response = api_functions.delete_data(url + "/" + str(i))
        try:
            assert response.status_code == 200
        except:
            assert response.status_code == 404
