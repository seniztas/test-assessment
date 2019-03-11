from testhelpers import post_api, get_api, delete_api, put_api

class TestMovie(object):
    #test cases for POST#
    def test_post_movie_with_valid_data(self):
        new_movie = {'title': 'Captan Marvel', 'year': 2019}
        status_code, data = post_api('movies', new_movie)
        assert status_code == 201
        assert data['title'] == 'Captan Marvel'
        assert data['year'] == 2019
        assert isinstance(data['id'], str)
    
    def test_post_movie_with_invalid_data(self):
        new_movie = {'title': '', 'year': ''}
        status_code, data = post_api('movies', new_movie)
        assert status_code == 201
        assert data['title'] == ''
        assert data['year'] == ''
        assert isinstance(data['id'], str)

    def test_post_movie_with_empty_data(self):
        new_movie = {}
        status_code, data = post_api('movies', new_movie)
        assert status_code == 400
    
    def test_post_movie_with_invalid_date(self):
        new_movie = {'title': '', 'year': 'test'}
        status_code, data = post_api('movies', new_movie)
        assert status_code == 201
        assert data['year'] == 'test'
        assert isinstance(data['id'], str)

    #test cases for GET#
    def test_get_movie_with_valid_id(self):
        status_code, data = get_api('movies', '6652f161-d664-4a3c-aaf8-99ff0880c380')
        assert status_code == 200
        assert data['title'] == 'Sharknado'
        assert data['year'] == 2013

    def test_get_movie_with_invalid_id(self):
        status_code, data = get_api('movies', '6652f161-d664-4a3c-aaf8-99ff0880c381')
        assert status_code == 404
    
    def test_get_movie_with_null_id(self):
        status_code, data = get_api('movies', '')
        assert status_code == 200

     #test cases for DELETE#
    def test_delete_movie_with_invalid_id(self):
        status_code, data = delete_api('movies', 'b9f2d28c-57dc-4381-a752-ac36611ab51b')
        assert status_code == 404

    #test cases for PUT#
    def test_put_movie_with_valid_id(self):
        update_exist_movie = {'title': 'Captan Marvel', 'year': 2019}
        status_code, data = put_api('movies', 'e6068a8f-fb38-49b5-a1a9-2e1222a2bdce',update_exist_movie)
        assert status_code == 200
        assert data['title'] == 'Captan Marvel'
        assert data['year'] == 2019
        return_movie_data = {"title": "Die Hard", "year": 1988}
        put_api('movies', 'e6068a8f-fb38-49b5-a1a9-2e1222a2bdce',return_movie_data)

