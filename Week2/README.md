# Frontend Fundamentals – Week 2 (Day 1)

## 🎯 Objective

Build a fully structured blog page using **Semantic HTML5 only**  
(No CSS, No JavaScript, No <div> allowed)

The goal was to understand:
- Page structure
- Semantic HTML elements
- Forms & media
- Accessibility basics

---

## 📌 Assignment Requirements

### Learning Outcomes
- Understand page structure
- Master semantic tags and layout scaffolding
- Use forms with validation
- Embed media (video & audio)
- Apply accessibility basics (ARIA, alt, labels)
- Document learnings in README

---

## ✅ What I Built

A fully semantic blog page (`blog.html`) that includes:

- Header with navigation
- Multiple content sections (HTML, CSS, JavaScript)
- Images with captions
- Embedded video & audio
- Accessible subscription form
- Footer section

No `<div>` elements were used.

---

## 🏗 Semantic HTML Structure Used

```html
<header>
<nav>
<main>
<section>
<article>
<figure>
<footer>

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# DAY 2 – CSS Layout Mastery (Flexbox + Grid)

## 📌 Objective

Replicate the provided UI screenshot using modern CSS layout techniques:
- Flexbox
- CSS Grid
- Responsive Design (Mobile-first approach)

The goal was to build a structured layout that visually matches the reference image while using proper semantic HTML and modern layout systems.

---

## 🖼 Reference Layout Structure

The layout includes:

- Header (top full-width section)
- Sidebar (left side vertical section)
- Main Content Area:
  - One large content block (Content-1)
  - Two smaller content blocks (Content-2 & Content-3)
- Footer (bottom full-width section)

---

## ✅ What I Implemented

### 1️⃣ Semantic HTML Structure
Used proper HTML5 semantic elements:

- `<header>`
- `<main>`
- `<aside>`
- `<section>`
- `<footer>`

This improves accessibility and code readability.

-------------------

### 2️⃣ Flexbox Implementation

Used Flexbox for:

- Main layout alignment (Sidebar + Content)
- Centering content inside boxes
- Vertical stacking of content blocks

Key properties used:

```css
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
gap;

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Day 3 – JavaScript ES6 + DOM Manipulation

## 📌 Project: Interactive FAQ Accordion

This project was built as part of Day 3 practice to understand **modern JavaScript (ES6)** and **DOM manipulation without frameworks**.

The task was to build an interactive FAQ accordion where users can click on a question to expand or collapse the answer dynamically.

---

## 🎯 Learning Goals

- Understand ES6 syntax (`const`, arrow functions)
- Practice DOM selection and traversal
- Implement event listeners
- Manipulate classes dynamically using `classList`
- Manage UI state using CSS and JavaScript together

---

## 🚀 Features Implemented

- Multiple FAQ sections
- Answers hidden by default
- Expand/collapse functionality on click
- Dynamic icon toggle (`+` / `-`)
- Clean separation of structure, style, and behavior

---

## 🧱 Technologies Used

- HTML5
- CSS3
- JavaScript (ES6)
- DOM API

No external libraries or frameworks were used.

---

## 🏗️ Implementation Explanation

### 1️⃣ HTML

Each accordion item contains:
- `.item` → Main container
- `.title` → Clickable button
- `.icon` → Displays current state
- `.content` → Hidden answer section

---

### 2️⃣ CSS Logic

```css
.content {
  display: none;
}

.item.active .content {
  display: block;
}



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Here is your copy-paste ready README.md starting with DAY 4 Topic as requested:

📅 DAY 4 – JS Utilities + LocalStorage Mini-Project
🔹 Learning Outcomes

Modular JavaScript functions

LocalStorage persistence

Custom utility functions (debounce, throttle, groupBy)

Debugging using DevTools (breakpoints, watch)

Error handling using try/catch

Logging errors in logs/errors.md

📝 Modular Todo App – Project Description

This project is a Todo Application built using Vanilla JavaScript with a modular architecture.

It demonstrates:

Clean code structure

Separation of concerns

Data persistence using LocalStorage

Reusable utility functions

Error-safe coding practices

The application stores todos in LocalStorage, so data remains saved even after refreshing the page.

📂 Project Structure
day4/
│
├── index.html
├── js/
│   ├── main.js
│   ├── storage.js
│   ├── ui.js
│   ├── utils.js
│
└── logs/
    └── errors.md

⚙️ Features

✅ Add Todo
✅ Delete Todo
✅ Persistent Storage
✅ Debounced Input Handling
✅ Modular Code Structure
✅ Error Handling

🔄 Application Flow
1️⃣ Initial Load

main.js executes

Calls getTodos() from storage.js

Todos fetched from LocalStorage

renderTodos() displays them

2️⃣ Add Todo

User enters text

Clicks Add button

New todo object created

Saved using saveTodos()

UI re-renders

3️⃣ Delete Todo

Delete button clicked

Todo removed from array

Updated array saved to LocalStorage

UI updated

🧠 Key Concepts Used
🔹 Modular JavaScript

Each file has a single responsibility:

main.js → App logic

storage.js → LocalStorage handling

ui.js → DOM rendering

utils.js → Utility functions

This makes the code scalable and maintainable.

🔹 LocalStorage Persistence

Saving data:

localStorage.setItem("todos", JSON.stringify(todos))


Retrieving data:

JSON.parse(localStorage.getItem("todos"))

🔹 Debounce Utility

Used to limit how often a function runs.

Example:

export function debounce(func, delay) {
  let timeout;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), delay);
  };
}

🔹 Error Handling

Used try/catch to prevent crashes:

try {
  const todos = JSON.parse(localStorage.getItem("todos")) || [];
} catch (error) {
  console.error("Error loading todos:", error);
}


Errors can also be logged in:

logs/errors.md

🛠 Debugging

Use Chrome DevTools:

Console tab

Sources → Add breakpoints

Watch variables

Application → Check LocalStorage

🚀 How to Run

Open project folder

Open index.html in browser

OR use Live Server in VS Code.
