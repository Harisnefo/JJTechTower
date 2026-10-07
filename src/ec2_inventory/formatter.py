"""Output formatting functions."""

from typing import Any


def format_inventory(instances: list[dict[str, Any]]) -> str:
    """Format EC2 inventory as human-readable text."""

    if not instances:
        return "No EC2 instances found."

    lines = [
        "EC2 Inventory",
        "=============",
    ]

    for instance in instances:
        lines.append(
            f"{instance['name']} | "
            f"{instance['instance_id']} | "
            f"{instance['instance_type']} | "
            f"{instance['state']} | "
            f"{instance['environment']}"
        )

    return "\n".join(lines)
