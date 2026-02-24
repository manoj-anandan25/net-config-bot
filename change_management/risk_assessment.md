# Risk Assessment

**Change ID:** CR-2026-001  

## Impact
- Low risk: VLAN addition is isolated to switch01.
- Possible disruption if misconfigured.

## Rollback Plan
- Restore `configs/backups/switch01_backup.cfg`.
- Use `automation/rollback.py` script.