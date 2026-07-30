from aegis.process.service import ProcessService


def test_process_service():
    process = ProcessService()

    result = process.run(["python3", "--version"])

    assert result.returncode == 0
    assert "Python" in result.stdout or "Python" in result.stderr
