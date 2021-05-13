iH,iW,iA,iB = [int(x) for x in input().split()]
iD = 10**9+7 #法

iLBoxW=iB-1
iLBoxH=iH-iA-1
iRBoxW=iW-iB-1
iRBoxH=iH-1
#iMax = iH+iW-2
iMax = max(iLBoxW+iLBoxH,iRBoxW+iRBoxH)

#nCr = n!/r!(n-r)!

#二分累乗法 iDを法として
def fBiPow(iX,iN,iD):
    iY = 1
    while iN > 0:
        if iN % 2 == 0:
            iX = iX * iX % iD
            iN = iN // 2
        else:
            iY = iX * iY % iD
            iN = iN - 1
    return iY

#階乗(iDを法とした)の配列
aM = [1]*(iMax+1)
for i in range(1,iMax+1):
    aM[i]=aM[i-1]*i %iD
#各階乗のiDを法とした逆元の配列
aInvM = [1]*(iMax+1)
aInvM[iMax] = fBiPow(aM[iMax],iD-2,iD)
for i in range(iMax,0,-1):
    aInvM[i-1]=aInvM[i]*i % iD

iRet = 0
for iL in range(0,iLBoxH+1):
    iRet += (aM[iL+iLBoxW]*aInvM[iL]*aInvM[iLBoxW]) % iD * (aM[iRBoxW+iRBoxH-iL]*aInvM[iRBoxW]*aInvM[iRBoxH-iL])%iD
    iRet %= iD
iRet %= iD
print(iRet)
