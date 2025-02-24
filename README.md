This project is a simple face recognition system that detects and identifies faces from a live webcam feed using OpenCV and the face_recognition library. 
The program loads known face images, encodes them, and compares them to faces detected in the video stream.

How it Works:
1. Load known images and encode them
2. Capture video from the webcam.
3. Detect faces in each frame and encode them.
4. Compare detected faces with known encodings.
5. Draw a rectangle around recognized faces and display their names.
6. Display the video stream with labeled faces.

Usage:
1. Make sure to replace "upload jpeg" with the actual file paths of the known face images.
2. Modify known_face_names to include the names of the people in the images.
3. The script uses OpenCV's VideoCapture(0) to access the default webcam. Change the index if using an external camera.
4. Ensure your IDE can access your camera
5. If on Mac, check your camera settings across devices to allow your IDE to store and use your photos
6. After running the script, type 'q' in the terminal to exit the program



   
