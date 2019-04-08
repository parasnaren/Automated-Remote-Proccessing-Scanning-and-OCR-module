# byte-me
Developing an Automised Scanning and Storage system, that implements OCR to extract text from a scanned RC Card and store the structured data into a Database.

# Data Flow

### Implementation of input :

Build an Android app that works as a scanner, by using the smartphone's camera. 
The app would act as an IP Camera that would establish a socket connection over the network.
This port would be opened on the Web App running OpenCV to read the frames from the feed.
Inverse Binary Thresholding followed by dilation to get image boundaries.
Contouring of the boundaries to obtain the optimal frame.

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


