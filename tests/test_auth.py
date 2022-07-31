def test_login_required(client):
    response = client.post('/login', data={'email': '', 'password': ''})
    expectation_result = 'Email dan password tidak boleh kosong'
    assert expectation_result in response.context['errors']

def test_login_valid(client):
    payload = {'email': 'admin123@gmail.com', 'password': 'admin123'}
    response = client.post('/login', data=payload)
    token = response.cookies.get('Authorization')
    assert "Bearer" in token

def test_login_inexistent_admin(client):
    payload = {'email': 'test@gmail.com', 'password': 'test123456'}
    response = client.post('/login', data=payload)
    assert response.cookies.get('Authorization') == None