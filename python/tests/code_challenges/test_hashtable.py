from data_structures.hashtable import Hashtable


def test_hashtable_exists():
    assert Hashtable


def test_set_exists():
    assert Hashtable.set


def test_get_exists():
    assert Hashtable.get


def test_hash_exists():
    assert Hashtable.hash


def test_contains_exists():
    assert Hashtable.contains


def test_keys_exists():
    assert Hashtable.keys


def test_create_default():
    ht = Hashtable()
    actual = ht.size
    expected = 1024
    assert actual == expected


def test_hash():
    ht = Hashtable()
    index = ht.hash('cat')
    assert 0 <= index < ht.size  # 0 is less than or equal to index while index is less than size


def test_set_apple():
    ht = Hashtable()
    ht.set('fruit', 'apple')
    fruit_ind = ht.hash('fruit')
    actual = ht.buckets[fruit_ind]
    expected = ('fruit', 'apple')
    assert actual.head.value == expected


def test_get_apple():
    ht = Hashtable()
    ht.set('fruit', 'apple')
    actual = ht.get('fruit')
    expected = 'apple'
    assert actual == expected


def test_collisions():
    ht = Hashtable()
    ht.set('cat', 'josie')
    ht.set('act', 'a contemporary theatre')
    ht.set('tac', 'taco tuesday')

    assert ht.get('cat') == 'josie'
    assert ht.get('act') == 'a contemporary theatre'
    assert ht.get('tac') == 'taco tuesday'


def test_contains_true():
    ht = Hashtable()
    ht.set('cat', 'josie')
    expected = True
    actual = ht.contains('cat')
    assert actual == expected


def test_contains_false():
    ht = Hashtable()
    ht.set('cat', 'josie')
    expected = False
    actual = ht.contains('act')
    assert actual == expected


def test_keys_in_hashtable():
    ht = Hashtable()
    ht.set('cat', 'josie')
    ht.set('act', 'a contemporary theatre')
    ht.set('tac', 'taco tuesday')
    actual = ht.keys()
    expected = {'cat', 'act', 'tac'}
    assert actual == expected


def test_keys_not_in_hashtable():
    ht = Hashtable()
    ht.set('cat', 'josie')
    ht.set('act', 'a contemporary theatre')
    ht.set('gor', 'taco tuesday')
    actual = ht.keys()
    expected = ['cat', 'act', 'tac']
    assert actual != expected


def test_set_update():
    ht = Hashtable()
    ht.set('cat', 'josie')
    ht.set('cat', 'a contemporary theatre')
    actual = ht.get('cat')
    expected = 'a contemporary theatre'
    assert actual == expected


def test_contains_zero():
    ht = Hashtable()
    ht.set(0, 'zero')
    expected = True
    actual = ht.contains(0)
    assert actual == expected
