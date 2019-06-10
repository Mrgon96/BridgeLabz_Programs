def SwapNibble(x):
    print(x & 0x0F)
    print(x & 0xF0)
    return ( (x & 0x0F) << 4 | (x & 0xF0) >> 4)


x=100
print(SwapNibble(x))    