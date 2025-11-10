C = type('C', (), {'__init__': lambda self, v: setattr(self, 'v', v), '__str__': lambda self: f"{self.v}"})
