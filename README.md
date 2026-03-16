# 📊 WhatsApp Chat Analyzer

A **Data Analysis Web App** that analyzes exported WhatsApp chat data and generates meaningful insights such as message statistics, activity timelines, word usage, emoji analysis, and activity heatmaps.

The project helps visualize chat patterns and understand communication behavior using **Python, Pandas, and Streamlit**.

---

## 🚀 Features

* 📈 **Chat Statistics**

  * Total Messages
  * Total Words
  * Media Shared
  * Links Shared

* 👥 **Most Active Users**

  * Identify the most active participants in group chats

* ☁️ **Word Cloud**

  * Visual representation of frequently used words

* 🔤 **Most Common Words**

  * Displays the most frequently used words in the chat

* 😀 **Emoji Analysis**

  * Shows the most commonly used emojis

* 📅 **Monthly Timeline**

  * Message activity across months

* 📆 **Daily Timeline**

  * Message activity across days

* 🔥 **Activity Heatmap**

  * Displays the most active hours across the week

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **WordCloud**
* **Emoji**
* **Streamlit**

---

## 📂 Project Structure

```
whatsapp-chat-analyzer
│
├── app.py                # Streamlit application
├── helper.py             # Analysis functions
├── preprocessor.py       # Chat data preprocessing
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Export a WhatsApp chat as a `.txt` file from WhatsApp.
2. Upload the file into the application.
3. The system preprocesses the chat data.
4. Various analysis functions extract insights such as:

   * Message counts
   * Word frequency
   * Emoji usage
   * Activity timelines
5. Results are displayed using interactive visualizations.

---

## 📥 Export WhatsApp Chat

To use this application:

1. Open WhatsApp
2. Open the chat you want to analyze
3. Click **More Options (⋮)**
4. Select **Export Chat**
5. Choose **Without Media**
6. Upload the exported `.txt` file into the application

---

## 💻 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
```

### Navigate to project directory

```bash
cd whatsapp-chat-analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📊 Example Insights

The analyzer generates insights such as:

* Total messages sent in the chat
* Most active participants
* Most frequently used words
* Emoji usage statistics
* Message activity by **day, month, and hour**
* Weekly activity heatmap

---

## 📌 Future Improvements

* Sentiment analysis of chats
* Chat topic detection using NLP
* Advanced visualizations
* Deployment on **Streamlit Cloud / AWS / Heroku**

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, please consider **starring the repository**!

