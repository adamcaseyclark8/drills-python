def deep_clone_object(obj):
    if isinstance(obj, list):
        return [deep_clone_object(item) for item in obj]
    if isinstance(obj, dict):
        return {key: deep_clone_object(value) for key, value in obj.items()}
    return obj
