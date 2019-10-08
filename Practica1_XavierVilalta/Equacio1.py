class EquacioPrimerGrau:

    def __init__(self, s):
        self.s_eq = s

    def calcula(self):
        h = self.s_eq.split()
        a = h[0]
        a = a[:-1]
        b = h[2]
        operador = h[1]
        c = h[4]
        print(self.s_eq)

        if operador == "+":
          r = (float(c) - float(b))/float(a)


        elif operador == "-":
          r=(float(c) + float(b))/ float(a)
        print("X = "+str(r))
        return r


eq = EquacioPrimerGrau("2x + 3 = 7")
eq.calcula()
