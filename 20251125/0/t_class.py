C = type("C", (), {"var": 100500, "__init__": lambda self, v: setattr(self, "var", v)})
