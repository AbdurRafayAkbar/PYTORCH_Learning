import torch

x=torch.tensor([1,2,3])
print(f"x datatype => {x.dtype}")

x=torch.dtype(torch.float32)
print(f"x when changed datatype => {x}")

x.to(torch.float64)
print(f"x when changed datatype using to(torch.float64) => {x}")