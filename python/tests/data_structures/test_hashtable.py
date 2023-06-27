import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


#@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected

def test_more_fruit():
    hashtable = Hashtable()
    hashtable.set("apple", "apple sauce")
    hashtable.set("grape", "grape juice")
    hashtable.set("grapefruit", "yummy")
    hashtable.set("mango", "why would you eat this")
    actual = hashtable.get("mango")
    expected = "why would you eat this"
    assert actual == expected

def test_contains():
    hashtable = Hashtable()
    hashtable.set("apple", "apple sauce")
    hashtable.set("grape", "grape juice")
    hashtable.set("grapefruit", "yummy")
    hashtable.set("mango", "why would you eat this")
    actual = hashtable.has("grape")
    expected = True
    assert actual == expected

def test_contains2():
    hashtable = Hashtable()
    hashtable.set("apple", "apple sauce")
    hashtable.set("grape", "grape juice")
    hashtable.set("grapefruit", "yummy")
    hashtable.set("mango", "why would you eat this")
    actual = hashtable.has("dog")
    expected = False
    assert actual == expected

def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "apple sauce")
    hashtable.set("grape", "grape juice")
    hashtable.set("grapefruit", "yummy")
    hashtable.set("mango", "why would you eat this")
    actual = hashtable.keys()
    expected = ["apple", "grape", "grapefruit", "mango"]
    assert set(actual) == set(expected)

def test_keys2():
    hashtable = Hashtable()
    hashtable.set("apple", "apple sauce")
    hashtable.set("grape", "grape juice")
    hashtable.set("grapefruit", "yummy")
    hashtable.set("mango", "why would you eat this")
    actual = hashtable.keys()
    expected = ["apple", "grape", "grapefruit", "mango", "dragonfruit"]
    assert set(actual) != set(expected)


