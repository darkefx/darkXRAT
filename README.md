# darkXRAT
---
**darkXRAT** is an advanced Android Remote Access Trojan (RAT) developed by `dark_efx` (F Society). Designed for ethical hacking and cybersecurity research, it provides comprehensive remote control capabilities over Android devices.

---

## 📌 Features

* **📍 Location Tracking**

  * Retrieve real-time GPS coordinates.
  * Generate Google Maps links for precise location visualization.

* **📍 SMS Logging**

  * Receives and uploads all sms live to server.
  * This feature helps in bypassing 2fa,otp e.t.c.

* **🔐 Key Logging**

  * Automated upload of key logs after every 2 minutes.
  * This Feature is helpful for reading chats and login credentials.

* **🔐 Permission Management**

  * Automated granting of critical permissions using Accessibility Services.
  * Bypass manual user interactions for seamless operation.
    

* **📁 File Management**

  * Browse, upload, and download files from the device's storage.
  * Execute file operations remotely.

* **📷 Media Access**

  * Capture photos using the device's camera.
  * Record audio through the microphone.
  * Access and exfiltrate media files.

* **📞 Communication Control**

  * Monitor incoming and outgoing calls.
  * Read and send SMS messages.

* **🖥️ Remote Interface**

  * Stream the device's screen in real-time.
  * Simulate touch inputs and gestures.

* **📡 Command & Control (C2)**

  * Utilizes Firebase Realtime Database for command reception and data exfiltration.
  * Supports dynamic server URL updates through remote configurations.

# 📌 Next Version Upcoming Features

* **🔄 Persistence Mechanisms**

  * Employs multiple strategies to maintain long-term access.
  * Automatically reinstalls or reactivates components as needed.

* **🛡️ Uninstall Protection**

  * Prevents uninstallation of the RAT app through Accessibility-based auto-click prevention mechanisms.
  * Ensures persistent presence on the target device.

* **🛰️ Stealth Agent Deployment**

  * Installs a secondary hidden agent app with Accessibility permissions.
  * Maintains control even if the main app is removed.

---

## ⚙️ Installation & Setup

1. **Install ngrok server:**

   ```bash
   bash install_ngrok_v3.sh
   ```

1. **Set Flask Endpoint:**

   ```bash
   mkdir android_upload_server && cd android_upload_server
   nano server.py
   ```
   Paste the flaskserver.py File Code



2. **Build the APK:**

   * Open the project in Android Studio.
   * use the apk zip to import app to android studio
   * Delete my `google-services.json` file in the `app/` directory , change package name, replace server links in 4-5 places in code with your ngrok link and connect 
     to firebase.

3. **Configure Firebase:**

   * Set up a Firebase project.
   * Enable Realtime Database and Authentication.
   * Download the `google-services.json` file and place it in the `app/` directory.

4. **Deploy to Target Device:**

   * Install the APK on the target Android device.
   * Grant necessary permissions, including Accessibility Services.

---

## 🧠 Legal Disclaimer

This project is intended solely for educational and ethical penetration testing purposes. Unauthorized use of this software to access or control devices without explicit consent is illegal and unethical. The developer, `dark_efx`, assumes no responsibility for any misuse or damage caused by this tool.

---

## ⚠️ Warning

**DarkAndroidRAT** is a powerful tool that can compromise the privacy and security of individuals. Use it responsibly and only in environments where you have explicit permission to conduct security assessments. Unauthorized deployment may lead to severe legal consequences.

---

## 👤 Author

* **Name:** `dark_efx`
* **Alias:** F Society
* **GitHub:** [darkefx](https://github.com/darkefx)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---


## 📺 Project Demo

[![Watch the demo](https://img.youtube.com/vi/gvYXaKMxsu0/0.jpg)](https://www.youtube.com/watch?v=gvYXaKMxsu0)



> ⚠️ **Disclaimer**  
> This video and project are intended for **educational and ethical cybersecurity research** only.  
> All demonstrations are done in **controlled environments** and comply with **legal and responsible disclosure guidelines**.  
> Unauthorized use of any code or method shown is strictly prohibited.


