from testhelpers import post_api, get_api, delete_api, put_api

class TestPerson(object):
    #test cases for POST#
    def test_post_person_with_valid_data(self):
        new_person = {'first_name': 'Patrick', 'last_name': 'Stewart', 'birth_year': 1940}
        status_code, data = post_api('persons', new_person)
        assert status_code == 201
        assert data['first_name'] == 'Patrick'
        assert data['last_name'] == 'Stewart'
        assert data['birth_year'] == 1940
        assert isinstance(data['id'], str)

    def test_post_person_with_null_data(self):
        new_person = {'first_name': '', 'last_name': '', 'birth_year': ''}
        status_code, data = post_api('persons', new_person)
        assert status_code == 201
        assert data['first_name'] == ''
        assert data['last_name'] == ''
        assert data['birth_year'] == ''
        assert isinstance(data['id'], str)
    
    def test_post_person_with_empty_data(self):
        new_person = {}
        status_code, data = post_api('persons', new_person)
        assert status_code == 400
    
    def test_post_person_with_invalid_date(self):
        new_person = {'first_name': '', 'last_name': '', 'birth_year': 'test'}
        status_code, data = post_api('persons', new_person)
        assert status_code == 201
        assert data['birth_year'] == 'test'
        assert isinstance(data['id'], str)

    #test cases for GET#
    def test_get_person_with_valid_id(self):
        status_code, data = get_api('persons', 'b9f2d28c-57dc-4381-a752-ac36611ab51a')
        assert status_code == 200
        assert data['first_name'] == 'Arnold'
        assert data['last_name'] == 'Schwarzenegger'
        assert data['birth_year'] == 1947

    def test_get_person_with_invalid_id(self):
        status_code, data = get_api('persons', 'b9f2d28c-57dc-4381-a752-ac36611ab51b')
        assert status_code == 404
    
    def test_get_person_with_null_id(self):
        status_code, data = get_api('persons', '')
        assert status_code == 200
    
    #test cases for DELETE#
    def test_delete_person_with_invalid_id(self):
        status_code, data = delete_api('persons', 'b9f2d28c-57dc-4381-a752-ac36611ab51b')
        assert status_code == 404

    #test cases for PUT#
    def test_put_person_with_valid_id(self):
        update_exist_person = {'first_name': 'Patrick', 'last_name': 'Stewart', 'birth_year': 1940}
        status_code, data = put_api('persons', 'b636e887-7402-4eda-885f-549ea9792116',update_exist_person)
        assert status_code == 200
        assert data['first_name'] == 'Patrick'
        assert data['last_name'] == 'Stewart'
        assert data['birth_year'] == 1940
        return_movie_data = {"first_name": "Charlize", "last_name": "Theron", "birth_year": 1975}
        put_api('persons', 'b636e887-7402-4eda-885f-549ea9792116',return_movie_data)