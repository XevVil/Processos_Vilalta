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

        if (operador == "+"):
          r = (float(c) - float(b))/float(a)
          print(r)

        if (operador == "-"):
            r=(float(c) + float(b))/ float(a)
            print(r)



 ## 20x + 30 = 70 /// 20x - 70 = -30
