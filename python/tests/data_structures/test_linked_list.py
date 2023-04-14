import pytest
from data_structures.linked_list import LinkedList
from data_structures.linked_list import zipLists

def test_exists():
    assert LinkedList


#@pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


#@pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


#@pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


#@pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


#@pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


#@pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


#@pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


#@pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")

"""
Added Tests
"""

def test_includes_false2():
    linked_list = LinkedList()
    linked_list.insert("potato")
    assert not linked_list.includes(None)

def test_to_string_nulls():
    linked_list = LinkedList()
    linked_list.insert("None")
    assert str(linked_list) == "{ None } -> NULL"

def test_to_string_wonky():
    linked_list = LinkedList()
    linked_list.insert("Node(potato)")
    assert str(linked_list) == "{ Node(potato) } -> NULL"


def test_zipper1():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    linked_list1.insert("2")
    linked_list1.insert("3")
    linked_list1.insert("1")

    linked_list2.insert("4")
    linked_list2.insert("9")
    linked_list2.insert("5")

    zippedlist = zipLists(linked_list1, linked_list2)

    assert str(zippedlist) == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL"

def test_zipper2():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    linked_list1.insert("3")
    linked_list1.insert("1")

    linked_list2.insert("4")
    linked_list2.insert("9")
    linked_list2.insert("5")

    zippedlist = zipLists(linked_list1, linked_list2)

    assert str(zippedlist) == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NULL"

def test_zipper3():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    linked_list1.insert("2")
    linked_list1.insert("3")
    linked_list1.insert("1")

    linked_list2.insert("9")
    linked_list2.insert("5")

    zippedlist = zipLists(linked_list1, linked_list2)

    assert str(zippedlist) == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> NULL"

def test_zipper4():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    linked_list2.insert("4")
    linked_list2.insert("9")
    linked_list2.insert("5")

    zippedlist = zipLists(linked_list1, linked_list2)

    assert str(zippedlist) == "{ 5 } -> { 9 } -> { 4 } -> NULL"

def test_zipper5():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    linked_list1.insert("2")
    linked_list1.insert("3")
    linked_list1.insert("1")

    zippedlist = zipLists(linked_list1, linked_list2)

    assert str(zippedlist) == "{ 1 } -> { 3 } -> { 2 } -> NULL"


def test_append():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.append(5)
    assert str(linked_list) == "{ 1 } -> { 3 } -> { 5 } -> NULL"

def test_append_empty():
    linked_list = LinkedList()
    linked_list.append(5)
    assert str(linked_list) == "{ 5 } -> NULL"

def test_insert_before():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.append(5)
    linked_list.insert_before(3,7)
    assert str(linked_list) == "{ 1 } -> { 7 } -> { 3 } -> { 5 } -> NULL"

def test_insert_before2():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.append(5)
    linked_list.insert_before(4,7)
    assert str(linked_list) == "{ 1 } -> { 3 } -> { 5 } -> NULL"

def test_insert_before3():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.append(5)
    linked_list.insert_before(1,7)
    assert str(linked_list) == "{ 7 } -> { 1 } -> { 3 } -> { 5 } -> NULL"

def test_insert_after():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.append(5)
    linked_list.insert_after(3,7)
    assert str(linked_list) == "{ 1 } -> { 3 } -> { 7 } -> { 5 } -> NULL"

def test_insert_after2():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.append(5)
    linked_list.insert_after(5,7)
    assert str(linked_list) == "{ 1 } -> { 3 } -> { 5 } -> { 7 } -> NULL"

def test_insert_after3():
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.append(5)
    linked_list.insert_after(1,7)
    assert str(linked_list) == "{ 1 } -> { 7 } -> { 3 } -> { 5 } -> NULL"

def test_insert_after3():
    linked_list = LinkedList()
    linked_list.insert_after(1,7)
    assert str(linked_list) == "NULL"


