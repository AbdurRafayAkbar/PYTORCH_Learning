import torch

#equation is y=x**2 , z=sin(y)

x=torch.tensor(4.0,requires_grad=True)

y=x**2
z=torch.sin(y)
# print(x)
# print(y)
# print(z)
z.backward()
print(x.grad)
# print(y.grad) we cant do that because y is not a leaf node, so it does not have a grad attribute.
