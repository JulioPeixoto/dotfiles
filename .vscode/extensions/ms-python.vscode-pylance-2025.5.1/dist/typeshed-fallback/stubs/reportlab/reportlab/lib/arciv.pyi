class ArcIV:
    def __init__(self, key) -> None: ...
    def reset(self) -> None: ...
    def encode(self, S): ...

def encode(text, key): ...
def decode(text, key): ...

__all__ = ["ArcIV", "encode", "decode"]
