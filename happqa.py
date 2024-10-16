#!/usr/bin/env python

"""Happy QA
This script solves how many releases possible within a 2-week sprint (10 working days) with the following constraints:
       1.Any taken release must be completed within the sprint.
       2.Bob can only validate one release at a time.
       3.Release validation cannot be postponed.

I'll use a greedy algorithm to solve this problem.
python: 3.13
"""
def select_releases(releases_file):
# Read input file
    with open(releases_file, 'r') as f:
        releases = [tuple(map(int, line.split())) for line in f.readlines()]

    # Sort releases by delivery day and validation time
    releases.sort(key=lambda x: (x[0], x[1]))

    # Initialize selected releases and current day
    selected_releases = []
    current_day = 1

    # Iterate through sorted releases
    for delivery_day, validation_time in releases:
        if delivery_day + validation_time <= 10:
            # Add release to selected list
            selected_releases.append((delivery_day, delivery_day + validation_time - 1))
            # Update current day
            current_day = delivery_day + validation_time

    # Write output to file
    with open('solution.txt', 'w') as f:
        f.write(str(len(selected_releases)) + '\n')
        for release in selected_releases:
            f.write(' '.join(map(str, release)) + '\n')

# Run the algorithm
select_releases('releases.txt')


"""
Postponing Release Validation (Optional)
"""

def select_releases_postponed(releases_file):
# Read input file
    with open(releases_file, 'r') as f:
        releases = [tuple(map(int, line.split())) for line in f.readlines()]

    #sorted releases
    for delivery_day, validation_time in releases:
        if delivery_day + validation_time > 10:
            #Try to postpone validation
            for day in range(delivery_day, 11):
                if day + validation_time <= 10:
                    # Add release to selected list with postponed validation
                    selected_releases.append((day, day + validation_time - 1))
                # Update current day
                current_day = day + validation_time
                break
        else:
            #Add release to selected list without postponing
            selected_releases.append((delivery_day, delivery_day + validation_time - 1))
            # Update current day
            current_day = delivery_day + validation_time
        # Write output to file
        with open('solution.txt', 'w') as f:
            f.write(str(len(selected_releases)) + '\n')
        for release in selected_releases:
            f.write(' '.join(map(str, release)) + '\n')

# Run the algorithm
select_releases_postponed('releases.txt')
