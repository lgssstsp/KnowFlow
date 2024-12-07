##  Comparision of different prompts and their corresponding outputs
The design of the prompts takes into account the objective of each step in the framework. We design the prompts based on the required input information and the expected output.
Different prompts can have some impact on the agent, but it does not cause a significant difference. Below are examples of different prompts and their corresponding outputs:

Prompt 1:
```
As a researcher specialized in graph-structured data, you are tasked with interpreting user requests related to graph learning. Your objective is to analyze the user's request, provided here: I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page.. 
Your analysis should deconstruct the request into several key components and present your findings in the form of a Python dictionary. Specifically, identify and articulate the following elements:

1. Learning_tasks_on_graph: The learning task on graph can only be node-level, link-level, or graph-level.
Node-level: If the task aims to predict or classify attributes or behaviors of individual nodes based on their features or their relationships to other nodes, it is a node-level task. For instance, identifying the category of a paper in a citation network based on its content and citation links.
Link-level: If the task focuses on the relationships between nodes, such as predicting the existence, strength, or quality of these connections, classify it as a link-level task. An example is predicting the rating a user gives to a movie, where the prediction is about the edge (rating) connecting two types of nodes (users and movies), which is a regression problem.
Graph-level: If the task involves understanding or predicting properties that describe entire graphs or significant subgraphs, it is a graph-level task. Examples include classifying whole graphs into categories or predicting a property of a chemical compound represented as a graph.
Review the user request carefully and determine whether the task is node-level, link-level, or graph-level. Provide your analysis in a structured Python dictionary format, categorizing the task correctly based on the provided details and emphasizing the focus of the learning task.

2. Learning_task_types: Ascertain whether the task is a regression or classification problem, or any other type of learning task. Clarify the nature of the learning challenge.

3. Evaluation_metric: Identify the evaluation metric that is desired or implied in the user's request for gauging the success of the learning task.
If the task is a classification problem, such as predicting categories or labels or domains, suggest metrics like Accuracy, Precision, Recall, F1-Score or others.
If the task is a regression problem, such as predicting numerical values, recommend metrics like Mean Squared Error (MSE), Root Mean Squared Error (RMSE) or others.
In cases where the user has not specified a preference for any metric, provide a rationale for your recommended metric based on the task's details and the desired outcomes. 

4. Preference: Note any specific preferred operations that the user mentions. 
If no preferences are stated, acknowledge this with 'None'.

5. Data: Only the dataset name.
Ensure that each component is distinctly identified and described, providing a clear and actionable breakdown of the user's request, and the format of your outputs should be a dictionary.

You should provide a Python dictionary as the output with a flat structure (no nested dictionaries), containing only the above keys. 
```
and its results:
```
{
    "Learning_tasks_on_graph": "Node-level",
    "Learning_task_types": "Classification",
    "Evaluation_metric": "Accuracy",
    "Preference": "None",
    "Data": "actor"
}
```

Prompt 2:
```
**Role**: Graph Data Scientist
**Task**: Analyze the graph-related user query provided here: I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page.. Break down the request into key components and articulate these in a Python dictionary.

1. **Graph_Task_Level**:
   - **Node**: Involves individual node attributes or behaviors prediction/classification.
   - **Link**: Concerns relationships between nodes, focusing on regression analysis like rating predictions.
   - **Graph**: Pertains to properties of entire graphs or significant subgraphs, like classifying molecular structures.
   Classify the request accordingly.

2. **Learning_Challenge**: Clarify whether the task is classification, regression, or other forms of graph learning.

3. **Performance_Metrics**:
   - Classification: Accuracy, Precision, Recall, F1-Score or others.
   - Regression: MSE, RMSE or others.
   Recommend appropriate metrics based on the task's nature.

4. **Preferences**: Record any specific methodologies preferred by the user or state 'None'.

5. **Dataset_Info**: Provide only the name of the dataset involved.

**Output Format**: Return a flat Python dictionary containing only the above categories.
```
and its results:
```
{
    "Graph_Task_Level": "Node",
    "Learning_Challenge": "Classification",
    "Performance_Metrics": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Preferences": "Graph Neural Networks",
    "Dataset_Info": "actor"
}
```

