# from abc import ABC
# class bus(ABC):
#     def volvo(self):
#         print("hello")
#         print("YYY")
# class SRT(bus):
#     def volvo(self):
#         print("it is lux")
# class KPN(bus):
#     def volvo(self):
#         print("AC BUS")
# class SAT(bus):
#     def volvo(self):
#         print("libray vehchile")
# s=SRT()
# s.volvo()
# s=KPN()
# S1=KPN()
# S1.volvo()
# s2=SAT()
# s2.volvo()

from abc import *
class falcon(ABC):
    def __init__(self):
        self.mine=[12,34,56,123,4565,345,66,65,1234]
    #abstract fun
    def heythere(self):
        pass
class winter(falcon):
    def heythere(self):
        print(self.mine)
win=winter()
win.heythere()