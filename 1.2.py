total=10 
f=int (input ('Введіть значення')) 
i=0 
while i<f:
    total=total*0.10+total
    i=i+1
print("Залишилось", total)