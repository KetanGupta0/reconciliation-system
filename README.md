# 🧾 Transaction Reconciliation System

A production-style backend system built using **Python, Pandas, and FastAPI** that performs transaction reconciliation between two datasets, detects mismatches, and generates downloadable Excel reports.

---

## 🚀 Features

* 📂 Upload CSV/Excel files dynamically via API
* 🔄 Data cleaning and transformation using Pandas
* ⚖️ Transaction reconciliation engine:

  * Matched records
  * Amount mismatches
  * Status mismatches
  * Missing transactions
* 📊 Multi-sheet Excel report generation
* 🌐 REST API built with FastAPI
* 🐳 Dockerized for easy deployment
* 🛡️ Schema validation & error handling

---

## 🧠 Key Concepts Implemented

* ETL Pipeline (Extract, Transform, Load)
* Data validation and schema enforcement
* Outer joins and reconciliation logic
* File handling in APIs (UploadFile)
* REST API design
* Error handling using HTTPException
* Docker containerization

---

## 📁 Project Structure

```bash
reconciliation-system/
│── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── utils/
│   ├── schemas/
│   └── main.py
│
│── data/
│── reports/
│── tests/
│── requirements.txt
│── Dockerfile
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd reconciliation-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
uvicorn app.main:app --reload
```

---

## 🐳 Run with Docker

```bash
docker build -t reconciliation-app .
docker run -p 8000:8000 reconciliation-app
```

---

## 🌐 API Endpoint

### 🔹 Reconcile & Download Report

```http
POST /reconcile/dynamic/
```

Upload two files → returns downloadable Excel report.

---

## 📊 Example Workflow

1. Upload two transaction files
2. System cleans and validates data
3. Reconciliation logic applied
4. Excel report generated
5. User downloads report

---

## ⚠️ Error Handling

* Invalid file format → returns 400
* Missing required columns → validation error
* Internal errors → safe API response

---

## 🔮 Future Enhancements

* Column auto-mapping
* Database integration
* Cloud storage (AWS S3)
* Async processing (Celery)
* Dashboard for visualization

---

## 👨‍💻 Author

**Chandra Kishor Gupta**
Senior Backend Developer (Laravel | Python | APIs)
