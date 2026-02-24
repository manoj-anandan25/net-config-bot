import unittest
from automation.generate_config import generate_config
from policies.compliance_checks import check_compliance

class TestPolicyChecks(unittest.TestCase):
    def test_compliance(self):
        # Generate a compliant config first
        data = {"vlan_id": 10, "vlan_name": "OfficeLAN"}
        output_file = "configs/generated/switch01.cfg"
        generate_config("vlan_config.j2", data, output_file)

        result = check_compliance(output_file)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()