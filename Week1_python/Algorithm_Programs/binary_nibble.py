def SwapNibble(x): #define function
    return ( (x & 0x0F) << 4 | (x & 0xF0) >> 4)#Shfting and swaping of bits



x=100 #integer you want to convert
print(SwapNibble(x))  #print result  