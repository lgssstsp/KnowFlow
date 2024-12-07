## Comparision of general RAG and our designed retrive strategies
If the query we provide is to select the appropriate operation from a series of related operations, the general RAG approach often selects samples from the knowledge base based on overall semantics. However, these samples may differ significantly from our data and task. In contrast, the post-processing strategy of our designed retrieval strategy ensures that the retrieved samples are relevant to both the task and the dataset.

Query:
```
        You are provided with a set of operations $OPERATIONS_SET: ['MessagePassing', 'SimpleConv', 'GCNConv', 'ChebConv', 'SAGEConv', 'CuGraphSAGEConv', 'GraphConv', 'GravNetConv', 'GatedGraphConv', 'ResGatedGraphConv', 'GATConv', 'CuGraphGATConv', 'FusedGATConv', 'GATv2Conv', 'TransformerConv', 'AGNNConv', 'TAGConv', 'GINConv', 'GINEConv', 'ARMAConv', 'SGConv', 'SSGConv', 'APPNP', 'MFConv', 'RGCNConv', 'FastRGCNConv', 'CuGraphRGCNConv', 'RGATConv', 'SignedConv', 'DNAConv', 'PointNetConv', 'GMMConv', 'SplineConv', 'NNConv', 'CGConv', 'EdgeConv', 'DynamicEdgeConv', 'XConv', 'PPFConv', 'FeaStConv', 'PointTransformerConv', 'HypergraphConv', 'LEConv', 'PNAConv', 'ClusterGCNConv', 'GENConv', 'GCN2Conv', 'PANConv', 'WLConv', 'WLConvContinuous', 'FiLMConv', 'SuperGATConv', 'FAConv', 'EGConv', 'PDNConv', 'GeneralConv', 'HGTConv', 'HEATConv', 'HeteroConv', 'HANConv', 'LGConv', 'PointGNNConv', 'GPSConv', 'AntiSymmetricConv', 'DirGNNConv', 'MixHopConv']. Additionally, the user's preferences for specific operations are outlined in their task plan $TASK_PLAN: {'Learning_tasks_on_graph': 'Node-level', 'Learning_task_types': 'Classification', 'Evaluation_metric': 'Accuracy', 'Preference': 'None', 'Data': 'actor', 'graph_structural_analysis': {'num_nodes': 7600, 'num_edges': 33544, 'num_node_features': 931, 'num_classes': 5, 'avg_node_degree': 3.9498684406280518, 'max_node_degree': 73.0, 'min_node_degree': 0.0, 'diameter': 12, 'graph_density': 0.0010395758444670697, 'avg_shortest_path_length': 4.109739162049862}}.
        Your task is to identify and select the appropriate operations from the set of operations $OPERATIONS_SET that align with the user's preferences specified in the task plan 
        Ensure the selected operations are accurately extracted from the provided set, combining both user-specified preferences and your recommended choices.
        It is mandatory to select at least four operations that you consider the most useful for the task.
        Your output should strictly adhere to the Python list format. The output must be a Python list containing exactly three names of the operations, and no additional text or characters should be included.
```

Sample retrieved by the general RAG:
```
{
    "Task Description": "Leaderboards for Link Property Prediction",
    "Dataset Name": "ogbl-ddi",
    "Method": "GIDN@YITU",
    "Test Accuracy": "0.9542 +- 0.0000",
    "Validation Accuracy": "0.8258 +- 0.0000",
    "Parameters": "3,506,691",
    "Hardware": "DepGraph@SCTS/CGCL",
    "Paper Summary": "The paper introduces a novel model called the **Graph Inception Diffusion Network (GIDN)**, designed for efficient link prediction in knowledge graphs. The core idea behind GIDN is to enhance graph diffusion processes across various feature spaces while minimizing computational complexity.\n\n### Model Design Aspects:\n\n1. **Graph Diffusion Mechanism:**\n   - GIDN encapsulates graph diffusion to represent information about nodes' neighborhoods more effectively than the original graph structure.\n   - It uses a matrix representation for each target prediction, capturing the proximity information of nodes.\n   - The model incorporates small-hop nodes and learnable generalized weighting coefficients, allowing for multi-layer generalized graph diffusion in diverse feature spaces.\n\n2. **Inception Module:**\n   - To address the computational challenges of deeper models, GIDN utilizes the inception module. \n   - This module allows the model to capture a rich set of features without the excessive computation typically associated with deeper networks.\n   - It enhances adaptability for training with larger datasets while managing computational resources efficiently.\n\n3. **Data Augmentation:**\n   - The method also includes data augmentation strategies focusing on nodes and edges within the graph structure.\n   - A notable technique involves using random walks to remove edges between nodes with differing labels while forming connections among nodes with the same labels.\n\n4. **Computational Efficiency:**\n   - GIDN is designed to strike a balance between accuracy and computational speed, leveraging lower complexity in its calculations, which is vital for handling large-scale knowledge graphs.\n\nOverall, GIDN's architecture emphasizes efficient computation and effective feature extraction while maintaining the ability to model complex relationships in knowledge graphs."
}
```

