def count_batteries_by_health(present_capacities):
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    # Iterate through each battery's present capacity
    for capacity in present_capacities:
        # Define the rated capacity of a new battery
        rated_capacity = 120
        # Calculate the State-of-Health (SoH) percentage
        soh_percentage = (capacity / rated_capacity) * 100

        # Classify batteries based on SoH and update counts
        if soh_percentage > 80:
            counts["healthy"] += 1
        elif 62 <= soh_percentage <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    # Return the counts for each health category
    return counts


def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    print("Health Conditions of a batteries")
    print("Healthy battery:", counts["healthy"])
    print("Exchange battery:", counts["exchange"])
    print("Failed battery:", counts["failed"])
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
