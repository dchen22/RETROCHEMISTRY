class Hydrocarbons:

    def __init__(self,eq='C'):

        self.eq = eq
        self.eq_list = []
        self.ele_parse()

    def ele_parse(self):
        c = 0
        while c < len(self.eq)-1:
            # checks for 2-letter symbols (e.g. 'Cl' and 'Pu' are uppercase followed by lowercase)
            if self.eq[c].isupper() and self.eq[c+1].islower():
                self.eq_list.append(self.eq[c]+self.eq[c+1])
            # checks for 1-letter symbols (e.g. 'N' and 'O' are single uppercase
            if self.eq[c].isupper() and self.eq[c+1].isupper():
                self.eq_list.append(self.eq[c])
            # checks for numbers
            if self.eq[c].isnumeric():
                c2 = c
                # search to see how long the number is ('300' is a '3' followed by '0' and '0')
                while c2 < len(self.eq):
                    if not self.eq[c2].isnumeric():
                        self.eq_list.append(self.eq[c:c2])
                        c += c2 - c - 1
                        break
                    c2 += 1
            c += 1
        return self.eq_list

    def adjacent(self,ind):
        # DOES NOT WORK FOR HYDROCARBON DERIVATIVES / COMPLEX FUNCTIONAL GROUPS

        # c1 and c2 are, respectively, counters that run left and right from the atom at the index
        c1,c2 = ind-1,ind+1
        adj_list = [None,None]
        while c1 >= 0:
            # check if element to the left is a number
            if self.eq_list[c1].isnumeric():
                c1 -= 1
            # check if element to the left is an atom (must be adjacent to atom at ind (NOT FOR HC DERIVATIVES))
            elif self.eq_list[c1].isalpha():
                adj_list[0] = self.eq_list[c1]
                break


        while c2 < len(self.eq_list):
            # check if element to the right is a number
            if self.eq_list[c2].isnumeric():
                c2 += 1
            # check if element to the right is an atom (must be adjacent to atom at ind (NOT FOR HC DERIVATIVES))
            elif self.eq_list[c2].isalpha():
                adj_list[1] = self.eq_list[c2]
                break

        return adj_list

cmpnd1 = Hydrocarbons('CClCCl')
print(cmpnd1.eq_list)
print(cmpnd1.adjacent(3))

# branching could be implemented through creating subarrays