import yaml
from jinja2 import Environment, FileSystemLoader
import os

def generate_config(template_name, data, output_file):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    config = template.render(data)

    os.makedirs("configs/generated", exist_ok=True)
    with open(output_file, "w") as f:
        f.write(config)

    print(f"Config generated: {output_file}")

if __name__ == "__main__":
    with open("inventories/switches.yaml") as f:
        switches = yaml.safe_load(f)

    data = {"vlan_id": 10, "vlan_name": "OfficeLAN"}
    generate_config("vlan_config.j2", data, "configs/generated/switch01.cfg")