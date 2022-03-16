while True:
    try:
        n_m = list(map(int, input("Enter Length and Width, for example(3 9):\n").split()))
        if n_m[0]*3 == n_m[-1]:
            break
        else:
            print("Please Enter width which is three times the length ")
    except BaseException:
        print("Invalid Input")

verti, hori = ".|.","-"
countx = 1
dec_range = int((n_m[-1]-3)*0.5)
inc_range = dec_range+3
tree = n_m[-1]

for i in range(0,n_m[0]):
    
    mat_line = (hori*dec_range) + (verti*countx) + (hori*dec_range)
    print(mat_line)
    tree-=6
    if tree == 3:
        break
    countx+=2
    dec_range-=3 
    
print("Welcome".center(n_m[-1], "-"))

for i in range(0,n_m[0]):

    mat_line = (hori*dec_range) + (verti*countx) + (hori*dec_range)
    if len(mat_line)!= n_m[-1]:
        break
    else:
        print(mat_line)
        dec_range+=3
        countx-=2


