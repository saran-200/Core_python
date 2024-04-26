# overriding (same function name and same parameters)
class sam:
    def name(self):
        print("sam")
class raja(sam):
    def name(self):
        super().name()
        print("raja")
class arun(raja):
    def name(self):
        super().name()
        print("ARUN")
s=arun()
s.name()