Prompt 3:
```
**Position**: Expert in Graph-Based Learning
**Objective**: Decompose the following user input concerning graph learning: I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page.. Output your findings as a Python dictionary.

1. **Task_Dimension**:
   - **Node**: Tasks like predicting node characteristics or classifications.
   - **Link**: Tasks focusing on node connections, suitable for regression analyses.
   - **Graph**: Tasks involving overall graph characteristics or classifications.
   Identify and classify the task's scope based on the input.

2. **Task_Nature**: Identify if the task is aimed at regression, classification, or other specific goals.

3. **Evaluation_Standards**:
   Provide a metric based on the task description.

4. **User_Specifications**: Note down any specific techniques or operations preferred by the user, or mention 'None'.

5. **Data_Reference**: Mention only the dataset name.

**Delivery**: Supply a non-nested Python dictionary that encapsulates all specified elements.
```
and its results:
```
{
    "Task_Dimension": "Node",
    "Task_Nature": "Classification",
    "Evaluation_Standards": "Node classification accuracy",
    "User_Specifications": "Graph neural networks",
    "Data_Reference": "actor"
}
```


Prompt 4:
```
**Role**: Specialist in Graph Learning
**Objective**: Thoroughly dissect and analyze the user's graph learning request here: I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page.. Present your analysis in a non-nested Python dictionary format.

1. **Task_Classification**:
   - **Node-Level**: Targets individual nodes for predicting behaviors or attributes.
   - **Link-Level**: Examines connections between nodes, suitable for regression tasks like ratings.
   - **Graph-Level**: Involves whole graphs or major subgraphs, useful for broad classifications.
   Classify the task appropriately.

2. **Type_of_Learning**: Determine whether the task involves classification, regression, or others.

3. **Metrics_for_Evaluation**:
   - Classification tasks: Suggest Accuracy, Precision, Recall, F1-Score, or others.
   - Regression tasks: Suggest MSE, RMSE, or others.
   Choose metrics that best fit the learning task described.

4. **Operational_Preferences**: Document any specific preferences or operations requested by the user, or note 'None'.

5. **Dataset_Details**: List the name of the dataset only.

**Expected Output**: Produce a straightforward Python dictionary detailing the above points.
```
and its results:
```
{
    "Task_Classification": "Node-Level",
    "Type_of_Learning": "Classification",
    "Metrics_for_Evaluation": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Operational_Preferences": "None",
    "Dataset_Details": "actor"
}
```


Prompt 5:
```
**Role**: Graph Learning Analyst
**Task**: Break down this graph learning query: I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page. into structured elements. Output these elements as a Python dictionary.

1. **Task_Levels**:
   - **Node**: Focuses on individual nodes for classification or prediction.
   - **Link**: Targets connections between nodes for regression analyses.
   - **Graph**: Deals with entire graphs or substantial subgraphs for classification.
   Categorize the task based on this framework.

2. **Learning_Type**: Classify the task as either regression, classification, or specify other.

3. **Metrics**:
   - For classifying: Recommend Accuracy, Precision, Recall, F1-Score or others.
   - For regressing: Recommend MSE, RMSE or others.
   Justify your metric recommendation based on task details.

4. **Preferences**: Note any user preferences for specific methodologies, or indicate 'None'.

5. **Dataset**: Simply state the name of the dataset used.

**Output**: Present your findings in a clean, flat Python dictionary.
```
and its results:
```
{
    "Task_Levels": "Node",
    "Learning_Type": "Classification",
    "Metrics": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Preferences": "None",
    "Dataset": "actor"
}
```

