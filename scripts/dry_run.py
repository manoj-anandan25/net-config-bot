from automation.generate_config import generate_config
from automation.validate_config import validate_config
from policies.compliance_checks import check_compliance

def dry_run():
    print("=== Dry Run Started ===")
    data = {"vlan_id": 20, "vlan_name": "TestLAN"}
    output_file = "configs/generated/switch01.cfg"
    generate_config("vlan_config.j2", data, output_file)

    validate_config(output_file)
    check_compliance(output_file)
    print("=== Dry Run Completed ===")

if __name__ == "__main__":
    dry_run()