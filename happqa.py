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