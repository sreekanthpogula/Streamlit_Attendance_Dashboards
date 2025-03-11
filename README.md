# 📊 Employee Attendance Dashboard

A **Streamlit** dashboard to track employee attendance, showing **Work from Home (WFH)** and **Work from Office (WFO)** data with interactive visualizations and filters.

## 🚀 Features
- 📅 **Date Range Filters** to view attendance trends
- 🏢 **Department Filters** for specific team insights
- 📊 **Charts & Graphs** (Pie Charts, Bar Charts) for WFH vs WFO trends
- 🔄 **Real-time Auto-Refresh** option
- 📂 **Multi-page support** (Summary, Department Analysis, Employee Details)
- ☁️ **Deployed on Streamlit Cloud**

## 📁 Folder Structure
```
📂 attendance-dashboard/
├── app.py                   # Main Dashboard Page
├── 📂 pages/                 # Multi-page support
│   ├── employee.py
│   ├── admin.py
│   ├── manager.py
├── 📄 requirements.txt       # Required Python libraries
├── 📄 README.md              # Project documentation
```

## 🛠️ Installation & Setup
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/attendance-dashboard.git
cd attendance-dashboard
```
### 2️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```
### 3️⃣ **Run the Streamlit App**
```sh
streamlit run app.py
```

## ☁️ Deploy on Streamlit Cloud
1. Push the code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Create a new app and select your GitHub repository.
4. Set `app.py` as the main file and deploy!

## 📎 API Integration
- Currently uses **dummy API data** (stored in `api/dummy_api.py`).
- Replace with **real API endpoints** for live attendance tracking.

## 🔥 Future Enhancements
✅ **Live API data fetching**
✅ **User authentication**
✅ **Employee attendance trends over time**
✅ **Export data to CSV/Excel**

---
💡 **Developed with ❤️ using Streamlit** | 📧 Need help? Contact [Your Email]

