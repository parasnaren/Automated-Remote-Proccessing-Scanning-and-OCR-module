# byte-me
Developing an Automised Scanning and Storage system, that implements OCR to extract text from a scanned RC Card and store the structured data into a Database.

# Data Flow

### Android App

- The app scans multiple frames in real time and relays them from the smartphone camera to a port on the network. 
- The frames are sent as a HTTP stream to the server
- The app has been made completely light-weight. All the computation takes place completely at the server end and the app is responsible solely for relaying video feed.

### Identification of the RC card from its background:

- Thresholding: Simple Thresholding is implemented on a grayscale image over a particular threshold value
- Dilation: The boundaries are enhanced using dilation. It is useful in joining broken parts of an object
- Contouring: The required image is obtained based on its boundary points based on the contour constraints
- Overlay: The image obtained is superimposed on the original image to obtain the precise boundaries

### Process images to pick the optimal:

- A single channel of an image (grayscale) and convolve it with a 3 x 3 kernel. The variance of the kernel is found
- If an image contains high variance then there is a wide spread of responses, and therefore, an in-focus image. But if there is very low variance, then there is a tiny spread of responses, indicating there are very little edges in the image. As we know, the more an image is blurred, the less edges there are.
- The variance of all the images are found and the image with the max value of variance ( ie., least blurry) is picked.

### Extract the text features using TESSERACT:

Tesseract is used to extract characters from the picked image.

### Regex

Regular expressions are implemented to uniquely identify every value for a given key-value pair, since the RC cards of the various states in India have different syntaxes for their keys.

# Files

### RecognitionCam.zip

Django web application.
Set up computer as server and run the mobile application as client.


# Libraries and Dependencies

- Google Tesseract
- OpenCV
- Django
- Android Studio
- Ajax
- SQLite


