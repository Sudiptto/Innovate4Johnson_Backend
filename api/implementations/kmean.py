import random
import numpy as np
from sklearn.cluster import KMeans


def kmean(vectors):
    candidates_with_id = vectors

    # Step 1: Create a list of vectors without the candidate ID for clustering
    candidates = np.array([vector[1:] for vector in candidates_with_id])

    # Step 2: Apply k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)  # 3 groups
    kmeans.fit(candidates)

    # Step 3: Get the group labels for each candidate
    group_labels = kmeans.labels_

    # Step 4: Combine the original candidate data with the assigned group label
    clustered_candidates = [
        (candidates_with_id[i], group_labels[i]) for i in range(len(candidates_with_id))
    ]

    # Step 5: Assign candidates to groups
    group1, group2, group3 = [], [], []

    for i in range(len(candidates_with_id)):
        if group_labels[i] == 0:
            group1.append(candidates_with_id[i])
        elif group_labels[i] == 1:
            group2.append(candidates_with_id[i])
        elif group_labels[i] == 2:
            group3.append(candidates_with_id[i])

    # Step 6: Determine the minimum group size
    min_size = min(len(group1), len(group2), len(group3))

    # Step 7: Balance groups by randomly selecting `min_size` candidates for each group
    group1_balanced = random.sample(group1, min_size)
    group2_balanced = random.sample(group2, min_size)
    group3_balanced = random.sample(group3, min_size)

    # Remaining candidates after balancing
    remaining_group1 = [candidate for candidate in group1 if candidate not in group1_balanced]
    remaining_group2 = [candidate for candidate in group2 if candidate not in group2_balanced]
    remaining_group3 = [candidate for candidate in group3 if candidate not in group3_balanced]

    # Step 8: Generate balanced teams
    teams = []

    while len(group1_balanced) >= 2 and len(group2_balanced) >= 2 and len(group3_balanced) >= 2:
        team = []
        # Select 2 candidates from each balanced group for the team
        team.extend(random.sample(group1_balanced, 2))
        team.extend(random.sample(group2_balanced, 2))
        team.extend(random.sample(group3_balanced, 2))

        # Remove selected candidates from the balanced groups
        group1_balanced = [candidate for candidate in group1_balanced if candidate not in team]
        group2_balanced = [candidate for candidate in group2_balanced if candidate not in team]
        group3_balanced = [candidate for candidate in group3_balanced if candidate not in team]

        # Add the team to the list of teams
        teams.append(team)

    remaining_candidates = remaining_group1 + remaining_group2 + remaining_group3
    while remaining_candidates:
        team = remaining_candidates[:6]  # Take up to 6 candidates
        remaining_candidates = remaining_candidates[6:]  # Update remaining candidates
        teams.append(team)

    # Increase the first element in each team by 1, 2, 3, etc.
    for idx, team in enumerate(teams):
        if team:  # Check if the team is not empty
            team[0] = (idx + 1, *team[0][1:])

    # Step 10: Display the teams
    for idx, team in enumerate(teams):
        print(f"Team {idx + 1}:")
        for candidate in team:
            print(f"Candidate ID: {candidate[0]}")
        print("-" * 30)

    return teams