Prompt 6:
```
**Role**: Expert in Graph Data Science
**Objective**: Disassemble the user's graph learning query, provided as I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page., into fundamental components. Document these in a Python dictionary.

1. **Graph_Task_Scope**:
   - **Node**: For tasks like predictions about individual nodes.
   - **Link**: For tasks regarding the relationships or ratings between nodes.
   - **Graph**: For tasks concerning overall properties of graphs or subgraphs.
   Determine the task's level based on these categories.

2. **Learning_Objective**: Specify whether the task is for classification, regression, or other types.

3. **Evaluation_Criteria**:
   - For classifying tasks: Metrics like Accuracy, Precision, Recall, F1-Score or others.
   - For regression tasks: Metrics like MSE, RMSE or others.
   Select appropriate metrics based on the task's objectives.

4. **Specific_Preferences**: Document any methodologies specifically requested by the user, or state 'None'.

5. **Dataset_Name**: Include only the name of the dataset involved.

**Expected Output**: Return a flat Python dictionary summarizing the key components.
```
and its results:
```
{
    "Graph_Task_Scope": "Node",
    "Learning_Objective": "Classification",
    "Evaluation_Criteria": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Specific_Preferences": "Graph Neural Networks",
    "Dataset_Name": "actor"
}
```


Prompt 7:
```
As a researcher specialized in graph-structured data, you are tasked with parsing and structuring user requests related to graph learning. Your job is to decompose the user's input: I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page. into a structured Python dictionary by identifying essential elements as follows:

1. **Task_Level**: Determine the scope of the task:
   - **Node**: Directly involves node attributes or behavior.
   - **Link**: Focuses on relationships or interactions between nodes.
   - **Graph**: Addresses attributes or classifications of entire graphs or significant subgraphs.
   Classify the request based on the description provided.

2. **Task_Classification**: Establish whether the task is classification, regression, or another form.

3. **Metric_Determination**: Identify the most appropriate evaluation metrics:
   - Classification: Options include Accuracy or F1-Score or others.
   - Regression: Options include MSE or RMSE or others.
   Recommend metrics based on the learning objectives stated.

4. **Preferences_Detail**: Record any specific methodologies or preferences mentioned by the user. If unspecified, note as 'None'.

5. **Dataset_Specification**: Record only the dataset's name.

**Output Requirements**: Your findings should be presented as a non-nested Python dictionary with clearly labeled keys.
```
and its results:
```
{
    "Task_Level": "Node",
    "Task_Classification": "Classification",
    "Metric_Determination": ["Accuracy", "F1-Score"],
    "Preferences_Detail": "Graph Neural Networks",
    "Dataset_Specification": "actor"
}
```


Prompt 8:
```
As a researcher specialized in graph-structured data, your task is to carefully analyze and interpret the user's graph learning request I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page.. Produce a Python dictionary that details:

1. **Task_Type**: Classify the learning task into one of the following categories:
   - **Node-Level**: Tasks like predicting node attributes.
   - **Link-Level**: Tasks like analyzing links between nodes.
   - **Graph-Level**: Tasks involving entire graphs or major subgraphs.
   Specify the category based on the input details.

2. **Learning_Model**: Identify the model type (classification, regression, etc.) required for the task.

3. **Evaluation_Metric**: Determine suitable metrics for assessing the task's success:
   - For classification: Suggest Accuracy, Precision, Recall, F1-Score or others.
   - For regression: Suggest MSE, RMSE or others.
   Base your recommendations on the specific task requirements.

4. **User_Preferences**: List any specific methodologies or techniques preferred by the user, or indicate 'None' if no preferences are provided.

5. **Dataset_Details**: Mention only the name of the dataset involved.

**Output**: Deliver this information in a flat structured Python dictionary format.
```
and its results:
```
{
    "Task_Type": "Node-Level",
    "Learning_Model": "Classification",
    "Evaluation_Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "User_Preferences": "None",
    "Dataset_Details": "actor"
}
```


