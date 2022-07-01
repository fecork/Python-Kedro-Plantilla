"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_classes, encode_categorical_columns, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                get_classes,
                ["raw_data", "params:target_col"],
                "classes",
                name="get_classes",
            ),
            node(
                encode_categorical_columns,
                ["raw_data", "params:target_col"],
                "encoded_data",
                name="encode_categorical_columns",
            ),
            node(
                split_data,
                ["encoded_data", "params:test_data_ratio", "classes"],
                dict(
                    train_x="train_x",
                    train_y="train_y",
                    test_x="test_x",
                    test_y="test_y",
                ),
                name="split",
            ),
        ]
    )
