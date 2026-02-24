import os

def validate_config(config_file):
    """
    Basic validation: ensure config file exists and contains required keywords.
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"{config_file} not found")

    with open(config_file) as f:
        content = f.read()

    errors = []
    if "vlan" not in content.lower():
        errors.append("Missing VLAN configuration")
    if "name" not in content.lower():
        errors.append("Missing VLAN name")

    if errors:
        print(f"Validation failed for {config_file}: {errors}")
        return False
    else:
        print(f"Validation passed for {config_file}")
        return True

if __name__ == "__main__":
    validate_config("configs/generated/switch01.cfg")