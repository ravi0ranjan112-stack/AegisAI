from aegis.events.bus import EventBus


def test_event_bus():
    bus = EventBus()

    state = {"called": False}

    def handler():
        state["called"] = True

    bus.subscribe("boot", handler)
    bus.emit("boot")

    assert state["called"]
