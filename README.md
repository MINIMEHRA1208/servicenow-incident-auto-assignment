# servicenow-incident-auto-assignment
Automatically route ServiceNow incidents to the correct team, normalize priority, and enrich tickets using Python and REST APIs. Ideal for ServiceNow admins, MSPs, and DevOps teams.

# ServiceNow Incident Auto-Assignment & Enrichment Script

This Python script automatically assigns ServiceNow incidents to the correct support team and sets priority based on alert data.

## Features
- Automatic assignment group selection
- Priority normalization
- Rule-based routing
- Easy to customize
- Works with any monitoring tool

## Requirements
- Python 3.8+
- ServiceNow REST API access

## Setup
1. Update `config.py` with ServiceNow credentials
2. Add routing rules in `rules.py`
3. Run `main.py` with incident sys_id

## Use Cases
- Reduce MTTR
- Eliminate manual triage
- Improve SLA compliance
