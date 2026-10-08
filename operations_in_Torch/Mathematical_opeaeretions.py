#scalar OPeartions

import torch


a=torch.tensor([1,2,3,4])
b=torch.tensor([5,6,7,8])
#addition
print(f"Addition of a and b => {a+b}")
#subtraction
print(f"Subtraction of a and b => {a-b}")
#multiplication
print(f"Multiplication of a and b => {a*b}")
#division
print(f"Division of a and b => {a/b}")  
#Int division
print(f"Int Division of a and b => {a//b}")
#power  
print(f"Power of a and b => {a**b}")
#mod
print(f"Mod of a and b => {b%a}")