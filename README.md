## 📘 ISBN Toolkit API

**Name:** Daniel Muuo Muumbi
**Admission Number:** *SCT-254-179/2023*

---

## 📌 Project Description

This project is an API that performs different operations related to ISBN numbers. It was developed as part of a coding exercise to demonstrate understanding of how ISBN validation works .

The main goal of this project is to implement the logic manually and expose it through simple API endpoints.

---

## 🎯 Objectives

The API is able to:

* Compute the check digit of an ISBN-10
* Validate an ISBN-10
* Convert ISBN-10 to ISBN-13
* Validate an ISBN-13

---

## 🧠 Approach 

The solution focuses on implementing the logic step by step.

### ISBN-10 Logic

* Each digit is multiplied by its position (1 to 10)
* The sum is taken and checked using modulus 11
* If the result is 10, it is represented as **'X'**

### ISBN-13 Logic

* Digits are multiplied alternately by 1 and 3
* The total is used to compute the check digit using modulus 10

This approach helped me understand how validation works behind the scenes.

---

## ⚙️ Technologies Used

* Python
* Flask (for API handling)

No external libraries were used for ISBN processing logic.

---

## 🚀 API Endpoints

### 1. Compute ISBN-10 Check Digit

```
POST /isbn10/check-digit
```

**Input:**

```json
{
  "isbn": "030640615"
}
```

---

### 2. Validate ISBN-10

```
POST /isbn10/validate
```

---

### 3. Convert ISBN-10 to ISBN-13

```
POST /isbn10/to-isbn13
```

---

### 4. Validate ISBN-13

```
POST /isbn13/validate
```

---

## 🧪 How to Run the Project

1. Clone the repository:

```
git clone https://github.com/your-username/isbn-toolkit-api.git
```

2. Navigate into the folder:

```
cd isbn-toolkit-api
```

3. Install Flask:

```
pip install flask
```

4. Run the application:

```
python app.py
```

5. Test endpoints using Postman or browser tools.

---

## ⚠️ Error Handling

The API includes basic validation such as:

* Incorrect length
* Non-numeric input
* Invalid ISBN formats

Clear error messages are returned to guide the user.

---

## 💡 Reflection

Working on this project helped me understand ISBN validation more deeply. By first solving the problem manually, I was able to translate each step into code. Writing the logic myself made it easier to see how check digits are calculated and how errors can occur.


