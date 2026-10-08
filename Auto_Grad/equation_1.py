import torch

# equation is y=x**2

x=torch.tensor(2.0,requires_grad=True)

y=x**2

y.backward()
print(x.grad)