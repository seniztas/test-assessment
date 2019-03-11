from testhelpers import post_api, get_api, delete_api

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
        assert status_code == 404, 'No persons found'
    
    def test_get_movie_with_null_id(self):
        status_code, data = get_api('movies', '')
        assert status_code == 200