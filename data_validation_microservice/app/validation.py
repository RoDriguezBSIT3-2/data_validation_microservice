def validate_data(data):
    errors = []
    if not data or not isinstance(data, str):
        errors.append("Data must be a non-empty string.")
    if len(data) > 255:
        errors.append("Data must be 255 characters or fewer.")
    return errors
