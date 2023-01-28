import requests


class Test_new_joke():
    """Create new Joke"""

    def __int__(self):
        pass

    # def test_create_new_random_joke(self):
    #     """Create random Joke"""
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print(f"status code: {result.status_code}")
    #     assert 200 == result.status_code
    #     if result.status_code == 200:
    #         print(f"Successful!!! We get the new joke")
    #     else:
    #         print("Failed!!! Request is wrong")
    #     result.encoding = 'utf-8'
    #     print(result.text)
    #     check = result.json()
    #     # check_info = check.get("categories")
    #     # print(check_info)
    #     # assert check_info == []
    #     # print("Category is True")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print("Chuck is")
    #     else:
    #         print("Chuck is absent")

    def test_create_new_random_categories_joke(self):
        """Create random category Joke"""
        category = "sport"
        url = f"https://api.chucknorris.io/jokes/random?category={category}"
        print(url)
        result = requests.get(url)
        print(f"status code: {result.status_code}")
        assert 200 == result.status_code
        if result.status_code == 200:
            print(f"Successful!!! We get the new joke")
        else:
            print("Failed!!! Request is wrong")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        icon_url = check.get("icon_url")
        snippet_icon_url = "assets.chucknorris"
        print(icon_url)
        if snippet_icon_url in icon_url:
            print(f"Good {snippet_icon_url}")
        else:
            print("False")
        print(check_info)
        assert check_info == ["sport"]
        print("Category is True")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck is")
        # else:
        #     print("Chuck is absent")


sport_joke = Test_new_joke()
sport_joke.test_create_new_random_categories_joke()

