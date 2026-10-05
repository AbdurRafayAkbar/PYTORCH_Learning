#Creating A tensor
import torch
#All values will be uninitialized
a=torch.empty(2,3)
print(f"empty => {a}")
#All values will be 0
b=torch.zeros(2,3)
print(f"zeros => {b}")
#all values will be 1
c=torch.ones(2,3)
print(f"ones => {c}")
#Values will change for every run
d=torch.rand(2,3)
print(f"random => {d}")
#Values will reamain same for the same seed value
torch.manual_seed(100)
e=torch.rand(2,3)
print(f"random with seed => {e}")

#
f=torch.arange(0,10,2) #start, end, step
print(f"arange => {f}")

g=torch.linspace(0,10,5) #start, end, number of points
print(f"linspace => {g}")

h=torch.eye(3) #Identity matrix of size 3x3
print(f"eye => {h}")