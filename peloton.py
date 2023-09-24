#!/usr/bin/python3

# A solution to Fiddler on the Proof posted on 09-22-2023

# Tells whether equilateral triangle with length n can be
# transformed into an almost-rhombus or complete-rhombus
# n = number of riders (or dots) at base of triangle
# check_complete = flag to print if rhombus is complete
def peloton_game(n, check_complete):
    features=[]
    trunc_sum=n
    for i in range(1,n-1):
        summ=0
        k = 2 + i-1
        while n-k > 0 and summ < trunc_sum:
            summ += (n-k)
            k += 1
        if summ == trunc_sum:
            top_sum = ((n-i)*(n-i+1)) // 2
            nriders = top_sum + trunc_sum
            if check_complete and trunc_sum == (((n-i-1)*(n-i)) // 2):
                print("Complete Rhombus! n=%d, width=%d, #riders=%d" %
                                                      (n,n-i,nriders))
            features.append((n,n-i,nriders))
        trunc_sum += (n - i) 
    return features

if __name__ == "__main__":
    # number of formations
    for nf in range(1, 4): 
        print("\nNumber of distinct formations = %d" % nf)
        # number of riders at base of initial peloton
        for nr in range(5, 100): 
            feats = peloton_game(nr, False)
            if nf == len(feats):
                for f in feats:
                    print("Rhombus:n=%d, width=%d, #riders=%d" % f)



