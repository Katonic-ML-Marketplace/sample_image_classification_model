# Image Classification Model

This repository contains the example and sample files to deploy a Custom Image Classification Model on Katonic Platform.

## Prerequisites for Deployment:

- `labels_file.json`: This file is required for feedback or performance metrics calculations of binary or multi-class classification problems.

***Please note that these classes should be in encoded format (eg. ["cat", "dog] will be [0, 1] or [1, 2]) for both binay and multi-class problems.***

```python
# labels_file.json for multi-class classification, you can define your own classes here
{"labels": [1, 2, 3, 4, 5, 6]}

# labels_file.json for binary classification, you can define your own classes here
{"labels": [1, 2]} or [0, 1] 
```

- `launch.py`: This file consists of `loadmodel`, `preprocessing` and `predict` functions.
 The first function helps to fetch the model. The second function is optional,if you are performing any kind of preprocessing on the data before prediction please add all the necessary steps into it and return the formatted input, else you can just return `False` if no processing is required. In the third function write down the code for prediction and return the results in the data structure supported by API response.   

For more information on how to create and manage `launch.py` you can visit [here](https://docs.katonic.ai/UserGuide/katonic-deploy/how-to-s/Deploy%20a%20Image%20Classification%20Model#:~:text=Copy-,launch.py,-%2D%20This%20is%20the).

- `schema.py`: Define your schema on how you should pass your input data in predict function.
For more information on how to create and manage `schema.py` you can visit [here](https://docs.katonic.ai/UserGuide/katonic-deploy/how-to-s/Deploy%20a%20Image%20Classification%20Model#:~:text=Copy-,schema.py,-%2D%20This%20file%20will).

- `requirements.txt`: Define the required packages along with specific versions this file.

## Sample Input Data for Prediction API

```python
{
    "data":"http://images.cocodataset.org/val2017/000000039769.jpg"
}
```
## Sample Input Data for Feedback API

```python
{
  "predicted_label": [1,3,4,1,1,1,3,3,4],
  "true_label": [1,3,4,3,1,1,4,3,4]
}
```
