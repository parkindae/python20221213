#전역변수
str = "Not Class Member"

#클래스정의
class GString:
    #멤버정의
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #명시적으로 지정
        print(self.str)

g = GString()
g.set("First Message")
g.print()
