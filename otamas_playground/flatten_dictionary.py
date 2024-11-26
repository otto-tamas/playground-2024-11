from typing import Any


def flatten_dict(d: dict[str, Any]):
    if not isinstance(d, dict):
        raise ValueError("Input must be a dictionary")

    flattened = {}
    for key, value in d.items():
        if isinstance(value, dict):
            # Call recursively flatten_dict for the current value
            # and build the nested key
            children = flatten_dict(value).items()
            flattened.update(
                {f"{key}.{child_key}": value for child_key, value in children}
            )
        else:
            flattened[key] = value

    return flattened
