***
# restml_endpoint

**This repo contains code to deploy a simple ML model using Flask. Tests with unittest and Jenkins pipeline to run on a Docker image**

## Project status
- Current version:
  - ML model trained on fashion-MNIST-train1 
  - Flask application with an homepage to input data and a classify route to return predicted class
  - Tests with unittest to check that the endpoint returns expected value
  - Jenkins pipeline that builds, runs and tests code on a Docker image

- TO DO:
  - Probability associated to predicted class isn't correct (displays 1.0 everytime)

## Installation

**1. Cloning**

With https :
```
git clone https://github.com/RaphaelJehl/restml_endpoint.git
```
**2. Python**

Python version used is 3.8

Check with :
```
python --version
```

**3. Dependencies**

Create a virtual environment
```
cd path/to/installation/folder
python -m venv venv1
```
Activate your virtual environment
```
venv1\Scripts\activate
```
Install dependencies
```
pip install -r requirements.txt
```

**3. Running Flask application**
```
py app.py
```
Input must be a 784x1 array
