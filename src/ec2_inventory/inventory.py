"""AWS EC2 inventory utilities."""

from typing import Any


def normalize_instance(instance: dict[str, Any]) -> dict[str, Any]:
    """Normalize an EC2 instance response into a simple dictionary."""

    tags = {
        tag["Key"]: tag["Value"]
        for tag in instance.get("Tags", [])
        if "Key" in tag
    }

    return {
        "instance_id": instance.get("InstanceId"),
        "instance_type": instance.get("InstanceType"),
        "state": instance.get("State", {}).get("Name", "unknown"),
        "private_ip": instance.get("PrivateIpAddress"),
        "public_ip": instance.get("PublicIpAddress"),
        "name": tags.get("Name", "N/A"),
        "environment": tags.get("Environment", "unknown"),
    }


def filter_instances(
    instances: list[dict[str, Any]],
    environment: str | None = None,
    state: str | None = None,
) -> list[dict[str, Any]]:
    """Filter EC2 instances by environment and state."""

    normalized = [normalize_instance(instance) for instance in instances]

    if environment:
        normalized = [
            instance
            for instance in normalized
            if instance["environment"].lower() == environment.lower()
        ]

    if state:
        normalized = [
            instance
            for instance in normalized
            if instance["state"].lower() == state.lower()
        ]

    return normalized


def count_by_type(instances: list[dict[str, Any]]) -> dict[str, int]:
    """Return the number of instances grouped by instance type."""

    counts: dict[str, int] = {}

    for instance in instances:
        instance_type = instance.get("instance_type", "unknown")
        counts[instance_type] = counts.get(instance_type, 0) + 1

    return counts
