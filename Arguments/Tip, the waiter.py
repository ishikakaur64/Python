def total_calc(bill_amount,tip_perc=10):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print("Total Amount",total)
total_calc(4000)