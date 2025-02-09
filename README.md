# **HyperOptiDetect-X: Advanced YOLOv10 Object Recognition System**

## Overview
Welcome to **HyperOptiDetect-X**, an ultra-efficient, high-performance web application designed to revolutionize object detection in images and videos. Leveraging the cutting-edge YOLOv10 architecture, this system allows you to perform high-precision, real-time object detection with flexibility for various applications, whether it be for real-time performance or research-grade accuracy.

The app offers customizable configuration options, giving you the ability to adjust detection models, image size, and confidence thresholds. With support for both images and videos, **HyperOptiDetect-X** ensures rapid and reliable object recognition across diverse media formats.

## Features
- **Multiple Detection Models**: Choose from an array of YOLOv10 models, each offering a unique trade-off between speed and accuracy.
- **Fine-Tuned Customization**: Adjust image size and confidence threshold for optimized detection results.
- **Seamless Real-Time Processing**: Experience near-instant results, with an intuitive progress indicator.
- **Multi-Format Support**: Process both images and videos effortlessly.
- **Effortless Results**: Easily download the annotated files after processing.

## Requirements
- Python 3.7+
- Flask
- OpenCV
- YOLOv10 Model from Ultralytics

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/hyperoptidetect-x.git
   cd hyperoptidetect-x
   ```

2. **Install dependencies:**
   Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

   Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv10 Model:**
   The app will automatically download the YOLOv10 model when needed. Ensure that you have a stable internet connection.

4. **Set up the file structure:**
   The app requires a folder called `static/results` to store uploaded and processed files. This folder will be created automatically when the app runs, but ensure it's in the correct location.

## Usage

1. **Run the application:**
   Start the Flask web server:
   ```bash
   python app.py
   ```

2. **Open the application:**
   Visit `http://127.0.0.1:5000` in your web browser.

3. **Upload a file for object detection:**
   - Select a model from the dropdown menu (e.g., `YOLOv10n`, `YOLOv10s`, `YOLOv10m`, etc.).
   - Choose an image or video file to upload.
   - Adjust the image size (320 to 1280) and confidence threshold (0 to 1) as needed.
   - Click the **Detect Objects** button to start processing.

4. **Wait for processing to finish:**
   The system will display a loading screen while processing your file. Processing time will depend on the file size and selected model.

5. **Download the annotated result:**
   Once processing is complete, the result will be shown on the page. You can view it directly in the browser and download it using the provided link.

## Model Details

- **YOLOv10n**: Fast, best for small images. Lightweight and ideal for real-time applications.
- **YOLOv10s**: Balanced model suitable for both images and videos. A good trade-off between speed and accuracy.
- **YOLOv10m**: Accurate and fast, suitable for medium-sized tasks.
- **YOLOv10b**: Highly accurate but slower, ideal for detailed object detection.
- **YOLOv10l**: Very accurate but slower, ideal for large-scale tasks and complex scenarios.
- **YOLOv10x**: The most accurate model but extremely slow, ideal for research or high-precision tasks.

## File Formats Supported
- **Images**: jpg, jpeg, png, bmp, gif
- **Videos**: mp4, avi, mov, mkv

## Directory Structure

```
/project-directory
  ├── /static
  │    ├── /results                # Folder to store processed files
  │    ├── /css                    # Contains CSS files
  │    ├── /js                     # Contains JavaScript files
  ├── app.py                       # Flask application
  ├── /ultralytics                 # All the models data gathered from ultralytics
  ├── requirements.txt             # Python dependencies
  ├── index.html                   # HTML frontend template
  ├── README.md                    # Project documentation
  ├── LICENSE                      # License file
```

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Credits

- **YOLOv10** model by [Ultralytics](https://github.com/ultralytics/ultralytics)
- **OpenCV** for video and image processing
- **Flask** for the web framework
