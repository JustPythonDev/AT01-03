# PIP install pytest-mock
from home_ex_03_01 import get_random_cat_pic


def test_get_cat_pic_success(mocker):
   mock_get = mocker.patch('home_ex_03_01.requests.get')

   # Создаем мок-ответ для успешного запроса
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = [{
           "id":"al1",
           "url":"https://cdn2.thecatapi.com/images/al1.jpg",
           "width":1600,
           "height":1200
       }]


   cat_pic = get_random_cat_pic()

   assert cat_pic[0]["url"] == 'https://cdn2.thecatapi.com/images/al1.jpg'


def test_get_cat_pic_failure(mocker):
   mock_get = mocker.patch('home_ex_03_01.requests.get')

   # Создаем мок-ответ для неуспешного запроса
   mock_get.return_value.status_code = 404

   cat_pic = get_random_cat_pic()

   assert cat_pic is None


