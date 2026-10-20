import torch

def matrixmul(a, b) -> torch.Tensor:
    """
    Multiply two matrices using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2D tensor of shape (m, n) or a scalar tensor -1 if dimensions mismatch.
    """
    a_t = torch.as_tensor(a, dtype = torch.float)
    b_t = torch.as_tensor(b, dtype = torch.float)
    #dim check
    if a_t.size(dim=1) != b_t.size(dim=0):
        return torch.tensor(-1)

    val = a_t @ b_t
    
    return val
