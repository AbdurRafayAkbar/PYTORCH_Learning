import torch

if torch.cuda.is_available():
    print("GPU is Available")
    print(f"using  GPU {torch.cuda.get_device_name(0)}")
else:
    print("No GPU available using CPU " )