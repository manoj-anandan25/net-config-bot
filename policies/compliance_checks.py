import yaml

def check_compliance(config_file, policy_file="policies/zero_trust.yaml"):
    with open(policy_file) as f:
        policies = yaml.safe_load(f)

    with open(config_file) as f:
        content = f.read().lower()

    violations = []
    for rule in policies["zero_trust"]:
        if "deny all" in rule["rule"].lower() and "deny" not in content:
            violations.append("Missing default deny rule")
        if "port security" in rule["rule"].lower() and "port-security" not in content:
            violations.append("Missing port security config")

    if violations:
        print(f"Compliance check failed: {violations}")
        return False
    else:
        print("Config is compliant with Zero Trust policy")
        return True

if __name__ == "__main__":
    check_compliance("configs/generated/switch01.cfg")