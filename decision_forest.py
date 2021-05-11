# 250201092

Istat = eval(input("Istat: "))
decision_A = 0 # result of decision A
decision_B = 0 # result of decision B
decision_C = 0 # result of decision C
flag_rm = False # control for rm input
flag_nox = False # control for nox input

# Decision Tree A
if Istat >= 9.7:
    if Istat >= 20:
        flag_nox = True
        nox = eval(input("nox: ")) # this line get an input from user when Istat>=20 but not, do not get an input
        if nox >= 0.6:
            decision_A = 10
        else:
            decision_A = 17
    else:
        lon = eval(input("lon: "))
        if lon >= -7.1:
            decision_A = 18
        else:
            decision_A = 22
else:
    flag_rm = True
    rm = eval(input("rm: ")) # this line get an input from user when else blog runs but not, do not get an input
    if rm < 6.9:
        age = eval(input("age: "))
        if age < 88:
            if rm < 6.6:
                decision_A = 23
            else:
                decision_A = 28
        else:
            decision_A = 36
    else:
        if rm < 7.4:
            decision_A = 34
        else:
            decision_A = 45

# Decision Tree B
if not flag_rm:
    rm = eval(input("rm: ")) # if rm input does not get from user above lines, it will got this line
if rm < 7.1:  # if rm input get from user, the code will continuous this line
    if Istat >= 15:
        if not flag_nox:
            nox = eval(input("nox: ")) # if nox input does not get from user above lines, it will got this line
        if nox >= 0.6:
            if Istat >= 20:
                decision_B = 10
            else:
                decision_B = 15
        else:
            decision_B = 18
    else:
        if rm < 6.5:
            if Istat >= 9.6:
                decision_B = 21
            else:
                decision_B = 24
        else:
            if Istat >= 4.9:
                decision_B = 26
            else:
                decision_B = 32
else:
    if rm < 7.4:
        decision_B = 33
    else:
        decision_B = 46

# Decision Tree C
if rm < 6.7:
    if Istat >= 14:
        crim = eval(input("Crim: "))
        if crim >= 7:
            decision_C = 12
        else:
            decision_C = 17
    else:
        if Istat >= 9.5:
            decision_C = 21
        else:
            rad = eval(input("Rad: "))
            if rad < 7.5:
                decision_C = 24
            else:
                decision_C = 34
else:
    if rm < 7.5:
        if Istat >= 5.5:
            ptratio = eval(input("Ptratio: "))
            if ptratio >= 19:
                decision_C = 22
            else:
                decision_C = 31
        else:
            decision_C = 34
    else:
        decision_C = 45

print("Decision Tree A:", decision_A)
print("Decision Tree B:", decision_B)
print("Decision Tree C:", decision_C)
average = (decision_A + decision_B + decision_C)/3 # average of three decision trees
print("Decision Forest:", average)



