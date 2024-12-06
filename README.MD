# Environment
    environment.yml

# Directory Structure
    framework/ 
    ├── F2GNN/ # automl source code 
    ├── LRGNN/ # automl source code 
    ├── ProfCF/ # automl source code 
    ├── all-MiniLM-L6-v2/ # Word embedding model, can be downloaded from https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 
    ├── knowledge_base/ # Knowledge base file directory 
    ├── manager.py # Manager agent 
    ├── data.py # Data agent 
    ├── configuration.py # Configuration agent 
    ├── search.py # Evaluation agent 
    ├── tune.py # Evaluation agent 
    ├── response.py # Evaluation agent 
    ├── knowledge.py # Knowledge agent 
    ├── main.py # Entry point file 
    ├── llm_api.py # LLM API call 
    └── retrive.py # Retriever

# Run Example
    cd framework
    python main.py --dataset actor --knowledge_types ogb pyg_info_nn new_paper --knowledge_percentage 1.0
