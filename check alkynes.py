# valencies in case they're needed later
vals = {
    'O':2,
    'C':4
}

# most Basic alkYne string
b_y = 'C#C'

class Hydrocarbon:

    def __init__(self,eq='CC'):
        self.eq = eq


    def is_alkyne(self):
        return b_y in self.eq

    def terminality(self):
        # assumes pure hydrocarbon alkyne (and single alkynyl group)
        left = 'terminal'
        right = 'terminal'
        # check for C bonded on left side of alkynyl group
        if self.eq.find(b_y) > 0 and self.eq[self.eq.find(b_y)-1] == 'C':
            left = 'internal'
        elif self.eq.find(b_y) > 1 and self.eq[self.eq.find(b_y)-2:self.eq.find(b_y)] == 'C-':
            left = 'internal'
        # check for C bonded on right side of alkynyl group
        if self.eq.find(b_y) < len(self.eq)-len(b_y) and self.eq[self.eq.find(b_y)+len(b_y)] == 'C':
            right = 'internal'
        elif self.eq.find(b_y) < len(self.eq)-len(b_y)-1 and self.eq[self.eq.find(b_y)+len(b_y):self.eq.find(b_y)+len(b_y)+2] == '-C':
            right = 'internal'
        # requires complete internalization of alkynyl group to be considered internal alkyne
        if left == 'internal' and right == 'internal':
            return 'internal'
        else:
            return 'terminal'

    def de_hydro_hal(self):
        pass


hc1 = Hydrocarbon(eq='C#C-C-C')
print(hc1.is_alkyne())
print(hc1.terminality())

# C-C#C-C
