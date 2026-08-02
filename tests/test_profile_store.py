from aegis.profiles.store import ProfileStore


def test_profile_store():
    store = ProfileStore()
    assert store.execute("set name aegis") == "OK"
    assert store.execute("get name") == "aegis"
