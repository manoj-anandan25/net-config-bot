<p align="center">
  <img src="https://github.com/user-attachments/assets/6056213e-8fbb-4f41-b307-1fe48755a2eb" alt="Net-Config-Bot Architecture" width="800">
</p>

<h1 align="center"> Net-Config-Bot</h1>

<p align="center">
  <b>GitOps-Driven Network Configuration & Compliance Framework</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Network-Automation-orange?style=for-the-badge" alt="Network">
  <img src="https://img.shields.io/badge/Framework-Netmiko-yellow?style=for-the-badge" alt="Netmiko">
</p>

---

###  Why This Project Matters
Manual CLI configuration is the leading cause of network outages and security drift. Traditional automation often lacks the safety nets required for production environments.

**Net-Config-Bot** treats **Infrastructure as Code (IaC)** by ensuring every change is validated against compliance policies before it touches a device. It features a "safety-first" deployment model with automated rollbacks, demonstrating:
- **Risk Mitigation:** Automated pre-flight checks and mandatory dry-run modes.
- **Policy Enforcement:** Rule-based compliance validation integrated into the deployment pipeline.
- **Operational Excellence:** Reducing MTTR and human error through template-driven design.

###  System Workflow

`Inventory (YAML)` ➔ `Template Rendering (Jinja2)` ➔ `Policy Validation` ➔ `Dry-Run Diff` ➔ `Deployment (Netmiko)` ➔ `Rollback (on failure)`

---

###  Engineering Highlights
- **GitOps Workflow:** Applies version-controlled discipline to network engineering changes.
- **Template-Based Generation:** Uses **Jinja2** to maintain consistent, vendor-agnostic configuration blueprints.
- **Compliance Engine:** A validation layer that blocks unsafe or non-compliant ACLs and VLAN configurations.
- **Automated Rollback:** Tracks configuration diffs and restores the last known good state automatically upon execution failure.

---

###  Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **Automation** | Netmiko |
| **Templating** | Jinja2 |
| **Inventory** | YAML (Infrastructure as Code) |
| **Testing** | Pytest (Policy Validation) |

---

###  Repository Architecture

```text
net-config-bot/
├── inventory/        # Site-specific YAML device data
├── templates/        # Jinja2 configuration blueprints
├── policies/         # Compliance & Policy-Driven rule sets
├── automation/       # Config generation & validation core
├── rollback/         # Backup & restoration mechanisms
├── logs/             # Detailed execution & audit trails
└── main.py           # Master Orchestration Script

```

---

###  Setup & Execution

1. **Clone the Repository**

```bash
git clone https://github.com/manoj-anandan25/net-config-bot.git
cd net-config-bot
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run a Safe Dry-Run (Validation Only)**

```bash
python main.py --dry-run
```

4. **Deploy to Production**

```bash
python main.py --apply
```

###  Deployment Insights

<p align="center">
<img src="https://github.com/user-attachments/assets/fff4a039-8392-4465-9794-499c124b3aa5" width="85%" />
</p>

---

###  Future Roadmap

* [ ] **CI/CD Integration:** Automated deployment via GitHub Actions.
* [ ] **Multi-Vendor Expansion:** Native support for Arista, Juniper, and HP.
* [ ] **Observability:** Integration with ServiceNow/Jira for automated Change Requests.

---

<p align="center"> Developed by <b>Manoj Anandan</b> </p>

```
