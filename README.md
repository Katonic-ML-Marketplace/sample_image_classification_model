# Test Image Classification Model

This repo contain the example and sample files to Deploy a Custom Image Classification Model.

## Deployment Requirements

- `labels_file.json`: This file required to create feedback or performance metrics for binary or multi-class classification.

***Please note that these classes should be mapped classes of original classes (eg. ["cat", "dog] will be [0, 1] or [1, 2]) for both binay and multi-class problems.***

```python
# labels_file.json for multi-class classification, you can define your own classes here
{"labels": [1, 2, 3, 4, 5, 6]}

# labels_file.json for binary classification, you can define your own classes here
{"labels": [1, 2]} or [0, 1] 
```

- `launch.py`: This file consists of `loadmodel`, `preprocessing` and `predict` functions works on to load model from local or pre-trained from any python pkg, adds pre-processing steps and prediction scripts for user inference data respectively.

For more info on how to create and manage `launch.py` you can visit [here](https://docs.katonic.ai/UserGuide/katonic-deploy/how-to-s/Deploy%20a%20Image%20Classification%20Model#:~:text=Copy-,launch.py,-%2D%20This%20is%20the).

- `schema.py`: Define your schema on how you should pass your input data in predict function.
For more info on how to create and manage `schema.py` you can visit [here](https://docs.katonic.ai/UserGuide/katonic-deploy/how-to-s/Deploy%20a%20Image%20Classification%20Model#:~:text=Copy-,schema.py,-%2D%20This%20file%20will).

- `requirements.txt`: Define your model dependent pkgs in this file.
