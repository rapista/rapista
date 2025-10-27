from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# --- Home Route ---
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Flask API Home</title>
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #74ABE2, #5563DE);
                    color: white;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    font-size: 2.5em;
                    margin-bottom: 20px;
                }
                a {
                    text-decoration: none;
                    background-color: #fff;
                    color: #5563DE;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-weight: bold;
                }
                a:hover {
                    background-color: #f1f1f1;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to my Flask API!</h1>
            <a href="/student">View Student Info</a>
            <br><br>
            <a href="/register">Register Here</a>
        </body>
    </html>
    """

# --- JSON API Route ---
@app.route('/student')
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

# --- Registration Form ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        grade = request.form.get('grade')
        section = request.form.get('section')
        return f"""
        <html>
            <head>
                <title>Registration Success</title>
                <style>
                    body {{
                        font-family: 'Poppins', sans-serif;
                        background: #F7F9FC;
                        color: #333;
                        text-align: center;
                        padding-top: 100px;
                    }}
                    .card {{
                        background: white;
                        border-radius: 10px;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                        width: 400px;
                        margin: auto;
                        padding: 30px;
                    }}
                    h2 {{ color: #5563DE; }}
                    a {{
                        display: inline-block;
                        margin-top: 20px;
                        text-decoration: none;
                        background: #5563DE;
                        color: white;
                        padding: 10px 20px;
                        border-radius: 5px;
                    }}
                    a:hover {{ background: #3746a1; }}
                </style>
            </head>
            <body>
                <div class="card">
                    <h2>Registration Successful!</h2>
                    <p><b>Name:</b> {name}</p>
                    <p><b>Grade:</b> {grade}</p>
                    <p><b>Section:</b> {section}</p>
                    <a href="/">Go Back Home</a>
                </div>
            </body>
        </html>
        """
    return render_template_string("""
    <html>
        <head>
            <title>Student Registration</title>
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #5563DE, #74ABE2);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .register-box {
                    background-color: white;
                    border-radius: 15px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                    width: 400px;
                    padding: 30px;
                    text-align: center;
                }
                h2 {
                    color: #5563DE;
                    margin-bottom: 20px;
                }
                input[type="text"], input[type="number"] {
                    width: 80%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                button {
                    background-color: #5563DE;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 1em;
                }
                button:hover {
                    background-color: #3746a1;
                }
                a {
                    display: block;
                    margin-top: 15px;
                    color: #5563DE;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <div class="register-box">
                <h2>Student Registration</h2>
                <form method="POST">
                    <input type="text" name="name" placeholder="Enter your name" required><br>
                    <input type="number" name="grade" placeholder="Enter your grade" required><br>
                    <input type="text" name="section" placeholder="Enter your section" required><br>
                    <button type="submit">Register</button>
                </form>
                <a href="/">Back to Home</a>
            </div>
        </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
