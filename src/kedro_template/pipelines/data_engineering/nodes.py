from typing import Any, Dict, List

import pandas as pd
from sklearn.model_selection import train_test_split


def get_classes(data: pd.DataFrame, target_col: str) -> List[str]:
    """Node for getting the classes from the Iris data set.
    :param int num1: The first number
    :param int num2: The second number

    :returns: The sum of two numbers

    :rtype: int
    """
    return sorted(data[target_col].unique())


def encode_categorical_columns(data: pd.DataFrame, target_col: str) -> pd.DataFrame:
    """Node for encoding the categorical columns in the Iris data set."""

    return pd.get_dummies(data, columns=[target_col], prefix="", prefix_sep="")


def split_data(
    data: pd.DataFrame, test_data_ratio: float, classes: list
) -> Dict[str, Any]:
    """Node for splitting the classical Iris data set into training and test
    sets, each split into features and labels.
    """

    X, y = data.drop(columns=classes), data[classes]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_data_ratio)

    # When returning many variables, it is a good practice to give them names:
    return dict(
        train_x=X_train,
        train_y=y_train,
        test_x=X_test,
        test_y=y_test,
    )
