import itertools

# Step 1: Define the ring data
rings = [
    {"name": "Acid Stone", "health": 0, "lifesteal": 0, "shield": 0, "damage_reduction": 0, "elemental_damage": 12, "crit_chance": 0},
    {"name": "Ahanae Crystal", "health": 0, "lifesteal": 0, "shield": 0, "damage_reduction": 0, "elemental_damage": 0, "crit_chance": 4},
    {"name": "Akari War Band", "health": 0, "lifesteal": 0, "shield": 0, "damage_reduction": 0, "elemental_damage": 0, "crit_chance": 10},
    {"name": "Alchemy Stone", "health": 0, "lifesteal": 6, "shield": 0, "damage_reduction": 0, "elemental_damage": 0, "crit_chance": 0},
    {"name": "Alumni Ring", "health": 0, "lifesteal": 0, "shield": 0, "damage_reduction": 0, "elemental_damage": 10, "crit_chance": 0},
]

# Step 2: Function to calculate stats for a given combination of rings
def calculate_stats(ring_combination):
    total_stats = {"health": 0, "lifesteal": 0, "shield": 0, "damage_reduction": 0, "elemental_damage": 0, "crit_chance": 0}
    for ring in ring_combination:
        for key in total_stats:
            total_stats[key] += ring[key]
    return total_stats

# Step 3: Generate all possible combinations of four rings and calculate stats
def find_best_combinations(rings, priority_stats):
    all_combinations = list(itertools.combinations(rings, 4))
    stats_and_combinations = []

    for combination in all_combinations:
        stats = calculate_stats(combination)
        stats_and_combinations.append((stats, combination))

    # Sort based on priority_stats, which is a list of stat names in order of importance
    sorted_combinations = sorted(stats_and_combinations, key=lambda x: tuple(-x[0][stat] for stat in priority_stats))
    return sorted_combinations

# Step 4: Define priority stats and find the best combinations
priority_stats = ["health", "shield", "damage_reduction", "elemental_damage", "crit_chance"]
best_combinations = find_best_combinations(rings, priority_stats)

# Step 5: Output the results
print("Top Ring Combinations and Their Stats:")
for stats, combination in best_combinations[:5]:  # Display top 5 combinations
    print(f"Stats: {stats}")
    print("Rings:")
    for ring in combination:
        print(f"  - {ring['name']}")
    print("\n")
