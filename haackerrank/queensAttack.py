# #in
#dan nini adalah solusi yang menurut saya sangat cerdas dan cantik
def queensAttack(n, k, r_q, c_q, obstacles):
    u = n - r_q
    d = r_q-1
    r = n - c_q
    l = c_q-1
    #menentukan banyak buah yang bisa diserang oleh ratu di sepanjang diagonal
    ru = min(u, r) 
    rd = min(r,d)
    lu = min(l,u)
    ld = min(l,d)
    for o in obstacles:
        if o[1] == c_q:
            if o[0] < r_q:
                d = min(d, r_q-1-o[0])
            else:
                u = min(u, o[0]-r_q-1)
        elif o[0] == r_q:
            if o[1] < c_q: 
                l = min(l, c_q-1-o[1])
            else: 
                r = min(r, o[1]-c_q-1)
        elif abs(o[0]-r_q) == abs(o[1]-c_q):
            if o[1]>c_q:
                if o[0]>r_q: 
                    ru = min(ru, o[1]-c_q-1)
                else: 
                    rd = min(rd, o[1]-c_q-1)
            else:
                if o[0]>r_q: 
                    lu = min(lu, c_q-1-o[1])
                else: 
                    ld = min(ld, c_q-1-o[1])
                
    return u + d + r + l + ru + rd + lu + ld

print(queensAttack(5, 3, 4, 3, [[5,5], [4,2], [2,3]]))