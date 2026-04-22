# Team_coding_divas_Smart_Irrigation_System
Team Name: Coding Divas
# 🌱 Smart Irrigation System

## 📌 Overview

The **Smart Irrigation System** is an IoT-based project designed to automate the irrigation process by monitoring soil moisture levels. It helps in efficient water usage by supplying water only when required, reducing wastage and manual effort.

---

## 🎯 Objectives

* Automate irrigation using sensors
* Reduce water wastage
* Improve plant health
* Minimize human intervention

---

## 🎥 Prototype Demonstration

👉 Watch the working model here:
🔗 https://drive.google.com/drive/folders/1J_whRXorgc-nUot9S8z-mQMU3f8PbknQ?usp=sharing

---

## ⚙️ Components Used

### 🔌 Hardware

* Microcontroller (Arduino / ESP8266 / ESP32)
* Soil Moisture Sensor
* DHT11/DHT22 Sensor (optional)
* Relay Module
* Water Pump
* Connecting Wires
* Power Supply

### 💻 Software

* Arduino IDE
* Embedded C / C++
* Python (for data processing)
* JavaScript (for visualization)
* MySQL (for database storage)
* (Optional) IoT Platform (Blynk / Firebase / MQTT)

---

## 🧠 Data Structures Used

| Structure     | Language   | Used For                     |
| ------------- | ---------- | ---------------------------- |
| List          | Python     | All moisture readings        |
| Dictionary    | Python     | Sensor values + system state |
| deque (Queue) | Python     | Latest 5 readings (FIFO)     |
| List          | Python     | Weather types                |
| Array         | JavaScript | Chart data points            |
| Tables        | MySQL      | Persistent storage           |

---

## 🔄 Working Principle

1. The soil moisture sensor reads the moisture level of the soil.
2. The microcontroller processes the sensor data.
3. If moisture level is below a threshold:

   * Water pump turns **ON**
4. If moisture level is above threshold:

   * Water pump turns **OFF**
5. (Optional) Data is stored in database and visualized on dashboard.

---

## 🧠 System Architecture

* Sensors → Microcontroller → Relay → Pump
* Microcontroller → Python Processing → MySQL Database
* Database → JavaScript Dashboard (Charts)

---

## 💡 Features

* Automatic watering system
* Water conservation
* Real-time monitoring
* Data visualization using charts
* Low-cost and scalable solution

---

## 🚀 Future Enhancements

* Mobile app integration
* Weather-based irrigation control
* Machine Learning for prediction
* Solar-powered system
* Multi-zone irrigation support

---

## 📂 Project Structure

```
Smart_Irrigation_System/
│── code/
│   └── main.ino
│── backend/
│   └── data_processing.py
│── frontend/
│   └── dashboard.js
│── database/
│   └── schema.sql
│── README.md
│── documentation/
```

---

## 🛠️ Installation & Setup

1. Install Arduino IDE
2. Connect hardware components properly
3. Upload the code to the microcontroller
4. Set up Python environment and MySQL database
5. Run backend script
6. Open dashboard for visualization

---

## 📊 Applications

* Agriculture fields
* Home gardening
* Greenhouses
* Smart farming systems

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgment

Thanks to all open-source contributors and IoT communities for guidance and support.
