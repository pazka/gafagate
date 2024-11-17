from typing import Tuple
import math


def normalize(value: float, min_val: float, max_val: float) -> float:
    return math.ceil((value - min_val) / (max_val - min_val))


def interpolate(min_value: float, max_value: float, normalized_value: float) -> float:
    return math.ceil(min_value + (max_value - min_value) * normalized_value)


def normalize(value: tuple[float, float, float], min_val: tuple[float, float, float], max_val: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(math.ceil((v - min_v) / (max_v - min_v)) for v, min_v, max_v in zip(value, min_val, max_val))


def interpolate(min_val: Tuple[float, float, float], max_val: Tuple[float, float, float], normalized_val: float) -> Tuple[float, float, float]:
    return tuple(math.ceil(min_v + (max_v - min_v) * normalized_val) for min_v, max_v in zip(min_val, max_val))


def extract_1_from_color(_color: Tuple[int, int, int], i) -> int:
    color = [0, 0, 0]
    color[i] = _color[i]
    return tuple(color)
