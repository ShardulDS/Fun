for i in range(1, 255):
    for j in range(i, 255):
        k = (3*j**2 - 2*i**2)/(4*i)
        if k*10%10 == 0:
            print(j, i)
            break
    