Sample retrieved by our retrieve strategy:
```
{
    "name": "FAConv",
    "description": "The Frequency Adaptive Graph Convolution operator from the \"Beyond Low-Frequency Information in Graph Convolutional Networks\" paper.",
    "link": "../generated/torch_geometric.nn.conv.FAConv.html#torch_geometric.nn.conv.FAConv",
    "paper_link": "https://arxiv.org/abs/2101.00797",
    "paper_name": "\"Beyond Low-Frequency Information in Graph Convolutional Networks\"",
    "Model design and experimental setup": {
        "GNN_Design": {
            "agg_ops": "Low-pass and high-pass filters to adaptively aggregate different frequency signals using a self-gating mechanism.",
            "skip_connections": "Adaptive integration of raw features with aggregated signals helps retain additional information.",
            "layer_info_fusion": "Layers aggregate low-frequency signals from similar-class neighbors and high-frequency signals from different-class neighbors.",
            "num_layers": "Configurable; experiments showed performance analysis across different depths.",
            "hyperparameters": "Includes a scaling parameter \u03b5, dropout, learning rate, and weight decay. Exact settings vary per dataset.",
            "activation": "Uses a tanh function within the self-gating mechanism."
        },
        "Experimental_Setup": {
            "datasets": "Cora, Citeseer, Pubmed, Chameleon, Squirrel, and Actor networks.",
            "dataset_summary": "Assortative: Cora, Citeseer, Pubmed with publication citations. Disassortative: Chameleon, Squirrel with Wikipedia pages and Actor co-occurrence network.",
            "baseline": "Comparison with models like SGC, GCN, GWNN, GIN, GAT, MoNet, APPNP, and Geom-GCN.",
            "performance_comparisons": "FAGCN showed superior performance across multiple datasets, outperforming other models in both assortative and disassortative network analysis."
        }
    },
    "Paper Summary": "The paper \"Beyond Low-frequency Information in Graph Convolutional Networks\" discusses the design of a novel graph convolutional network model called Frequency Adaptation Graph Convolutional Networks (FAGCN). This model specifically aims to adaptively integrate both low-frequency and high-frequency signals from node features to enhance learning effectiveness in various network types.\n\n### Key Methods Discussed in the Paper:\n\n1. **Separation of Frequency Signals:**\n   - FAGCN employs enhanced low-pass and high-pass filters to separate low-frequency and high-frequency signals from raw node features. The filters are mathematically defined and help in delineating the different contributions each signal type makes to the node representations.\n\n2. **Self-Gating Mechanism:**\n   - A self-gating mechanism is developed within FAGCN to adaptively determine the importance or proportion of low-frequency and high-frequency signals during the message passing phases. This is realized through coefficients that learn from both node features and their neighbors, allowing the model to dynamically adjust the filtering based on the network context.\n\n3. **Adaptive Aggregation:**\n   - FAGCN aggregates signals from neighboring nodes using different coefficients for low-frequency and high-frequency contributions, which prevents the over-smoothing problem often encountered in existing GNNs. The mathematical formulation includes normalizing the contributions based on the node's degree to manage representation sizes effectively.\n\n4. **Architecture Framework:**\n   - The architecture of FAGCN uses a multi-layer perceptron (MLP) for non-linear transformations and propagates aggregated representations through several layers. This modular design allows for flexible adaptation to signal types without prior knowledge of network structure (assortative or disassortative).\n\n5. **Expressive Power:**\n   - The paper theorizes that FAGCN generalizes existing GNNs and possesses superior expressive power due to its ability to adjust the filtering and aggregation of low- and high-frequency signals, thus allowing for better performance across different network types.\n\nIn summary, FAGCN represents a significant advancement in graph neural network design, focusing on the dual adaptation of frequency signals to optimize node representation learning while mitigating issues like over-smoothing. This adaptive mechanism allows for more nuanced learning strategies tailored to the characteristics of real-world networks."
}
```