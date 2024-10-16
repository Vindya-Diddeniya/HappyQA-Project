#!/usr/bin/env python

"""
Happy QA Code Assignment
The following script solves how many releases can be possibly done within a 2-week sprint, 10 working days with the following conditions:
1.Any taken release must be completed within the sprint.
2.Bob can only validate one release at any given time.
3.Release validation cannot be postponed.

Because of this problem, I will utilize a greedy algorithm.
python: 3.13
PyCharm CE
AI platforms were consulted to explore the algorithms suitable for scheduling scenarios in Agile sprints. Several approaches were suggested by them. I have chosen the "greedy algorithm" because it is simple and understandable for me, and it has been used very much in the industry.
There are other algorithms that could be considered for release scheduling besides my selection. A few of them are as follows:
1. Dynamic Programming: This is an approach wherein the problem is divided into subproblems, each is distinctly solved, and results are stored in order to avoid redundant computation. Here, you could fill a 2D table tracking, for each day in the sprint, how many maximum releases can be validated considering all the possible validation times.
2. Backtracking Algorithm: An algorithm that, by recursion, may explore all possible combinations of releases. It exhibits backtracking at the dead end, i.e., a point where a release cannot be finished within the sprint. This would be able to find feasible combinations of releases, though somewhat computationally costly.
3. Branch and Bound Algorithm: This algorithm is somewhat like a backtracking algorithm, but it makes use of bounding functions to discard non-promising branches. It carries out branch-and-bound by an estimate of the maximum number of releases that can be completed for a given set, thereby pruning branches that cannot lead to optimal solutions.
4. ILP: This represents the problem as an integer linear program where it is focusing on maximizing releases completed in the sprint by respecting constraints on validation times and sprint duration. Solution of the ILP can be obtained with an ILP solver.
5. Metaheuristics: These are high-level algorithms that make use of heuristics to explore possible solutions. Examples include simulated annealing, genetic algorithms, and ant colony optimization. These methods may provide a good solution while probably not ensuring optimality.


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
