from typing import Any


def flatten_dict(d: dict[str, Any]):
    flattened = {}

    for key, value in d.items():
        if isinstance(value, dict):
            flattened.update(
                {
                    f"{key}.{child_key}": value
                    for child_key, value in flatten_dict(value).items()
                }
            )
        else:
            flattened[key] = value

    return flattened


# Example usage:
nested_dict = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}, "g": {"h": 5}}

flattened = flatten_dict(nested_dict)
print(flattened)
