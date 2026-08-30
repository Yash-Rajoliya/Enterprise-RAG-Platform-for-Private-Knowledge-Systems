from typing import Dict, Any


class StateManager:
    def __init__(self):
        self._state: Dict[str, Any] = {}

    def set(self, key: str, value: Any):
        self._state[key] = value

    def get(self, key: str):
        return self._state.get(key)

    def clear(self):
        self._state.clear()

    def snapshot(self):
        return dict(self._state)