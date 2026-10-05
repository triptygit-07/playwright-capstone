def deep_compare(actual, expected, path="root"):
    if type(actual) is not type(expected):
        return (
            False,
            f"{path}: type mismatch "
            f"({type(actual).__name__} != {type(expected).__name__})"
        )

    if isinstance(actual, dict):
        for key in expected:
            current_path = f"{path}.{key}"

            if key not in actual:
                return False, f"{current_path}: missing key"

            matched, message = deep_compare(
                actual[key],
                expected[key],
                current_path
            )

            if not matched:
                return False, message

        for key in actual:
            if key not in expected:
                return False, f"{path}.{key}: unexpected key"

        return True, ""

    if isinstance(actual, list):
        if len(actual) != len(expected):
            return (
                False,
                f"{path}: list length mismatch "
                f"({len(actual)} != {len(expected)})"
            )

        for index, (actual_item, expected_item) in enumerate(
            zip(actual, expected)
        ):
            matched, message = deep_compare(
                actual_item,
                expected_item,
                f"{path}[{index}]"
            )

            if not matched:
                return False, message

        return True, ""

    if actual != expected:
        return (
            False,
            f"{path}: value mismatch ({actual!r} != {expected!r})"
        )

    return True, ""