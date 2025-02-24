import cv2
import face_recognition

# Load known images and encode faces and store in array
known_face_encodings = []
known_face_names = []

image_of_person1 = face_recognition.load_image_file("upload jpeg") #Load an image 
encoding_of_person1 = face_recognition.face_encodings(image_of_person1)[0] #Encode the image into the memory and store

#Repeat for a second image/second person

image_of_person2 = face_recognition.load_image_file("upload jpeg")
encoding_of_person2 = face_recognition.face_encodings(image_of_person2)[0]

# Add encodings and names to our lists
known_face_encodings = [encoding_of_person1, encoding_of_person2]
known_face_names = ["Person 1", "Person 2"] #Insert user's names

# Initialize video capture (0 is usually the built-in camera, change number for your preffered choice of camera).
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame of users face
    ret, frame = video_capture.read()  

    # Resize for better processing (optional based on device)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) 

    # Convert the image to RGB (OpenCV uses BGR by default)
    rgb_small_frame = small_frame[:, :, :-1]

    # Detect faces and encode them
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Create an array of faces and compare images to faces stored from camera
    face_names = [] 
    for face_encoding in face_encodings:
        # Compare faces with known faces stored from above jpegs
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown" # If face does not match jpeg

        # If a match was found in known_face_encodings, use the first match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up since the frame we processed was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Label the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()