print("welcome to tip calculator")
total_bill=float(input("what wastotal bill$"))
total_perc=int(input("what should be percentage 10,13,15"))
total_div=int(input("how many peopleto split"))
total_tip=total_bill* (total_perc/100)

final = (total_bill + total_tip)

each = final/total_div
print(f"each person should pay {each}")
