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
            if not isinstance(value, int) and not isinstance(value, str):
                raise ValueError("Values must be int, str or dict")
            
            flattened[key] = value

    return flattened
