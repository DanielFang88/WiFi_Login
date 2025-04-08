# 🚀 VCCCD WiFi Auto Login Script

This project automatically logs into the VCCCD student WiFi portal after connection, eliminating manual login.

GitHub Repository: [https://github.com/DanielFang88/WiFi_Login](https://github.com/DanielFang88/WiFi_Login)

---

## 📆 Features

- ✅ Simulates browser-based POST login request
- ✅ Supports configuration via `.env` file
- ✅ Can be packaged into `.exe` and run on startup
- ✅ Works with Python 3.x

---

## 🛠️ Usage

### 1. Clone the repository

```bash
git clone https://github.com/DanielFang88/WiFi_Login.git
cd WiFi_Login
```

### 2. Install dependencies

```bash
pip install python-dotenv requests
```

### 3. Create a `.env` file

In the root directory, create a file named `.env`:

```dotenv
VCCCD_USERNAME=your_username
VCCCD_PASSWORD=your_password
```

### 4. Run the script

```bash
python vcccd_login.py
```

---

## 🔐 Security Tip

Make sure the `.env` file is added to `.gitignore` to prevent uploading sensitive information to GitHub!

```
.env
```

---

## 📁 Project Structure

```
.
├── vcccd_login.py             # Login script
├── .env                       # Contains user credentials (not committed)
├── .env.example               # Sample configuration
├── wifi_auto_login_summary.md # Project development summary
├── README.md
└── requirements.txt
```

---

## ✨ Author

- Daniel Fang  
- Powered by Python, Fiddler, ChatGPT
