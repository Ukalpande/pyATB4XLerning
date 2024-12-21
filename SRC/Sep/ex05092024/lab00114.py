"""

Hybrid Inheritance
hierarchical Inheritance
"""
class Father:
    def BHK1(self):
        print("fadars 1BHK for all son's")

class Ujwal(Father):
    def BHK2(self):
        print("ujwal has 2BHK")

class Shubh(Father):
    def BHK3(self):
        print("shubh has 3BHK")

class Gopi(Father):
    def n0_house(self):
        print("gopi has no House")


uk = Ujwal()
uk.BHK1()
uk.BHK2()
#uk not access 3 bhk bcoz its belongs to sk

sk = Shubh()
sk.BHK1()
sk.BHK3()
#sk not access 2bhk coz its belongs to uk
gk = Gopi()
gk.BHK1()
gk.n0_house()
#gk not access 3bhk and 2bhk bcoz its belongs to uk and sk
