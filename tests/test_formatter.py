"""Tests for inventory formatting."""

from src.ec2_inventory.formatter import format_inventory


def test_empty_inventory():
    assert format_inventory([]) == "No EC2 instances found."


def test_format_inventory():
    instances = [
        {
            "name": "web-01",
            "instance_id": "i-001",
            "instance_type": "t3.micro",
            "state": "running",
            "environment": "dev",
        }
    ]

    output = format_inventory(instances)

    assert "EC2 Inventory" in output
    assert "web-01" in output
    assert "i-001" in output
    assert "t3.micro" in output
