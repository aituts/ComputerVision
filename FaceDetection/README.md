# Enabling Camera and performing Face Detection using Viola-Jones Face Detection Algo

Youtube Link: 
```
https://youtu.be/cPpK1hV2w0E
```
1. Install OpenCV
```
    pip install opencv-python
```
2. Download OpenCV package for CascadeClassifier
```
    https://github.com/opencv/opencv/tree/3.4.1 (Download ZIP)
```
3. Import CV
4. Enable Video Capture
5. Initialize Face Detection Classifier 
6. Writing the following logic
    * Convert the image into grayscale
    * Detect face with scale factor as 1.3 and minimum-neighbours as 5
    * Draw a green rectangle surrounding the face based on edges (BGR format)
    * Quit the program if pressed 'q' key
    
7. Release the camera
8. Clear and destroy all windows created by the program
