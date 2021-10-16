def detectColor():
    ret,frame = cap.read()    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    redLower = np.array([160,127,127],np.uint8)
    redUpper = np.array([179,255,255],np.uint8)
    redMask = cv2.inRange(hsv,redLower,redUpper)
    redcontour,redhierarchy = cv2.findContours(redMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    violetLower = np.array([130,127,127],np.uint8)
    violetUpper = np.array([160,255,255],np.uint8)
    violetMask = cv2.inRange(hsv,violetLower,violetUpper)
    violetcontour,violethierarchy = cv2.findContours(violetMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    blueLower = np.array([75,127,127],np.uint8)
    blueUpper = np.array([130,255,255],np.uint8)
    blueMask = cv2.inRange(hsv,blueLower,blueUpper)
    bluecontour,bluehierarchy = cv2.findContours(blueMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    greenLower = np.array([38,127,127],np.uint8)
    greenUpper = np.array([75,255,255],np.uint8)
    greenMask = cv2.inRange(hsv,greenLower,greenUpper)
    greencontour,greenhierarchy = cv2.findContours(greenMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    yellowLower = np.array([26,127,127],np.uint8)
    yellowUpper = np.array([38,255,255],np.uint8)
    yellowMask = cv2.inRange(hsv,yellowLower,yellowUpper)
    yellowcontour,yellowhierarchy = cv2.findContours(yellowMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    orangeLower = np.array([0,127,127],np.uint8)
    orangeUpper = np.array([20,255,255],np.uint8)
    orangeMask = cv2.inRange(hsv,orangeLower,orangeUpper)
    orangecontour,orangehierarchy = cv2.findContours(orangeMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    kernal = np.ones((5,5),"uint8")
    redMask = cv2.dilate(redMask,kernal)
    violetMask = cv2.dilate(violetMask,kernal)
    blueMask = cv2.dilate(blueMask,kernal)
    greenMask = cv2.dilate(greenMask,kernal)
    yellowMask = cv2.dilate(yellowMask,kernal)
    orangeMask = cv2.dilate(yellowMask,kernal)

    

    for pic, contour in enumerate(redcontour):
        area = cv2.contourArea(contour)
        if (area > 5000):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),2)

            cv2.putText(frame,"Red",(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255))

    for pic, contour in enumerate(violetcontour):
        area = cv2.contourArea(contour)
        if (area > 5000):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h),(173,68,143),2)

            cv2.putText(frame,"Violet",(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(173,68,143))

    for pic, contour in enumerate(bluecontour):
        area = cv2.contourArea(contour)
        if (area > 5000):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h),(219,152,52),2)

            cv2.putText(frame,"Blue",(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(219,152,52))

    for pic, contour in enumerate(greencontour):
        area = cv2.contourArea(contour)
        if (area > 5000):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h),(113,204,46),2)

            cv2.putText(frame,"Green",(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(113,204,46))

    for pic, contour in enumerate(yellowcontour):
        area = cv2.contourArea(contour)
        if (area > 5000):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h),(111,220,247),2)

            cv2.putText(frame,"Yellow",(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(111,220,247))

    for pic, contour in enumerate(orangecontour):
        area = cv2.contourArea(contour)
        if (area > 5000):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h),(51,118,220),2)

            cv2.putText(frame,"Orange",(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(51,118,220))