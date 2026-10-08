import torch

a=torch.tensor([1,2])
b=torch.tensor([3,4])

print(f"a => {a}")
print(f"b => {b}")
#add
print(f"Addition of a and b => {torch.add(a,b)}")
#subtraction
print(f"subtraction of a and b => {torch.sub(a,b)}")
#multiplication
print(f"Multiplication of a and b => {torch.mul(a,b)}")
#division
print(f"Division of a and b => {torch.div(a,b)}")
#power
print(f"Power of a and b => {torch.pow(a,b)}")
#mod
print(f"Mod of a and b => {torch.remainder(a,b)}")

#----------------------------------------------#

#absolute_value
print(f"absolute value of a => {torch.abs(a)}")
#Negative
print(f"Negative of a => {torch.neg(a)}")
#Round
print(f"Round of a => {torch.round(a)}")
#clamp

print(f"clamp of a and b => {torch.clamp(b, min=0.2,max=2.5)}")