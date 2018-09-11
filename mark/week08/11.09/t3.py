from t1 import Person
from t2 import get_score


def monkeypatch4Person():    # 猴子补丁
    Person.get_score = get_score

monkeypatch4Person()

if __name__ == '__main__':
    print(Person().get_score())

