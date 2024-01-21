import torch

def main():
    print(f"ID of current CUDA device:{torch.cuda.current_device()}")    
    print(f"Name of current CUDA device:{torch.cuda.get_device_name(torch.cuda.current_device())}")
    return torch.cuda.is_available()

if __name__ == '__main__':
    main()