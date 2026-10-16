"""Manage campus shuttle routes and passenger trip records."""

import json
import secrets
from datetime import datetime
from pathlib import Path
MIN_CAPACITY = 10
ROUTES = {
    "R1": {"name": "Main Gate - Library", "trips": []},
    "R2": {"name": "Hostel - Sports Complex", "trips": []},
    "R3": {"name": "Admin Block - Metro", "trips": []},
}


def add_trip_log(route_id, passenger_count, logs=None):
    """Record a valid passenger count for a route."""
    if route_id not in ROUTES:
        raise ValueError(f"Unknown route: {route_id}")
    if not isinstance(passenger_count, int) or passenger_count < 0:
        raise ValueError("Passenger count must be a non-negative integer.")

    if logs is None:
        logs = []

    ROUTES[route_id]["trips"].append(passenger_count)
    logs.append(
        f"{datetime.now()}: {route_id} carried {passenger_count}"
    )
    return logs


def remove_route(route_id):
    """Remove a route if it exists."""
    if route_id not in ROUTES:
        raise ValueError(f"Unknown route: {route_id}")
    del ROUTES[route_id]


def average_load(route_id):
    """Return a route's average passenger count, or zero if no trips exist."""
    if route_id not in ROUTES:
        raise ValueError(f"Unknown route: {route_id}")

    trips = ROUTES[route_id]["trips"]
    if not trips:
        return 0

    return sum(trips) / len(trips)


def underused_routes():
    """Return routes whose average passenger count is below capacity."""
    return [
        route_id
        for route_id, route in ROUTES.items()
        if route["trips"] and average_load(route_id) < MIN_CAPACITY
    ]


def assign_driver(route_id):
    """Assign a driver to a valid route."""
    if route_id not in ROUTES:
        raise ValueError(f"Unknown route: {route_id}")

    drivers = ["Prakash", "Leela", "Imran", "Tom"]
    return secrets.choice(drivers)


def sync_fleet_data(file="fleet.json"):
    """Save route data to JSON and reload it."""
    file_path = Path(file)
    with file_path.open("w", encoding="utf-8") as fleet_file:
        json.dump(ROUTES, fleet_file, indent=2)

    with file_path.open("r", encoding="utf-8") as fleet_file:
        saved_routes = json.load(fleet_file)

    ROUTES.clear()
    ROUTES.update(saved_routes)


def main():
    """Run a sample shuttle-management session."""
    add_trip_log("R1", 32)
    add_trip_log("R1", 28)
    add_trip_log("R2", 4)

    print("Driver for R1:", assign_driver("R1"))
    print("Underused:", underused_routes())
    print("R1 average:", average_load("R1"))

    sync_fleet_data()

    choice = input("Route to look up (Enter for R2): ").strip() or "R2"
    if choice in ROUTES:
        print("Trips on", choice, ":", ROUTES[choice]["trips"])
    else:
        print("Unknown route:", choice)

    remove_route("R3")
    print("R3 removed successfully.")


if __name__ == "__main__":
    main()
