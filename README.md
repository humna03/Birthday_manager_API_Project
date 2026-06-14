# 🎂 Birthday Manager API Project

A FastAPI-based Birthday Management System that allows users to store, manage, update, and delete birthday records. The application also integrates Groq AI to generate personalized gift suggestions based on the user's relationship and preferences.

---

# 📖 Project Description

Managing birthdays manually can be difficult, especially when dealing with multiple friends, family members, and colleagues. This project provides a centralized solution for storing birthday information and retrieving it through REST APIs.

In addition to birthday management, the system uses Artificial Intelligence through Groq AI to suggest personalized gift ideas, making the application more useful and interactive.

---

# 🚀 Features

✅ Add new birthday records

✅ Retrieve all birthday records

✅ Retrieve a specific birthday by ID

✅ Update birthday information

✅ Delete birthday records

✅ Generate AI-powered gift suggestions

✅ Automatic API documentation with Swagger UI

✅ Request and response validation using Pydantic

---

# 🛠 Technologies Used

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| FastAPI       | Backend API Framework           |
| SQLModel      | Data Modeling                   |
| Pydantic      | Request & Response Validation   |
| Groq AI       | AI Gift Recommendation          |
| Python Dotenv | Environment Variable Management |
| Swagger UI    | API Testing & Documentation     |

---

# 📂 Project Structure

```text
Birthday_manager_API_Project/
│
├── main.py
├── schemas.py
├── database.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

---

# 📊 Birthday Data Model

Each birthday record contains the following information:

| Field        | Description                       |
| ------------ | --------------------------------- |
| id           | Unique identifier                 |
| name         | Person's name                     |
| birthday     | Date of birth                     |
| relationship | Friend, Family, Colleague, etc.   |
| phone        | Contact number (optional)         |
| notes        | Additional information (optional) |

---

# 🔗 API Endpoints

## 1. Add Birthday

```http
POST /birthdays
```

### Example Request

```json
{
  "name": "sara",
  "birthday": "2000-06-14",
  "relationship": "Friend",
  "phone": "03001234567",
  "notes": "Likes gaming"
}
```

---

## 2. Get All Birthdays

```http
GET /birthdays
```

Returns all stored birthday records.

---

## 3. Get Birthday By ID

```http
GET /birthdays/{birthday_id}
```

Returns a specific birthday record.

---

## 4. Update Birthday

```http
PUT /birthdays/{birthday_id}
```

Updates an existing birthday record.

---

## 5. Delete Birthday

```http
DELETE /birthdays/{birthday_id}
```

Deletes a birthday record.

---

## 6. Generate Gift Ideas

```http
POST /birthdays/{birthday_id}/gift_ideas
```

Uses Groq AI to generate personalized gift suggestions.

---

# 🤖 AI Gift Recommendation Feature

The application integrates Groq AI to provide personalized gift suggestions.

### Example Input

* Relationship: Friend
* Notes: Likes gaming and technology

### Example Output

* Gaming Mouse
* Wireless Headset
* Steam Gift Card

This feature demonstrates the integration of Generative AI into a real-world application.

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone <repository-url>
```

## Navigate to Project Folder

```bash
cd Birthday_manager_API_Project
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

For security reasons, never upload your actual API key to GitHub.

---

# ▶️ Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Using Swagger UI, users can test all endpoints directly from the browser.

---

# 📸 Project Screenshots

## Swagger API Documentation

(Add screenshot here)

## Add Birthday Endpoint

(Add screenshot here)

---

# 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

* REST API Development
* FastAPI Framework
* Request Validation
* Response Models
* API Documentation
* AI Integration
* Environment Variables
* Software Project Structure

---

# 🔮 Future Enhancements

* Email Birthday Reminders
* SMS Notifications
* WhatsApp Integration
* User Authentication
* Streamlit Frontend Dashboard
* Advanced AI Gift Recommendations

---

# 👨‍💻 Author

**Humna**

FASTAPI + SQLModel + Pydantic + Groq AI Project

---

# 📄 License

This project was developed for educational and learning purposes.


