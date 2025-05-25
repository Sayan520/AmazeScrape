<div id="top"></div>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<!-- Project Icon with Title -->
<br />
<div align="center">
  <a href="https://github.com/Sayan520">
    <img src="https://cdn-icons-png.flaticon.com/128/5065/5065181.png" alt="Logo" width="80" height="80"/> 
  </a>

<h3 align="center">AmazeScrape: Amazon Web Scraper</h3>

  <p align="center">
    A responsive, elegant frontend + Flask-powered Amazon product scraping tool with real-time feedback, progress bar, and download options.
    <br />
    <a href="https://github.com/Sayan520/AmazeScrape"><strong>Explore the Repo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Sayan520/AmazeScrape/blob/main/app.py">View Backend</a>
    ·
    <a href="https://github.com/Sayan520/AmazeScrape/blob/main/scrape_amazon.py">View Scraper Module</a>
    ·
    <a href="https://linkedin.com/in/sayaan-ghosh">Contact Me</a>
  </p>
</div>

---
<!-- Project Details -->

## 🖼️ Project Preview

![AmazeScrape Screenshot](/AmazeScrape.jpg)

---

## 🎯 Objectives

- Build a user-friendly web interface for Amazon product scraping
- Allow users to choose number of pages, filename, and export format (CSV/Excel)
- Provide real-time scraping feedback with spinner, toasts, modal confirmations
- Offer auto file download with smart naming
- Simulate progress bar updates (extendable to real-time)
- Maintain responsive and modern UI/UX

---

## 🛠️ Tools & Technologies

### 🚀 Technologies
[![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white)]()
[![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black)]()

### 🔧 Tools
[![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white)](https://github.com/Sayan520/AmazeScrape)
[![Postman](https://img.shields.io/badge/-Postman-FF6C37?logo=postman&logoColor=white)](https://www.postman.com/)

---

## 📦 Features

### ✅ Form Input & Validation
- Search Query, Number of Pages, Format (CSV/Excel), and Filename inputs
- Required fields with validation feedback before submission

### 🔄 Loading Spinner
- Animated spinner during scraping (better than static text)
- Hidden on completion or error

### 🧠 Smart Confirmation Modal
- SweetAlert2 modal with confirmation prompt before starting
- Dynamic query and page info shown in the modal

### 🔔 Toast Notifications
- Input validation errors
- Scraping success with download
- Network or backend errors

### 📥 Download System
- File auto-downloads via Blob link
- Extracts filename from `Content-Disposition` or falls back to user input

### 📊 Progress Bar (Simulated)
- Responsive progress bar updating dynamically
- Easily connectable to backend events in future

### 📄 Format Preview
- Shows preview filename with extension hint:
  - `output.csv` (Comma Separated)
  - `output.xlsx` (Microsoft Excel)
- Updates live as user changes format or filename

---

## 🧪 Installation Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Sayan520/AmazeScrape.git
cd AmazeScrape
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source .\venv\Scripts\activate  # on Mac: venv/bin/activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Run the app:**
```bash
python app.py
```
5. **Open your browser and visit:**
```bash
http://127.0.0.1:5000
```
## 📬 Connect with Me

<div align="left">

[![LinkedIn - Sayan Ghosh](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0A66C2)][reach_linkedin]  
[![Gmail - sayan520](https://img.shields.io/badge/Gmail-sayan520-red?style=for-the-badge&logo=gmail&logoColor=white&labelColor=EA4335)][reach_gmail]  
[![Instagram - @mr_saayaann](https://img.shields.io/badge/Instagram-@mr_saayaann-pink?style=for-the-badge&logo=instagram&logoColor=white&labelColor=E4405F)][reach_instagram]

</div>
---

## 📜 License
This project is open-source and free to use for educational and personal projects.

---

**Take Care & Happy Coding! 💻🚀**

<!-- CONTACT LINKS -->
[reach_linkedin]: https://linkedin.com/in/sayaan-ghosh  
[reach_gmail]: mailto:ghoshsayan5205@gmail.com?subject=GitHub  
[reach_instagram]: https://www.instagram.com/mr_saayaann