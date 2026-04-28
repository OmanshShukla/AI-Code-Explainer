# 🤖 AI Code Explainer

An AI-powered web application that explains code in simple, human-readable language using **LLaMA3 via Ollama**. Built with **Streamlit**, this tool helps students and developers quickly understand complex code logic.

---

## 🚀 Features

* 🔍 Explain code in plain English
* 💡 Supports multiple programming languages
* ⚡ Fast local inference using Ollama (no API required)
* 🧠 Uses LLaMA3 for intelligent explanations
* 🖥️ Simple and clean UI with Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Ollama**
* **LLaMA3**

---

## 📸 Demo

### 🧾 Input

![Input](assets/input.png and assets/input1.png)

### 📖 Output

![Output](assets/output.png and assets/output1.png)

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/OmanshShukla/AI-Code-Explainer.git
cd AI-Code-Explainer
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install Ollama

Download and install Ollama from: https://ollama.com

---

### 4️⃣ Pull LLaMA3 Model

```bash
ollama run llama3
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
AI-Code-Explainer/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── assets/
    ├── input.png,input1.png
    └── output.png,output1.png
```

---

## ⚙️ How It Works

1. User inputs code into the Streamlit interface
2. The code is sent to the LLaMA3 model via Ollama
3. The model processes and generates a simplified explanation
4. The explanation is displayed in the UI

---

## 📌 Future Improvements

* 📁 Upload code files (.py, .java, etc.)
* 🧠 Line-by-line explanation mode
* 🌙 Dark mode UI
* 🗣️ Voice-based explanation
* 🐞 Error detection and debugging suggestions

---

## 👨‍💻 Author

**Omansh Shukla**
B.Tech CSE (AI)

---

## ⭐ Show Your Support

If you like this project, please ⭐ the repository on GitHub!
