import numpy as np

def calculate_distance(x, y):
    """Returns a distance in km between points, using a Haversine formula.

    Args:
      x: An array (lat1, lon1) representing the first point.
      y: An array (lat2, lon2) representing the second point.
    """
    # Convert latitudes and longitudes to radians
    x_rad = np.radians(x)
    y_rad = np.radians(y)

    # Differences in latitudes and longitudes
    dlat = y_rad[0] - x_rad[0]
    dlon = y_rad[1] - x_rad[1]

    # Haversine formula
    a = np.sin(dlat / 2) ** 2 + np.cos(x_rad[0]) * np.cos(y_rad[0]) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    d = 6371 * c  # Earth radius in kilometers
    return d
