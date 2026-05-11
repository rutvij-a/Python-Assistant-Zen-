# Python Assistant ZEN 1.0 🤖🎙️

**ZEN 1.0** is a Python-based personal voice assistant designed to perform daily tasks through voice commands. It can interact with users, automate system operations, search the web, control media, provide weather and news updates, send emails, take notes, and more.

---

## 📌 Project Overview

The **Python Assistant ZEN 1.0** project aims to simplify daily computer tasks using voice-based interaction and automation.

Unlike basic voice assistants, ZEN 1.0 provides multiple advanced features such as system control, web browsing, media handling, camera operations, email support, and mathematical calculations. It responds to user commands through speech, making the interaction more natural, convenient, and engaging.

---

## 🚀 Features

* 🎙️ **Voice Command Recognition**
* 🕒 **Time, Date & Weekday Retrieval**
* 💻 **System Operations**

  * Lock screen
  * Restart system
  * Shutdown system
  * Log out
  * Empty recycle bin
* 🌐 **Web & Application Search**

  * Search Google
  * Search Wikipedia
  * Open websites
  * Open applications like MS Word, CodeBlocks, and Eclipse
* 🎵 **Media Control**

  * Play songs
  * Play videos
  * Open images
* 🌦️ **Weather Updates**
* 📰 **News Headlines**
* 📷 **Camera & Recording Functions**

  * Capture photos
  * Record videos
  * Record audio clips
* 🧮 **Mathematical Calculations**

  * Solve equations
  * Wolfram Alpha integration
* 📧 **Email Handling**
* 📝 **Note-Taking**

  * Create notes
  * View saved notes

---

## 🛠️ Technologies Used

| Technology / Module | Purpose                    |
| ------------------- | -------------------------- |
| Python              | Core Programming Language  |
| SpeechRecognition   | Voice command recognition  |
| pyttsx3             | Text-to-speech response    |
| Wikipedia API       | Wikipedia search           |
| Webbrowser          | Open websites              |
| Wolfram Alpha API   | Mathematical calculations  |
| smtplib             | Email sending              |
| OpenCV              | Camera and video recording |
| datetime            | Time and date retrieval    |
| OS / Subprocess     | System operations          |

---

## ⚙️ How It Works

1. ZEN 1.0 starts and welcomes the user.
2. It retrieves the current time and date.
3. The assistant waits for a voice command.
4. User gives a verbal instruction.
5. ZEN processes the command.
6. The required task is executed.
7. The assistant responds audibly with the result.

---

## 📂 Project Structure

```plaintext
Python-Assistant-ZEN/
│
├── main.py
├── requirements.txt
├── notes/
├── media/
├── screenshots/
└── README.md
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Python-Assistant-ZEN.git
```

### 2. Open Project Folder

```bash
cd Python-Assistant-ZEN
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 📋 Requirements

Add these libraries inside `requirements.txt`:

```txt
SpeechRecognition
pyttsx3
wikipedia
wolframalpha
opencv-python
PyAudio
requests
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🎤 Example Commands

```plaintext
What is the time?
What is today's date?
Search Wikipedia for Python programming
Open Google
Play music
Take a photo
Record audio
Send email
Create a note
Shutdown the system
Restart the computer
What is the weather today?
Tell me the latest news
Calculate 25 plus 75
```

---

## 🖥️ Project Demonstration

When the assistant starts, it welcomes the user and provides basic system information such as current date and time. After that, it continuously listens for voice commands.

Based on the command, ZEN 1.0 performs the appropriate task, such as opening websites, playing media, sending emails, capturing photos, solving calculations, or controlling system operations.

---

## 🌟 Advantages

* Hands-free computer control
* User-friendly voice interaction
* Saves time by automating tasks
* Supports multiple daily-use features
* Can be expanded with new modules
* Improves accessibility and convenience

---

## 🔮 Future Enhancements

* GUI-based interface
* Wake word detection
* AI chatbot integration
* Multi-language voice support
* Improved security for system commands
* Smart home device integration
* Better natural language understanding

---

## ⚠️ Security Note

Some features such as email sending, shutdown, restart, and system lock require careful handling. Avoid sharing personal credentials in source code. Use environment variables or configuration files for sensitive information.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make changes
4. Commit your updates
5. Submit a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Rutvij A**

---

## ⭐ Support

If you found this project helpful, give it a ⭐ on GitHub!
