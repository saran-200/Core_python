# class college:
#     def __init__(self,name,course):
#         self.n=name
#         self.c=course
#     def print(self):
#         print(self.n,self.c)
# c=college("saran","IT")
# c.print()


# ======> single
# class bike:
#     def gear(self):
#         print("speed")
# class car(bike):
#     def ride(self):
#         print("race")
# c=car()
# c.gear()
# c.ride()


# =======> multilevel
# class college:
#     def clg (self):
#         print("MEC")
# class dept(college):
#     def dep(self):
#         print("IT")
# class sect(dept):
#     def sec(self):
#         print("no section")
# a=sect()
# a.clg()
# a.dep()
# a.sec()

# ==========> multiple
# class bus:
#     def lux(self):
#         print("lux bus")
# class lorry:
#     def load(self):
#         print("load lorry")
# class transport(bus,lorry):
#     def tra(self):
#         print("welcome")
# a=transport()
# a.tra()
# a.load()
# a.lux()

# ========> hiearach..... 

# class college:
#     def name(self):
#         print("MEC")
#     def type(self):
#         print("autonomus")
#         def pla(self):
#             print("rasipuram")
# class placement(college):
#     def grade(self):
#         print("good")
# class dept(college):
#     def name1(self):
#         print("IT")
# class detalis(placement,dept):
#     def data(self):
#         print("welcome")
# a=detalis()
# a.data()
# a.name(),a.type()
# a.grade()
# a.name1()


