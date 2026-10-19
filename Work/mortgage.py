# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months  = 1
extra_payment_start_month = 12*5+1
extra_payment_end_month = (12*4 ) + extra_payment_start_month
extra_payment = 1000
index = 1
while principal > 0:  
    extra = 0
    principal = principal* (1+rate/12)
    if extra_payment_start_month <=months <extra_payment_end_month :
        extra = 1000
    
    
    total_paid += payment + extra
    principal -= payment
    principal -= extra
    months += 1    
    print(index ,total_paid , principal )
    index += 1
print('Total paid', total_paid , 'over' , months-1, 'months')
