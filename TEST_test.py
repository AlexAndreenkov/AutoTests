import json

import requests


def testapi1():
    res = requests.get('https://automationexercise.com/api/productsList')
    response_body = res.json()
    assert response_body['responseCode'] == 200


def testapi2():
    res = requests.post('https://automationexercise.com/api/productsList')
    response_body = res.json()
    assert response_body['responseCode'] == 405
    assert response_body.get('message') == 'This request method is not supported.'


def testapi3():
    res = requests.get("https://automationexercise.com/api/brandsList")
    response_body = res.json()
    assert response_body['responseCode'] == 200


def testapi4():
    res = requests.put('https://automationexercise.com/api/brandsList')
    response_body = res.json()
    assert response_body['responseCode'] == 405
    assert response_body.get('message') == 'This request method is not supported.'


def testapi5():
    params = {
        'search_product': 'Tops'
    }
    res = requests.post('https://automationexercise.com/api/searchProduct', data=params)
    response_body = res.json()
    assert response_body['responseCode'] == 200


def testapi6():
    res = requests.post('https://automationexercise.com/api/searchProduct')
    response_body = res.json()
    assert response_body['responseCode'] == 400
    assert response_body.get('message') == 'Bad request, search_product parameter is missing in POST request.'


def testapi11():
    params = {
        'name': 'Alex',
        'email': 'alex@gmail.com',
        'password': '12341234',
        'title': 'Mr',
        'birth_date': '19',
        'birth_month': '10',
        'birth_year': '1990',
        'firstname': 'Alex',
        'lastname': 'Longero',
        'company': 'Awers',
        'address1': 'Moka 3',
        'address2': 'Loka 32',
        'country': 'Estonia',
        'zipcode': '13411',
        'state': 'Harjumaa',
        'city': 'Tallinn',
        'mobile_number': '+37255657712'

    }
    res = requests.post('https://automationexercise.com/api/createAccount', data=params)
    response_body = res.json()
    assert response_body['responseCode'] == 201
    assert response_body.get('message') == 'User created!'



def testapi7():
    params = {'email': 'alex@gmail.com',
              'password': '12341234'}
    res = requests.post('https://automationexercise.com/api/verifyLogin', data=params)
    resp_body = res.json()
    assert resp_body['responseCode'] == 200
    assert resp_body.get('message') == 'User exists!'


def testapi8():
    params = {'password': '12341234'}
    res = requests.post('https://automationexercise.com/api/verifyLogin', data=params)
    resp_body = res.json()
    assert resp_body['responseCode'] == 400
    assert resp_body.get('message') == 'Bad request, email or password parameter is missing in POST request.'


def testapi9():
    res = requests.delete('https://automationexercise.com/api/verifyLogin')
    resp_body = res.json()
    assert resp_body['responseCode'] == 405
    assert resp_body.get('message') == 'This request method is not supported.'


def testapi10():
    params = {
        'email': 'alex@gmail.com',
        'password': 'wrongpass111'
    }
    res = requests.post('https://automationexercise.com/api/verifyLogin', data = params)
    response_body = res.json()
    print(response_body)
    assert response_body['responseCode'] == 404
    assert response_body.get('message') == 'User not found!'


def testapi13():
    params = {
                'name': 'Alex',
                'email': 'alex@gmail.com',
                'password': '12341234',
                'title': 'Mr',
                'birth_date': '19',
                'birth_month': '10',
                'birth_year': '1990',
                'firstname': 'Alexandro',
                'lastname': 'Longeroro',
                'company': 'AwersOU',
                'address1': 'Moka 3',
                'address2': 'Loka 32',
                'country': 'Estonia',
                'zipcode': '13411',
                'state': 'Harjumaa',
                'city': 'Tallinn',
                'mobile_number': '+37255657712'
    }
    res = requests.put('https://automationexercise.com/api/updateAccount', data=params)
    response_body = res.json()
    assert response_body['responseCode'] == 200
    assert response_body.get('message') == 'User updated!'


def testapi14():
    params = {
        'email': 'alex@gmail.com'
    }
    res = requests.get('https://automationexercise.com/api/getUserDetailByEmail', params=params)
    response_body = res.json()
    print(response_body)
    assert response_body['responseCode'] == 200


def testapi12():
    params = {
        'email': 'alex@gmail.com',
        'password': '12341234'
    }
    res = requests.delete('https://automationexercise.com/api/deleteAccount', data=params)
    response_body = res.json()
    assert response_body['responseCode'] == 200
    assert response_body.get('message') == 'Account deleted!'
