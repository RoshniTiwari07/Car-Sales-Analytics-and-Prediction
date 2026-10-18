def validate_row_counts(expected_rows: int, actual_rows: int) -> None:
    """Raise an error when the MySQL row count differs from the CSV."""
    print(f"Expected rows: {expected_rows}")
    print(f"MySQL rows: {actual_rows}")

    if actual_rows != expected_rows:
        raise ValueError(
            f"MySQL row count mismatch: expected {expected_rows}, "
            f"found {actual_rows}"
        )
