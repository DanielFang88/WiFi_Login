import requests
import os

os.environ['NO_PROXY'] = 'captiveportal-login.vcccd.edu'
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

login_url = "https://captiveportal-login.vcccd.edu/cgi-bin/login"

payload = {
    "user": "yourusername",           # your username
    "password": "yourpassword",     # your password
    "url": "http://vcccd.edu",  # redirect URL after login
    "cmd": "authenticate"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://captiveportal-login.vcccd.edu/cgi-bin/login"
}

try:
    response = requests.post(login_url, data=payload, headers=headers, verify=False)
    print("✅ Sent login POST. Response code:", response.status_code)

    with open("login_response_real.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    if "Authentication successful" in response.text:
        print("🎉 Login successful!")
    else:
        print("⚠️ Login failed or not confirmed.")

except Exception as e:
    print("❌ Error:", e)
