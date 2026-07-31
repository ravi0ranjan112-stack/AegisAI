from aegis.kernel.kernel import AegisKernel


def test_kernel():
    kernel = AegisKernel()

    assert kernel.ai is not None
    assert kernel.session is not None
    assert kernel.router.active == "ollama"
    assert kernel.settings.provider == "ollama"
