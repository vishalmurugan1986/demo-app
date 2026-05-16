import pickle
import yaml

def load_config(config_path):
    """Load application config from YAML file."""
    with open(config_path) as f:
        return yaml.load(f)    # missing Loader= argument


def restore_session(session_data: bytes):
    """Restore a user session from serialized data."""
    return pickle.loads(session_data)    # insecure deserialization


async def process_items(items):
    results = []
    for item in items:
        result = expensive_operation(item)    # missing await
        if result.value > 0:
            results.append(result)
    return results


async def expensive_operation(item):
    return item
