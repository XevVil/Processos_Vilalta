class EquacioPrimerGrau:

    def __init__(self, s):
        self.s_eq = s

    def calcula(self):
        self.h = self.s_eq.split()

        if "x" in self.h[0]:
            self.a = self.h[0]
            self.a = self.a[:-1]
            self.b = self.h[2]
            self.operador = self.h[1]
            self.c = self.h[4]
        else:
          return "L'equacio no segueix el format ax + b = c"


        try:
          float(self.b[2]) 
        except:
          return "Operador no valid "+self.s_eq

        if self.operador == "+":
          self.r = (float(self.c) - float(self.b))/float(self.a)
        elif self.operador == "-":
          self.r = (float(self.c) + float(self.b))/ float(self.a)
        elif self.operador == "/":
          self.r = "Error"
        elif self.operador == "*":
          self.r = "Error"
        return self.r
