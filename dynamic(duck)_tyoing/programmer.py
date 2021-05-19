class Pycharm:
    def compile(self):
        print("compile using pycharm.")
    def run(self):
        print("run using pycharm. ")
class Vs_code:
    def compile(self):
        print("compile using vscode. ")
    def run(self):
        print("run using vs code. ")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.run()
p=Programmer()

#py=Pycharm()
#p.coding(py)

vs=Vs_code()
p.coding(vs)