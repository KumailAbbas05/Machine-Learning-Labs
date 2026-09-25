# Machine Learning Labs

![Python](https://img.shields.io/badge/Python-3.x-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Practice-yellow)

A growing collection of beginner Machine Learning exercises completed while learning Python and Scikit-learn.

## Current Topics

- `train_test_split`
- Training and testing sets
- Test-size configuration
- Reproducibility with `random_state`
- K-Fold cross-validation
- Training and testing indices
- Scikit-learn basics

## Repository Structure

```text
Machine-Learning-Labs/
├── lab02/
│   ├── train_test_split_numbers.py
│   └── kfold_items.py
├── examples/
│   └── email_train_test_split.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Lab Highlights

### Train/Test Split

Splits numbers 1–20 using:

```python
test_size=0.25
random_state=0
```

This demonstrates how a dataset can be separated before model training and evaluation.

### K-Fold Cross-Validation

Uses eight sample items with four folds to show how different portions of data become the test set in each fold.

## Run the Exercises

```bash
pip install -r requirements.txt
python lab02/train_test_split_numbers.py
python lab02/kfold_items.py
```

## What I Practiced

- Importing Scikit-learn tools
- Splitting data correctly
- Understanding train vs test data
- Understanding folds
- Reading index outputs
- Writing simple reproducible ML code

## Planned Additions

- Classification
- Regression
- Confusion matrix
- Accuracy and precision
- Cross-validation scores
- Feature preprocessing

## Author

**Kumail Abbas**  
BS Artificial Intelligence Student
