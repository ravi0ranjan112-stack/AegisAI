from aegis.vector.document import Document


def test_document() -> None:
    doc = Document("1", "Hello World")

    assert doc.id == "1"
    assert doc.text == "Hello World"
