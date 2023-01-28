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


new_place = Test_New_Location()
new_place.test_create_new_location()
