# WebEditingApp

A full-featured image editing web application built with **Flask**, **OpenCV**, and **Tailwind CSS**. This app provides a modern UI and supports real-time image manipulation right from your browser.

---

## 🚀 Features

- ✅ Image Upload & Preview
- 🖤 Dark/Light Theme Toggle (Tailwind CSS)
- 🎨 Image Processing Tools:
  - Grayscale
  - Gaussian Blur (slider)
  - Canny Edge Detection (dual sliders)
  - Sharpening
  - Brightness & Contrast Adjustment
  - Flip & Rotate
  - Black & White Conversion
  - Add Noise
  - Background Removal
- 🔁 Undo / Redo Support
- 💾 Download Final Image

---

## 📁 Project Structure
```
WebEditingApp/
├── app.py                  # Flask backend
├── requirements.txt
├── templates/
│   └── index.html          # Main HTML UI
├── static/
│   ├── css/
│   │   ├── style_light.css (optional)
│   │   └── style_dark.css (optional)
│   ├── js/
│   │   └── main.js         # Theme toggle handler (if separated)
│   └── uploads/            # Stores user-uploaded & processed images
└── README.md
```

---

## 🛠️ Installation

### 🔗 Clone the repository
```bash
git clone https://github.com/Mkaify/WebEditingApp.git
cd WebEditingApp
```

### 📦 Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
python app.py
```
Open your browser at `http://127.0.0.1:5000`

---

## ☁️ Deployment (Render / Railway)
1. Push the project to GitHub.
2. Go to [Render](https://render.com) → Create a new Web Service.
3. Connect your GitHub repo.
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Environment**: Python
5. Deploy!

---

## 📃 License
MIT License. Free to use and modify.

---

## 🙌 Author
**Muhammad Kaif ur Rehman**

If you like this project, consider ⭐️ starring the repo!
