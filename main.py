import yaml
import os
from automation.generate_config import generate_config
from automation.validate_config import validate_config
from policies.compliance_checks import check_compliance
from automation.apply_config import apply_config
from automation.rollback import rollback

def main():
    print("=== Net-Config-Bot: GitOps Workflow Started ===")

    # Load inventory
    with open("inventories/switches.yaml") as f:
        switches = yaml.safe_load(f)["switches"]

    # Example: generate VLAN config for switch01
    data = {"vlan_id": 10, "vlan_name": "OfficeLAN"}
    output_file = "configs/generated/switch01.cfg"
    generate_config("vlan_config.j2", data, output_file)

    # Step 1: Validate config
    if not validate_config(output_file):
        print("Validation failed. Aborting workflow.")
        return

    # Step 2: Compliance check
    if not check_compliance(output_file):
        print("Compliance check failed. Aborting workflow.")
        return

    # Step 3: Apply config (sandbox mode)
    device = switches[0]  # switch01
    try:
        apply_config(device, output_file)
        print("Config applied successfully.")
    except Exception as e:
        print(f"Error applying config: {e}")
        print("Initiating rollback...")
        rollback(device["hostname"])

    print("=== Net-Config-Bot: Workflow Completed ===")

if __name__ == "__main__":
    main()