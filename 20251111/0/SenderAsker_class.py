class Sender:
    greeted = False
    @classmethod
    def report(self_c):
        if not self_c.greeted:
            print("Greetings!")
            self_c.greeted = True
        else:
            print("Get away!")

class Asker:
    @staticmethod
    def askall(lst):
        for s in lst:
            s.report()
