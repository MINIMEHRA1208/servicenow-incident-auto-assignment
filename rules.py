def decide_assignment(incident):
    desc = incident.get("short_description", "").lower()
    ci = incident.get("cmdb_ci", "").lower()
    severity = incident.get("severity", "").lower()

    if "cpu" in desc or "memory" in desc:
        return "Infrastructure Team", "2"
    elif "disk" in desc:
        return "Storage Team", "2"
    elif "db" in ci or "database" in desc:
        return "Database Team", "1"
    elif "login failed" in desc or "auth" in desc:
        return "IAM Team", "2"
    elif severity == "critical":
        return "On-Call Team", "1"
    else:
        return "Service Desk", "3"
