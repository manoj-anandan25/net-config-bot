import shutil

def rollback(device_name):
    backup_file = f"configs/backups/{device_name}_backup.cfg"
    target_file = f"configs/generated/{device_name}.cfg"

    shutil.copy(backup_file, target_file)
    print(f"Rollback complete: {target_file} restored from {backup_file}")

if __name__ == "__main__":
    rollback("switch01")