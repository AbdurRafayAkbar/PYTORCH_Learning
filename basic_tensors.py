#Creating A tensor
import torch
a=torch.empty(2,3)
print(f"empty => {a}")
b=torch.zeros(2,3)
print(f"zeros => {b}")

c=torch.ones(2,3)
print(f"ones => {c}")

d=torch.rand(2,3)
print(f"random => {d}")

torch.manual_seed(100)
e=torch.rand(2,3)
print(f"random with seed => {e}")