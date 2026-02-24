from netmiko import ConnectHandler

def apply_config(device, config_file):
    with open(config_file) as f:
        commands = f.readlines()

    connection = ConnectHandler(
        device_type="cisco_ios",
        host=device["ip"],
        username="admin",
        password="admin123"
    )
    output = connection.send_config_set(commands)
    print(output)
    connection.disconnect()

if __name__ == "__main__":
    device = {"ip": "192.168.10.1"}
    apply_config(device, "configs/generated/switch01.cfg")