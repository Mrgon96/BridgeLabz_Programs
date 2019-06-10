import random
class CouponGenrator:

    @staticmethod
    def coupon_number():
        Number = int(input('Enter the Range for Coupons: '))
        count = 0
        
        distict=[]
        for i in range (1,Number+1):
            random_coupon = random.randrange(1,Number)
            if random_coupon not in distict:    
                distict.append(random_coupon)
                count += 1   

        print(distict)
        print('Total Random Numbers Generated is :',count)

c = CouponGenrator()
c.coupon_number()
