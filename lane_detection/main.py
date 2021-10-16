def detect_edge(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Show hsv", hsv)
    lower_blue = np.array([90,120,0], dtype = "uint8")
    upper_blue = np.array([150,255,255], dtype = "uint8")
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow("mask", mask)
    edges = cv2.Canny(mask, 50, 100)
    return edges

def region_of_interest(edges):
    height, wdith = edges.shape
    mask = np.zeros_like(edges)

    polygon = np.array([[(0, height), (0, height/2), (width, height/2), (width, height)]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    cv2.imshow("roi", cropped_edges)

def detect_line_segments(cropped_
