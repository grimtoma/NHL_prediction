import torch
import torch_directml
from torch_geometric.data import Data



device = torch_directml.device()
edge_index = torch.tensor([[0, 1],
                           [1, 0],
                           [1, 2],
                           [2, 1]], dtype=torch.long)
x = torch.tensor([[-1], [0], [1]], dtype=torch.float)

data = Data(x=x, edge_index=edge_index.t().contiguous()).to(device)
for i in range(10**5):
    result = data.x * torch.tensor([[5],[1],[2]]).to(device)
    #print(data.x.shape)
print(result)
