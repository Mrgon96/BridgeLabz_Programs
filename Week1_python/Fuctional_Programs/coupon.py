#import random module
import random
class CouponGenrator:

    @staticmethod
    def coupon_number():
        #taking user input
        Number = int(input('Enter the Range for Coupons: '))
        #count for unique values
        count = 0
        #distint values list
        distict=[]


        for i in range (1,Number+1):
            #generate random values
            random_coupon = random.randrange(1,Number)

            #checking for value not in array
            if random_coupon not in distict:    
                distict.append(random_coupon)
                count += 1   

        #print results
        print(distict)
        print('Total Random Numbers Generated is :',count)


#create class object
c = CouponGenrator()
c.coupon_number()
