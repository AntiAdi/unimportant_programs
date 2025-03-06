print("TICKET PRICING")
print("First Class : 870 $\nSecond Class : 100.42 $\nThird Class : 7 $")

total_price = 0.00



print("\nNumber of First Class tickets ?")
total_price += (float(input()))*870

print("Number of Second Class tickets ?")
total_price += (float(input()))*(100.42)

print("Number of Third Class tickets ?")
total_price += (float(input()))*7

print(f"Total Cost of tickets is {total_price:.1f} $")