import torch
import torch_directml
from torch_geometric.data import Data
import time



device = torch_directml.device()
print(device)
#device = torch.device('cpu')

def create_graph(num_nodes,num_atriburtes,num_edges):
    edge_index = torch.randint(0, num_nodes, (2, num_edges), dtype=torch.long)
    x = torch.randn((num_nodes, num_atriburtes))
    return Data(x=x, edge_index=edge_index)

data = create_graph(1000,10**4,500).to(device)
t_x = torch.randn((1,data.x.shape[1])).to(device)

print(data)

repeats = 10**4
start = time.perf_counter()
for i in range(repeats):
    result = data.x * t_x
print(time.perf_counter()-start)

