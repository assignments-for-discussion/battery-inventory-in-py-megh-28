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
     # Additional tests for boundary conditions
    # Test when all batteries are at the upper SoH limit
    all_max_capacities = [120] * 10
    counts_all_max = count_batteries_by_health(all_max_capacities)
    assert counts_all_max["healthy"] == 10
    assert counts_all_max["exchange"] == 0
    assert counts_all_max["failed"] == 0
    print("All batteries at upper SoH limit: Passed")

    # Test when all batteries are at the lower SoH limit
    all_min_capacities = [62] * 5
    counts_all_min = count_batteries_by_health(all_min_capacities)
    assert counts_all_min["healthy"] == 0
    assert counts_all_min["exchange"] == 0
    assert counts_all_min["failed"] == 5
    print("All batteries at lower SoH limit: Passed")

if __name__ == '__main__':
    test_bucketing_by_health()
