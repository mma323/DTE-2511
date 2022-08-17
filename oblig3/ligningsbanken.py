import random as rdm

def main():
    tests = make_test(['Ola', 'Kari', 'Fredrik'], 5)
    answer_questions(tests)
    print(tests)

def eq_2_text(eq):
    if eq[0]==1:
        a = ""
    elif eq[0]==-1:
        a = "-"
    else:
        a = eq[0]
    
    if eq[1] > 0:
        b = f"+ {eq[1]}"
    else:
        b = f"- {abs(eq[1])}"

    if eq[2] == 1:
        c = ""
    elif eq[2] == -1:
        c = "-"
    else:
        c = eq[2]

    if eq[3] > 0:
        d = f"+ {eq[3]}"
    else:
        d = f"- {abs(eq[3])}"

    return f"{a}x {b} = {c}x {d}"

def ok(L):
    for element in L:
        if element == 0:
            return False
    
    if L[0] == L[2]:
        return False
    
    if L[1] == L[3]:
        return False
    
    return True

def make_eq():
    equation = []
    for i in range(4):
        equation.append( rdm.randint(-9, 9) ) 

    if ok(equation):
        return equation
    else:
        return make_eq()

def make_n_eqs(n):
    equations = []
    for i in range(n):
        equation = make_eq()
        equations.append(equation)
    
    for equation in equations:
        if equations.count(equation) > 1:
            return make_n_eqs()
        if equations.count( equation[::-1] ) > 0:
            return make_n_eqs()
        if equations.count( equation[2:4] + equation[0:2] ) > 0:
            return make_n_eqs
            
    return equations

def make_test(students, n):
    tests = {}
    
    for name in students:
        tests[name] = make_n_eqs(n)

    return tests

def answer_questions(D):
   correct_name = False
   while not correct_name:
       name = input("Enter your name: ")
       if name in D:
           correct_name = True

   print("Please solve these equations: ")
   for equation in D[name]:
       print( eq_2_text(equation) )
       x = input("x = ")
       equation.append(x)
   return D
    
if __name__ == "__main__":
    main()
