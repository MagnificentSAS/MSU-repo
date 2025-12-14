import sys

class Omnibus:
    _global_counts = {}

    def __setattr__(self, name, value):
        Omnibus._global_counts[name] = Omnibus._global_counts.get(name, set()) | {id(self)}

    def __getattr__(self, name):
        return len(Omnibus._global_counts.get(name, set()))

    def __delattr__(self, name):
        if name in Omnibus._global_counts:
            Omnibus._global_counts[name] -= {id(self)}
            if len(Omnibus._global_counts[name]) == 0:
                del Omnibus._global_counts[name]

exec(sys.stdin.read())
