#  Net-Config-Bot

### GitOps-Style Network Configuration Automation Framework

---

##  Overview

**Net-Config-Bot** is an enterprise-style network automation framework that safely generates, validates, deploys, and rolls back network configurations.

It applies **GitOps principles** to network engineering:

* Infrastructure as Code
* Compliance Enforcement
* Change Validation
* Automated Rollback
* Version-Controlled Configurations

This project demonstrates production-grade automation discipline and safe configuration management.

---

##  Architecture
<img width="497" height="312" alt="output1" src="https://github.com/user-attachments/assets/6056213e-8fbb-4f41-b307-1fe48755a2eb" />

---

##  High-Level Workflow

```
User Request
      ↓
Inventory (YAML)
      ↓
Jinja2 Templates
      ↓
Config Generator
      ↓
Validator + Compliance Engine
      ↓
Apply via Netmiko
      ↓
Backup + Diff
      ↓
Rollback (if failure)
      ↓
Logs + Reports
```

---

##  Project Structure

```
net-config-bot/
├── inventory/            # Device & site YAML inventory
├── templates/            # Jinja2 configuration templates
├── policies/             # Zero Trust & compliance rules
├── automation/           # Config generation & validation logic
├── rollback/             # Backup & restore mechanisms
├── change_management/    # Change request documentation
├── logs/                 # Execution logs
├── tests/                # Unit tests for compliance rules
└── main.py               # Orchestrator
```

---

## ⚙️ How It Works

###  Inventory-Driven Design

Devices and site configurations are defined in YAML files.

###  Template-Based Generation

Jinja2 templates dynamically generate structured configurations for:

* VLANs
* ACLs
* Port Security
* SSIDs

###  Validation & Compliance

Before deployment:

* Syntax validation runs
* Zero Trust policies are enforced
* Unsafe configurations are blocked

### 4️ Deployment

Configurations are applied using **Netmiko**.

### 5️ Backup & Rollback

* Previous configs are backed up
* Diffs are generated
* If deployment fails → automatic rollback restores the last known good state

---

##  Feature Highlights

*  GitOps-style workflow
*  Infrastructure-as-Code for networking
*  Zero Trust policy enforcement
*  Automated rollback on failure
*  Config diff tracking
*  Markdown-based change documentation
*  Dry-run mode
*  Modular architecture
*  Unit testing with Pytest
*  Reviewer-friendly logs and outputs

---

##  Tech Stack

| Category      | Technology              |
| ------------- | ----------------------- |
| Language      | Python 3                |
| Automation    | Netmiko                 |
| Templates     | Jinja2                  |
| Configuration | YAML                    |
| Testing       | Pytest                  |
| Logging       | Python Logging          |
| Architecture  | Modular + GitOps Design |

---

##  Installation

```bash
pip install -r requirements.txt
```

---

##  Execution

### 🔹 Dry Run Mode (Safe)

```bash
python main.py --dry-run
```

### 🔹 Production Mode

```bash
python main.py --apply
```

---

##  Execution Output
<img width="1137" height="766" alt="output2" src="https://github.com/user-attachments/assets/fff4a039-8392-4465-9794-499c124b3aa5" />

---

##  Compliance Model

The system enforces:

* Deny-by-default network policies
* VLAN whitelisting
* Port security enforcement
* Configuration sanity validation
* Rollback safety guarantees

---

##  What This Project Demonstrates

* Enterprise change control discipline
* Production-safe automation design
* Infrastructure-as-Code implementation
* Risk mitigation through rollback
* Clear audit trails with logs and diffs
* Compliance-first network automation

---

##  Future Enhancements

* CI/CD pipeline integration
* GitHub Actions workflow
* REST API interface
* Multi-vendor device support
* ServiceNow / Jira integration
* Role-based access control

---

