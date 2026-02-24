# Change Request

**Request ID:** CR-2026-001  
**Requested By:** Network Team  
**Date:** 2026-01-28  

## Summary
Add VLAN 10 for OfficeLAN on switch01.

## Details
- Device: switch01
- Config: VLAN 10, name OfficeLAN
- Impact: Users in Bangalore office will join VLAN 10.

## Plan
1. Generate config via Net-Config-Bot.
2. Validate and check compliance.
3. Apply in sandbox, then production.