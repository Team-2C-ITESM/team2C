def mapFromCSV(filePath):
    import numpy as np
    import matplotlib.pyplot as plt
    from datetime import datetime

    # Initialize the position and trail
    position = np.array([0, 0, 0])
    trail = []

    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Load the CSV file
    # filename = 'DirectionData_2023-06-03_16-45-48.csv' # Replace with your CSV file name
    data = np.loadtxt(filePath, delimiter=',')

    # Extract the acceleration from the yaw, pitch and roll from the CSV file
    yaw = data[:, 0]
    pitch = data[:, 1]
    roll = data[:, 2]
    distance = data[:, 3]

    # Start the trajectory loop
    for i in range(len(yaw)):

        yawR = round(yaw[i]/30)*30
        pitchR = round(pitch[i]/30)*30

        if pitchR < 90 or pitchR > -90:
            # Calculate the direction vector
            direction = np.array([np.cos(np.deg2rad(yawR)) * np.cos(np.deg2rad(pitchR)),
                                np.sin(np.deg2rad(yawR)) * np.cos(np.deg2rad(pitchR)),
                                np.sin(np.deg2rad(pitchR))])

        if pitchR > 90 or pitchR < -90:
            # Calculate the direction vector
            direction = np.array([-np.cos(np.deg2rad(yawR)) * np.cos(np.deg2rad(pitchR)),
                                np.sin(np.deg2rad(yawR)) * np.cos(np.deg2rad(pitchR)),
                                np.sin(np.deg2rad(pitchR))])

        # Update the position based on the direction and distance
        position = position + distance[i] * direction

        # Update the trail with the new position
        trail.append(position.copy())

    # Convert trail to NumPy array

    trail = np.array(trail)

    # Plot the trail as a line
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(trail[:, 0], trail[:, 1], trail[:, 2], 'b-')

    ax.set_title('Pipeline Mapping')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Adjust plot limits to fit the trail
    trail_min = np.min(trail, axis=0)
    trail_max = np.max(trail, axis=0)
    axisMin = min(trail_min[0],trail_min[1],trail_min[2]) - 0.1
    axisMax = max(trail_max[0],trail_max[1],trail_max[2]) + 0.1
    ax.set_xlim(axisMin,axisMax)
    ax.set_ylim(axisMin,axisMax)
    ax.set_zlim(axisMin,axisMax)

    ax.invert_xaxis()

    plt.grid(True)
    plt.show()