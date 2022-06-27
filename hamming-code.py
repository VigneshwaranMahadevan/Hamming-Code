inputString=input()

answer=""

for blockIndex in range(len(inputString)//10):

    hexBlock40bit=inputString[10*blockIndex:10*blockIndex+10] #taking the 10 character long hexadecimal string

    binBlock40bit=bin(int(hexBlock40bit, 16))[2:].zfill(40)[:-1] #converting the hexadecimal characters to their binary representation

    bitsUnderHammingbit=[]      #for debugging
    bitsUnderSetHammingbit=[]   #for debugging
    setHammingBits=[]           #find the index of the error bit

    for hammingBit in range(6):  # hammingBit is for the hamming codes at 1,2,4,8,16 and 32
        bitsUnderHammingbit.append([])
        isHammingBitSet=0       #Checking for even parity
        for j in range(len(binBlock40bit)): # j is the index of the binBlock40bit string
            if((j>>hammingBit)&1==1):
                bitsUnderHammingbit[-1].append(j)
                isHammingBitSet^=int(binBlock40bit[j]) #xor to get even parity

        if(isHammingBitSet==1): # if hammingBit is set 
            bitsUnderSetHammingbit.append(bitsUnderHammingbit[-1]) #Append all set bits covered by hamming code at 2^hammingBit - debug
            setHammingBits.append(hammingBit) #Append set hamming bits to find the error bit
            
    if(setHammingBits==[]): #if setHammingBits is empty , no error
        ans=-1
    else:
        ans=0

    for hammingBit in setHammingBits:   #Finding the error bit
        ans+=2**hammingBit 
    
    if(ans!=-1): #If error is there
        binBlock40bit=binBlock40bit[:ans]+str(1-int(binBlock40bit[ans]))+binBlock40bit[ans+1:] #now binBlock40bit has the correct 40bit block

    blockData=""
    for asciiCharIdx in range(len(binBlock40bit)):
        if(asciiCharIdx in [0,1,2,4,8,16,32]):
            continue
        else:
            blockData+=binBlock40bit[asciiCharIdx] #blockData has the data (converted from 40 bit to 32 bit)

    blockAnswer=""
    for blockNumber in range(len(blockData)//8): #blockData has 32 bits
        data8Bit=blockData[8*blockNumber:8*blockNumber+8] #taking 8 bits at a time
        asciiVal=0
        for charIdx in range(len(data8Bit)):
            if(data8Bit[7-charIdx]=="1"):
                asciiVal+=2**(j) #finding the ASCII value of the 8 bits
        blockAnswer+=chr(asciiVal) #Appending the ASCII character

    answer+=blockAnswer #Append block answer to final Answer

print(answer)




