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
  * Execute file operations remotely.([bevijaygupta.medium.com][1])

* **📷 Media Access**

  * Capture photos using the device's camera.
  * Record audio through the microphone.
  * Access and exfiltrate media files.([checkpoint.com][2], [cyfirma.com][3])

* **📞 Communication Control**

  * Monitor incoming and outgoing calls.
  * Read and send SMS messages.([github.com][4], [infosecinstitute.com][5])

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

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/darkefx/DarkAndroidRAT.git
   ```



2. **Configure Firebase:**

   * Set up a Firebase project.
   * Enable Realtime Database and Authentication.
   * Download the `google-services.json` file and place it in the `app/` directory.

3. **Build the APK:**

   * Open the project in Android Studio.
   * Build the project to generate the APK file.([darkreading.com][6])

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
* **GitHub:** [darkefx](https://github.com/darkefx)([checkpoint.com][2])

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📷 Screenshots

*Include relevant screenshots or GIFs demonstrating the RAT's capabilities.*

---

## 📚 Resources

* [Firebase Documentation](https://firebase.google.com/docs)
* [Android Accessibility Services](https://developer.android.com/guide/topics/ui/accessibility/services)
* [Android Developers Guide](https://developer.android.com/guide)

---

*Note: Ensure that all usage complies with applicable laws and regulations. Always obtain proper authorization before deploying tools like DarkAndroidRAT.*

---

[1]: https://bevijaygupta.medium.com/wanna-build-a-rat-remote-access-trojan-71607edd618f?utm_source=chatgpt.com "Wanna Build a (RAT) Remote Access Trojan?? | by Vijay Kumar Gupta"
[2]: https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-remote-access-trojan/?utm_source=chatgpt.com "What is Remote Access Trojan (RAT)? - Check Point Software"
[3]: https://www.cyfirma.com/research/neptune-rat-an-advanced-windows-rat-with-system-destruction-capabilities-and-password-exfiltration-from-270-applications/?utm_source=chatgpt.com "NEPTUNE RAT : An advanced Windows RAT with System ... - cyfirma"
[4]: https://github.com/okhosting/awesome-cyber-security/blob/main/README.md?utm_source=chatgpt.com "awesome-cyber-security/README.md at main - GitHub"
[5]: https://www.infosecinstitute.com/resources/incident-response-resources/network-traffic-analysis-for-ir-discovering-rats/?utm_source=chatgpt.com "Network Traffic Analysis for IR — Discovering RATs - Infosec"
[6]: https://www.darkreading.com/cyberattacks-data-breaches/hunters-international-disguises-novel-sharprhino-rat-as-legitimate-network-tool?utm_source=chatgpt.com "Hunters International Masks SharpRhino RAT as Legit Network ..."