Prompt 9:
```
As a researcher specialized in graph-structured data, you are tasked to unpack and analyze the user's graph learning request I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page.. Translate your analysis into a structured Python dictionary, detailing:

1. **Task_Classification**: Determine if the learning task is aimed at classification, regression, or another specific type.
2. **Graph_Task_Level**: Define the scope of the task:
   - **Node**: Tasks regrading to  analyze individual node attributes.
   - **Link**: Tasks like studying the connections between nodes.
   - **Graph**: Tasks that consider properties of entire graphs.
3. **Evaluation_Criteria**: Select the most suitable metrics:
   - Classification tasks: Accuracy, Precision, Recall, F1-Score or others.
   - Regression tasks: MSE, RMSE or others.
4. **Dataset_Information**: State only the name of the dataset used.
5. **Preferences**: Document any specific methodologies or operations preferred by the user, or note 'None' if unspecified.

**Output Requirement**: Present your findings in a flat Python dictionary format, with each element properly categorized.
```
and its results:
```
analysis = {
    "Task_Classification": "Classification",
    "Graph_Task_Level": "Node",
    "Evaluation_Criteria": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Dataset_Information": "actor",
    "Preferences": "None"
}
```


Prompt 10:
```
As a researcher specialized in graph-structured data, break down the user's graph learning request I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page. into a structured Python dictionary, highlighting:

1. **Evaluation_Metric**: Suggest suitable metrics for assessing the task:
   - For classification tasks: Metrics like Precision, Recall, F1-Score or others.
   - For regression tasks: Metrics like MSE or RMSE.
2. **Task_Type**: Determine whether the task is classification, regression, or another type.
3. **Graph_Task_Level**: Classify the task level:
   - **Node**: Involves node-level analysis.
   - **Link**: Focuses on link-level interactions.
   - **Graph**: Pertains to overall graph properties.
4. **Preferences**: List any specific operational preferences mentioned by the user, or indicate 'None'.
5. **Data**: Simply provide the name of the dataset.

**Output Specifications**: Your findings should be formatted as a non-nested Python dictionary, with each key clearly defined.
```
and its results:
```
{
    "Evaluation_Metric": ["Precision", "Recall", "F1-Score"],
    "Task_Type": "Classification",
    "Graph_Task_Level": "Node",
    "Preferences": "None",
    "Data": "actor"
}
```


Prompt 11:
```
As a researcher specialized in graph-structured data, your objective is to deconstruct the user request I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page. for graph learning into manageable components. Format your findings into a Python dictionary as follows:

1. **Evaluation_Metric**: Identify the desired or implied evaluation metric for the task:
   - For classification: Accuracy, Precision, Recall, F1-Score or others.
   - For regression: MSE, RMSE or others.
2. **Task_Level**: Classify the scope of the task:
   - **Node**: Involves node-specific predictions.
   - **Link**: Centers on the relationships between nodes.
   - **Graph**: Encompasses entire graphs.
3. **Task_Type**: Ascertain whether the task is classification, regression, or another type.
4. **Preferences**: Note any specific preferences mentioned by the user regarding methodologies or tools.
5. **Data**: Provide only the dataset name.

**Output Format**: Your analysis should be encapsulated in a straightforward Python dictionary, ensuring clarity and actionability.
```
and its results:
```
{
    "Evaluation_Metric": "Accuracy",
    "Task_Level": "Node",
    "Task_Type": "Classification",
    "Preferences": "Graph Neural Networks",
    "Data": "actor"
}
```


