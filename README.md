SpendSense

A personal expense-tracking web application built with Python and Flask.

Overview

SpendSense helps users record, organize, and monitor their everyday spending through a simple web interface. Users can add expenses, assign categories, view their spending total, and delete entries.

Features

Add expenses with a name, amount, and category
Automatically record the date of each expense
View all recorded expenses in a table
Calculate total spending
Delete individual expenses
Store expense records in a JSON file
Validate expense inputs

Technologies Used

Python – Application logic and data processing
Flask – Web framework and routing
HTML – Webpage structure
CSS – Styling and layout
JSON – Local data storage
Git and GitHub – Version control and project hosting

Project Structure

SpendSenseWeb/
│
├── app.py
├── expenses.json
├── templates/
│   └── index.html
└── static/
    └── style.css

How to Run Locally

Clone this repository:
git clone https://github.com/Tayamika-art/SpendSenseWeb.git

Navigate into the project folder:
cd SpendSenseWeb

Install Flask:
python -m pip install flask

Start the application:
python app.py
Open http://127.0.0.1:5000 in your browser.

Future Improvements

Add spending summaries by category
Introduce monthly spending reports
Add interactive data visualizations
Improve input feedback and error handling

Author

Tayamika
GitHub: @Tayamika-art
