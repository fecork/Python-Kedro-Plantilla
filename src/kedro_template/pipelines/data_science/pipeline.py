"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import predict, report_accuracy, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                train_model,
                ["train_x", "train_y", "parameters"],
                "model",
                name="train",
            ),
            node(
                predict,
                dict(model="model", test_x="test_x"),
                "predictions",
                name="predict",
            ),
            node(
                report_accuracy,
                ["predictions", "test_y"],
                None,
                name="report",
            ),
        ]
    )
