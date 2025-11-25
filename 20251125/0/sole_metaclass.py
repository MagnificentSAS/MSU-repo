class sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError("Too many parents")

        return super().__new__(metacls, name, parents, namespace)
