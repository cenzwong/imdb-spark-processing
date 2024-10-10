from functools import reduce

from pyspark.sql import Column
from pyspark.sql import functions as F


def when_mapping(column, _dict: dict) -> Column:
    base_output = F
    for cond, val in _dict.items():
        base_output = base_output.when(column == cond, val)

    return base_output
