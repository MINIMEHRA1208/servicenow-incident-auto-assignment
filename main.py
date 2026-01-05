from servicenow_api import get_incident, update_incident
from rules import decide_assignment

def process_incident(sys_id):
    incident = get_incident(sys_id)

    assignment_group, priority = decide_assignment(incident)

    update_data = {
        "assignment_group": assignment_group,
        "priority": priority,
        "work_notes": (
            f"Auto-assigned to {assignment_group} "
            f"with priority {priority} based on alert analysis."
        )
    }

    update_incident(sys_id, update_data)
    print(f"[SUCCESS] Incident {sys_id} updated")

if __name__ == "__main__":
    INCIDENT_SYS_ID = "REPLACE_WITH_SYS_ID"

    if INCIDENT_SYS_ID.startswith("REPLACE"):
        raise ValueError("Please replace INCIDENT_SYS_ID with a valid sys_id")

    process_incident(INCIDENT_SYS_ID)
