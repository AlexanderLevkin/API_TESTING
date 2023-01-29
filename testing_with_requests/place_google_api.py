import requests


class Test_New_Location():
    """Work with new location"""

    def test_create_new_location(self):
        """Create new location"""

        base_url = "https://rahulshettyacademy.com"  # Базовая url
        key = "?key=qaclick123"  # Параметр для всех запросов
        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post

        """Post Method"""

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        result_post = requests.post(post_url, json=json_for_create_new_location)
        check_status = result_post.json().get("status")
        check_scope = result_post.json().get("scope")
        place_id = result_post.json().get("place_id")
        print(result_post.text)
        print(f"Status code: {result_post.status_code}")
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print(f"Successful!!! Created the new location")
        else:
            print("Failed!!! Request is wrong")
        assert check_status == "OK"
        assert check_scope == "APP"
        print("Status OK\nScope OK")
        print(f"Place Id = {place_id}")

        """Check creation new location with method GET"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Status Code : {result_get.status_code}")
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Successful!!! Checking the creation the new location")
        else:
            print("Failed. New location wasn't get")

        """Check the PUT Method"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_location = {  # Создаём тело запроса
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_location)  # Создаём переменную в которую помещаем
        # url по которому мы будем обращаться и само тело запроса в формате Json
        print(result_put.text)  # В формате TEXT!!!
        assert 200 == result_put.status_code
        if result_post.status_code == 200:
            print(f"Successful!!! Address successfully updated")
        else:
            print("Failed!!! Request is wrong")
            """Check the msg field"""
        check_put = result_put.json()  # Создаём переменную для проверки нашего PUT запроса в формате JSON ???????
        check_put_info = check_put.get("msg")  # Делаем GET запрос с ключом "msg" что бы получить его значение
        # для дальнейшей проверки
        assert check_put_info == "Address successfully updated"
        print(f"'{check_put_info}' - this is message correct")

        """Check the change the new location"""
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Status Code : {result_get.status_code}")
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Successful!!! Checking the creation the new location")
        else:
            print("Failed. New location wasn't get")

        """Check the address field"""
        check_address = result_get.json()  # Создаём переменную для проверки нашего PUT запроса в формате JSON
        check_address_info = check_address.get("address")  # Делаем GET запрос с ключом "address" что бы
        # получить его значение для дальнейшей проверки
        assert check_address_info == "100 Lenina street, RU"
        print(f"'{check_address_info}' - this address message correspond value '100 Lenina street'")

        """Delete new location"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        check_status_code = result_delete.status_code
        print(check_status_code)
        assert check_status_code == 200
        if check_status_code == 200:
            print(f"Status code is : {check_status_code}")
        else:
            print("Status code was failed!!!")
        check_delete_status = result_delete.json()
        check_delete_status_info = check_delete_status.get("status")
        assert check_delete_status_info == "OK"
        print(f"Delete new location with response: {check_delete_status_info}")

        """Check after delete"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Status Code : {result_get.status_code}")
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Successful!!! Checking the creation the new location")
        else:
            print("Failed. New location wasn't get")
        check_msg = result_get.json()
        check_msg_info = check_msg.get("msg")
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print("Location was delete\nTesting 'Test new location was finish successful'")


new_place = Test_New_Location()
new_place.test_create_new_location()
