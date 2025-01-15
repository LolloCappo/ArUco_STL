# aruco_stl/aruco.py

import cv2

def create_aruco_marker(dictionary, marker_id, marker_size=20):
    """
    Create an ArUco marker image.
    :param dictionary: ArUco dictionary.
    :param marker_id: Marker ID.
    :param marker_size: Size of the marker in pixels.
    :return: Marker image.
    """
    marker_image = cv2.aruco.generateImageMarker(dictionary, marker_id, marker_size)
    return marker_image
