# Net-Config-Bot

## Overview
Net-Config-Bot is a Python-based automation framework for managing network device configurations using GitOps principles. It ensures every change is version-controlled, validated against policies, and reversible.

## GitOps Workflow
1. **Inventories** define devices and sites.
2. **Templates** render configs via Jinja2.
3. **Automation scripts** generate, validate, and apply configs.
4. **Policies** enforce Zero Trust and compliance.
5. **Change Management** documents requests, risks, and approvals.
6. **Diffs & Backups** track changes and enable rollback.
7. **Main.py** orchestrates the full workflow.

## Change Process
- Submit a change request (`change_management/change_request.md`).
- Perform risk assessment (`change_management/risk_assessment.md`).
- Obtain approvals (`change_management/approval_log.md`).
- Run automation scripts to generate and validate configs.
- Apply configs in sandbox or production.
- Commit changes to Git for traceability.

## Rollback Strategy
- Backups stored in `configs/backups/`.
- Rollback script restores last known good config.
- Diffs (`diffs/*.diff`) highlight changes for quick review.