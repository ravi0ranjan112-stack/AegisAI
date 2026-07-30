from aegis.filesystem.service import FileService


def test_file_service():
    fs = FileService()

    fs.write_text("temp/test.txt", "Hello Aegis")

    assert fs.exists("temp/test.txt")

    text = fs.read_text("temp/test.txt")

    assert text == "Hello Aegis"

    fs.delete("temp")

    assert not fs.exists("temp")
