from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import cv2
import time
from ultralytics import YOLOv10

app = Flask(__name__)
UPLOAD_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
def load_model(model_id):
    return YOLOv10.from_pretrained(f'jameslahm/{model_id}')

# Check if file is an image
def is_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png', 'bmp', 'gif']

# Check if file is a video
def is_video(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['mp4', 'avi', 'mov', 'mkv']

# Process video frame-by-frame
def process_video(video_path, model, output_path, imgsz, conf_threshold):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use H.264 codec
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model.predict(source=frame, imgsz=imgsz, conf=conf_threshold)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

    cap.release()
    out.release()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    start_time = time.time()
    file = request.files["file"]
    model_id = request.form["model"]
    image_size = int(request.form["image_size"])
    conf_threshold = float(request.form["conf_threshold"])
    model = load_model(model_id)

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    if is_image(file.filename):
        # Process image
        image = cv2.imread(file_path)
        results = model.predict(source=image, imgsz=image_size, conf=conf_threshold)
        annotated_image = results[0].plot()
        output_path = os.path.join(UPLOAD_FOLDER, "annotated_" + file.filename)
        cv2.imwrite(output_path, annotated_image)
        file_type = "image"
    elif is_video(file.filename):
        # Process video
        output_path = os.path.join(UPLOAD_FOLDER, "annotated_" + file.filename)
        process_video(file_path, model, output_path, image_size, conf_threshold)
        file_type = "video"
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    end_time = time.time()
    processing_time = round(end_time - start_time, 2)

    return jsonify({
        "output_file": f"/download/{os.path.basename(output_path)}",
        "time": processing_time,
        "type": file_type
    })

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)