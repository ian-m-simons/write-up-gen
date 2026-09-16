# Hack the Box Write-Up Generator

A Python-based penetration testing workflow tool that automates Nmap scanning, parses XML results, performs basic web enumeration, and generates a professional Markdown report template for documenting Hack The Box, Proving Grounds, lab environments, and other authorized security assessments.

## Overview

During penetration testing engagements and lab exercises, a significant amount of time is spent collecting reconnaissance data and building report structures before documenting findings.

This tool automates the early stages of that workflow by:

- Running an Nmap full-port scan with service and default script detection
- Parsing Nmap XML output
- Extracting open ports and service information
- Automatically generating a structured Markdown penetration testing report
- Performing basic HTTP/HTTPS enumeration
- Reviewing HTML comments
- Checking for accessible `robots.txt` files

The goal is not to replace analyst work, but to eliminate repetitive setup tasks so more time can be spent on enumeration, exploitation, and report writing.

---

## Features

### Scan Automation

- Full TCP port scan (`-p-`)
- Default NSE scripts (`-sC`)
- Version detection (`-sV`)
- Saves output in all Nmap formats (`-oA`)

### XML Parsing

- Parses Nmap XML results
- Extracts:
  - Port numbers
  - Protocols
  - Service names
  - Service versions
  - Port states

### Automatic Report Generation

Creates a report template containing:

- Executive Summary / Overview
- Vulnerability Summary
- Attack Path Summary
- Reconnaissance Findings
- Initial Access Documentation
- Privilege Escalation Documentation
- Lessons Learned
- Appendices
- Evidence Sections
- MITRE ATT&CK References
- CVSS Placeholders

### Web Enumeration

For detected HTTP/HTTPS services:

- Retrieves page content
- Extracts HTML comments
- Checks for `robots.txt`
- basic detection of custom 404 responses

---

## Requirements

### Operating System

Tested on:

- Kali Linux
- Parrot OS

### Dependencies

- Python 3
- Nmap
- Curl

Install required packages:

```bash
sudo apt update
sudo apt install nmap curl
```

---

## Usage

Run the script with a target IP address:

```bash
python3 report_generator.py 10.10.10.10
```

Example:

```bash
python3 report_generator.py 10.129.123.45
```

---

## Output Structure

After execution:

```text
.
├── nmap
│   ├── scan.gnmap
│   ├── scan.nmap
│   └── scan.xml
└── report.md
```

### Nmap Results

Raw scan results are preserved in:

```text
nmap/
```

### Generated Report

A report template is created:

```text
report.md
```

and automatically populated with:

- Nmap results
- Open ports
- Service information

The remaining sections are intended to be completed during the assessment.

---

## Example Open Ports Table

Generated from parsed Nmap data:

```markdown
| Port | Service | Version |
|------|----------|----------|
| 22/tcp | ssh | OpenSSH 8.2 |
| 80/tcp | http | Apache 2.4.41 |
| 3306/tcp | mysql | MySQL 8.0 |
```

---

## Intended Use Cases

- Hack The Box machines
- Proving Grounds labs
- CPTS practice environments
- Internal lab environments
- Security training exercises

---

## Future Improvements

Potential future enhancements include:

- Improved error handling
- Argument validation
- Gobuster/Feroxbuster integration
- Automatic MITRE ATT&CK mapping recommendations
- Service fingerprint normalization
- Report customization profiles

---

## Learning Objectives

This project was created to practice and demonstrate:

- Python automation
- Offensive security workflows
- XML parsing
- Process automation
- Report generation
- Network reconnaissance
- Web enumeration
- Security tooling development

---

## Disclaimer

This tool is intended for educational purposes and authorized security assessments only.

Do not scan systems you do not own or have explicit permission to test.

The user is solely responsible for complying with all applicable laws, rules, and organizational policies.

---

## Author

**Ian Simons**

Offensive Security Student

Built while progressing through the Hack The Box CPTS learning path.
