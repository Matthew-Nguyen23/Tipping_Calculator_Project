
print("Welcome to the tipping calculator!")
thetotal = float(input("What was the total bill?"))
thetip = int(input("How much would you like to give? 10, 12, or 15?"))
thesplit = int(input("How many people to split the bill?"))


tip_percent = (thetip / 100)
totalamount_tip = (tip_percent * thetotal)
totalamount = (totalamount_tip + thetotal)
bill_per_person = (totalamount / thesplit)
finalamount = round(bill_per_person, 2)
finalamount = "{:.2f}".format(bill_per_person)

print(f"Each Person Should Pay Around ${finalamount}")