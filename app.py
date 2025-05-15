# app.py

from flask import Flask, render_template, request, send_file, redirect, url_for
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

current_image_path = None
history_stack = []
redo_stack = []


def process_image(img, operation, **kwargs):
    if operation == 'grayscale':
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif operation == 'blur':
        k = int(kwargs.get('k', 5))
        if k % 2 == 0:
            k += 1
        return cv2.GaussianBlur(img, (k, k), 0)
    elif operation == 'canny':
        t1 = int(kwargs.get('t1', 100))
        t2 = int(kwargs.get('t2', 200))
        return cv2.Canny(img, t1, t2)
    elif operation == 'sharpen':
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(img, -1, kernel)
    elif operation == 'brightness':
        val = int(kwargs.get('value', 0))
        return cv2.convertScaleAbs(img, alpha=1, beta=val)
    elif operation == 'contrast':
        val = float(kwargs.get('value', 1.0))
        return cv2.convertScaleAbs(img, alpha=val, beta=0)
    elif operation == 'bw':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        return bw
    elif operation == 'flip':
        return cv2.flip(img, 1)
    elif operation == 'rotate':
        return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif operation == 'noise':
        noise = np.random.normal(0, 25, img.shape).astype(np.uint8)
        noisy_img = cv2.add(img, noise)
        return noisy_img
    elif operation == 'remove_bg':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
        bg_removed = cv2.bitwise_and(img, img, mask=mask)
        return bg_removed
    else:
        return img


@app.route('/', methods=['GET', 'POST'])
def index():
    global current_image_path, history_stack, redo_stack
    if request.method == 'POST':
        if 'image' in request.files:
            file = request.files['image']
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            current_image_path = path
            history_stack = [path]
            redo_stack = []
            return redirect(url_for('index'))
        elif request.form.get('operation'):
            operation = request.form['operation']
            if operation == 'undo' and len(history_stack) > 1:
                redo_stack.append(history_stack.pop())
                current_image_path = history_stack[-1]
            elif operation == 'redo' and redo_stack:
                restored = redo_stack.pop()
                history_stack.append(restored)
                current_image_path = restored
            elif current_image_path:
                img = cv2.imread(current_image_path)
                kwargs = request.form.to_dict()
                kwargs.pop('operation', None)
                processed = process_image(img, operation, **kwargs)
                result_path = os.path.join(UPLOAD_FOLDER, 'processed.png')
                cv2.imwrite(result_path, processed)
                history_stack.append(result_path)
                redo_stack = []
                current_image_path = result_path
    return render_template('index.html', image=current_image_path)


@app.route('/download')
def download():
    if current_image_path:
        return send_file(current_image_path, as_attachment=True)
    return "No image to download"


if __name__ == '__main__':
    app.run(debug=True)
