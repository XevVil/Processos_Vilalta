class EquacioPrimerGrau:

    def __init__(self, s):
        self.s_eq = s

    def calcula(self):
        h = self.s_eq.split()
        a = h[0]
        a = a[1-1]
        b = h[2]
        operador = h[1]
        c = h[4]
        print(self.s_eq)

        if (operador == "+"):
          r = (int(c) - int(b))/int(a)
          print(r)

        if (operador == "-"):
            r=(int(c) + int(b))/ int(a)
            print(r)


eq = EquacioPrimerGrau("2x + 3 = 7")
eq.calcula()
