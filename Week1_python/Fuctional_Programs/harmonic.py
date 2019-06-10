N = input('Enter Number : ')

def harmonic(N):
        harmonic1 = 1.00
        for i in range(2,N+1):
                harmonic1 += 1/i
        return harmonic1        

if __name__ == "__main__" : 
        print(round(harmonic(N),5))
