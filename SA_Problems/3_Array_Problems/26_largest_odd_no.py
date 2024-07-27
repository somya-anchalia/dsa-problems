def largestOddNumber(num: str) -> str:
    n=len(num)
    ans=n-1
    while ans>=0 and int(num[ans])%2==0:
        ans-=1

    return num[:ans+1]

largest_odd = largestOddNumber("35427")
print(largest_odd)