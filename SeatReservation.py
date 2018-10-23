def solution(N, S):
    seat = "0ABCDEFGHJK"
    r = S.split()
    r = sorted(r)
    print(r)
    res = 0
    if len(S) == 0:
        return N *3
    else:
        p = 1
        while (p<=N):
            for x in range(1,len(seat)):
                count = 0
                z = 0
                if z == 1:
                    res +=1
                    count = 0

                if str(p) + seat[x] not in r:
                    if str(p) + seat[x] == str(p)+"D" or str(p)+"H":
                        count = 1
                    count += 1
                    if count < 4:
                        z = 1
                if str(p) + seat[x]  in r :
                    count += 0
            p +=1
        return res

print(solution(1,"1F 2C 3D 1A"))
