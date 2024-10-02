import pytest
from lesson_02_03 import init_db, add_user, get_user


@pytest.fixture
def db_conn():
   conn = init_db()
   yield conn
   conn.close()

def test_add_or_get_user(db_conn):
   add_user(db_conn, "Sasha", 30)
   user = get_user(db_conn, "Sasha")
   assert user == (1, "Sasha", 30)

@pytest.mark.parametrize("name, age", [
   ("Sasha", 30),
   ("Masha", 30),
])
def test_add_or_get_user_parametrized(db_conn, name, age):
   add_user(db_conn, name, age)
   user = get_user(db_conn, name)
   print(user)
   assert user == (1, name, age)
