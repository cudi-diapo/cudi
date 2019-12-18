from srcs.Thread import Thread


class Test:
    def __init__(self, addr):
        self.test = 1
        self.addr = addr

    def __str__(self):
        return f"{self.test} | {self.addr.oui}"


class Oui:
    def __init__(self):
        self.oui = 3


def print_test(u):
    while u.test == 1:
        print(u)


oui = Oui()
test = Test(oui)
print(test)
oui.oui = "iruheiuh"
print(test)

nb = 10
t = []
for x in range(nb):
    t.append(Thread(x, f"Tread = {x}", print_test, test))
for x in t:
    x.start()
for x in t:
    x.join()

test.test = "changement"
oui.oui = "hfigeiugethghthotehgoiehgiorehiohrioghioerhirroeihg"
