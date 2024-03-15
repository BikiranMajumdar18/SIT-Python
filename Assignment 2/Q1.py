'''If cost price and selling price of an item is input through the keyboard, 
write a program to determine whether the seller has made profit or incurred loss.
Also determine how much profit he made or loss he incurred.'''

sp = int(input("Enter the SP: "))
cp = int(input("Enter the CP: "))

profit = sp - cp
loss = cp - sp

if sp > cp:
    print("Profit: ", profit)
else:
    print("Loss: ", loss)
