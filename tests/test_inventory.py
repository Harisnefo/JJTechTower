"""Tests for EC2 inventory utilities."""

from src.ec2_inventory.inventory import (
    count_by_type,
    filter_instances,
    normalize_instance,
)


def sample_instances():
    return [
        {
            "InstanceId": "i-001",
            "InstanceType": "t3.micro",
            "State": {"Name": "running"},
            "PrivateIpAddress": "10.0.1.10",
            "Tags": [
                {"Key": "Name", "Value": "web-01"},
                {"Key": "Environment", "Value": "dev"},
            ],
        },
        {
            "InstanceId": "i-002",
            "InstanceType": "t3.small",
            "State": {"Name": "stopped"},
            "PrivateIpAddress": "10.0.1.11",
            "Tags": [
                {"Key": "Name", "Value": "db-01"},
                {"Key": "Environment", "Value": "prod"},
            ],
        },
    ]


def test_normalize_instance():
    instance = normalize_instance(sample_instances()[0])

    assert instance["instance_id"] == "i-001"
    assert instance["instance_type"] == "t3.micro"
    assert instance["state"] == "running"
    assert instance["name"] == "web-01"
    assert instance["environment"] == "dev"


def test_filter_by_environment():
    instances = filter_instances(
        sample_instances(),
        environment="dev",
    )

    assert len(instances) == 1
    assert instances[0]["instance_id"] == "i-001"


def test_filter_by_state():
    instances = filter_instances(
        sample_instances(),
        state="stopped",
    )

    assert len(instances) == 1
    assert instances[0]["instance_id"] == "i-002"


def test_count_by_type():
    instances = [
        normalize_instance(instance)
        for instance in sample_instances()
    ]

    counts = count_by_type(instances)

    assert counts["t3.micro"] == 1
    assert counts["t3.small"] == 1