Prompt 12:
```
As a researcher specialized in graph-structured data, analyze and structure the user request I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page. into a Python dictionary, prioritizing:

1. **Data**: Mention only the name of the dataset involved.
2. **Preferences**: Record any specific preferences or operations mentioned by the user. If none, specify 'None'.
3. **Task_Classification**: Identify whether the task is classification, regression, or another learning type.
4. **Graph_Task_Level**: Detail the learning task's scope:
   - **Node**: Predictions about individual nodes.
   - **Link**: Analysis of the connections between nodes.
   - **Graph**: Insights into entire graphs or significant subgraphs.
5. **Evaluation_Metric**: Choose suitable metrics based on the task:
   - For classification: Metrics like Accuracy or Precision.
   - For regression: Metrics such as MSE or RMSE.

**Output Structure**: Deliver your findings in a non-nested Python dictionary format, with keys reflecting the prioritized order.
```
and its results:
```
{
    "Data": "actor",
    "Preferences": "None",
    "Task_Classification": "classification",
    "Graph_Task_Level": "Node",
    "Evaluation_Metric": "Accuracy"
}
```


Prompt 13:
```
As a researcher specialized in graph-structured data, you are responsible for translating complex user requests into actionable graph learning tasks. Process the request I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page. and convert it into a structured Python dictionary, covering the following aspects:

1. **Dataset_Information**: Start by identifying the dataset name involved in the request.
2. **Task_Level**: Analyze and categorize the task level based on the user's description:
   - **Node**: Related to predictions at the node level.
   - **Link**: Involves relationships between nodes.
   - **Graph**: Concerns properties of entire graphs or significant subgraphs.
3. **Task_Classification**: Ascertain the type of task, whether it's classification, regression, or another form.
4. **Evaluation_Metric**: Recommend appropriate metrics for evaluating the learning task:
   - Classification tasks might use metrics such as Accuracy or F1-Score.
   - Regression tasks might use metrics like MSE or RMSE.
5. **Preferences**: Note any specific preferences for methodologies or tools mentioned by the user. If unspecified, acknowledge this with 'None'.

**Output Requirements**: Ensure your analysis is presented in a clear, non-nested Python dictionary, structured to reflect the logical flow from dataset to task specifics.
```
and its results:
```
{
    "Dataset_Information": "actor",
    "Task_Level": "Node",
    "Task_Classification": "Classification",
    "Evaluation_Metric": "Accuracy, F1-Score",
    "Preferences": "Graph Neural Networks"
}
```

Prompt 14:
```
As a researcher specialized in graph-structured data, your role is to dissect user requests related to graph learning and articulate them into a comprehensible Python dictionary. Take the input I have graph, it is saved on the dataset file: actor, 
which is an actor-only induced subgraph of the film-director-actor-writer network. 
In this graph-based dataset, nodes represent actors, and edges represent 
the co-occurrence of two actors on the same Wikipedia page. 
Node features correspond to keywords extracted from the actors' Wikipedia pages. 
The goal is to use graph neural networks to classify nodes into one of five categories 
based on the words present in an actor's Wikipedia page. and focus on delineating:

1. **Task_Type**: First, establish whether the task is aimed at classification, regression, or involves a different analytical approach.
2. **Graph_Task_Level**: Identify the granularity of the task based on the information provided:
   - **Node**: Tasks involving individual node characteristics.
   - **Link**: Tasks focusing on the connections between nodes.
   - **Graph**: Tasks examining the attributes of whole graphs.
3. **Evaluation_Metric**: Determine the most suitable evaluation metrics based on the task's nature:
   - For classification: Consider metrics like Precision, Recall, or F1-Score.
   - For regression: Opt for metrics such as MSE or RMSE.
4. **Preferences**: Capture any specific methodologies or operations preferred by the user, or clearly indicate 'None' if no preferences are provided.
5. **Data**: Conclude with the dataset's name that is pertinent to the request.

**Expected Output**: Your findings should be organized in a straightforward Python dictionary, ensuring that the structure logically flows from the type of task to the dataset details.
```
and its results:
```
{
    "Task_Type": "Classification",
    "Graph_Task_Level": "Node",
    "Evaluation_Metric": ["Precision", "Recall", "F1-Score"], 
    "Preferences": "Graph Neural Networks", 
    "Data": "actor" 
}
```