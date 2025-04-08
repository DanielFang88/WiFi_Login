🚀 VCCCD WiFi Auto Login ScriptThis project automatically logs into the VCCCD student WiFi portal after connection, eliminating manual login.
GitHub Repository: https://github.com/DanielFang88/WiFi_Login
📆 Features✅ Simulates browser-based POST login request
✅ Supports configuration via .env file
✅ Can be packaged into .exe and run on startup
✅ Works with Python 3.x
🛠️ Usage1. Clone the repositorygit clone https://github.com/DanielFang88/WiFi_Login.git
cd WiFi_Login2. Install dependenciespip install python-dotenv requests3. Create a .env fileIn the root directory, create a file named .env:
VCCCD_USERNAME=your_username
VCCCD_PASSWORD=your_password4. Run the scriptpython vcccd_login.py🔐 Security TipMake sure the .env file is added to .gitignore to prevent uploading sensitive information to GitHub!
.env📁 Project Structure.
├── vcccd_login.py             # Login script
├── .env                       # Contains user credentials (not committed)
├── .env.example               # Sample configuration
├── wifi_auto_login_summary.md # Project development summary
├── README.md
└── requirements.txt✨ AuthorDaniel Fang
Powered by Python, Fiddler, ChatGPT
