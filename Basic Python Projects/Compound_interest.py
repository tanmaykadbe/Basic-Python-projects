Amount = 0
Time  = 0
Rate = 0

while Amount <= 0:
    Amount = float(input("Please enter the Amount: "))
    if Amount <= 0:
        print("Amount cannot be zero")
while Time <= 0:
    Time = float(input("Please enter the Time: "))
    if Time <=0 :
     print("The Time cannot be zero")
while Rate <= 0:
    Rate = float(input("Please enter the Rate: "))
    if Rate <=0 :
       print("The Rate cannot be zero")

total = Amount * pow((1 + Rate / 100), Time)
print(f"The Balance after {Time} Year/s will be {total}")