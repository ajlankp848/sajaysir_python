#** as dictionary

def employee(**kwargs):
    for k,v in kwargs.items():
        print(k, "=>", v)
employee(id=100,nat_place="pattambbi",w_place="kochi")


def print_employee(**kwras):
    print(kwras)
print_employee(id=1234,name="Ajay",salary=50000)