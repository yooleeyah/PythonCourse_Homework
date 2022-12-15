def DeMorgansLaw(x,y,z):
    if (not(x or y or z) == ((not x) and (not y) and (not z))): print('True')
    else: print('False')
for i in 0,1:
    for j in 0,1:
        for k in 0,1:
            DeMorgansLaw(i,j,k)