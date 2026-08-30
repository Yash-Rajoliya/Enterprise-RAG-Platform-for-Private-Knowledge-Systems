from app.vector.faiss_store import FAISSStore


def test_store():
    store = FAISSStore(dim=4)

    store.add(
        [[0.1,0.2,0.3,0.4]],
        ["doc"]
    )

    result = store.search(
        [0.1,0.2,0.3,0.4]
    )

    assert len(result) == 1