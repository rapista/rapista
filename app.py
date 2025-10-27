from flask import Flask, jsonify, request, render_template_string, redirect, url_for

app = Flask(__name__)

# In-memory list to store registered students
students = []

# --- Home Route ---
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Flask API Home</title>
            <style>
                body {
                    margin: 0;
                    font-family: 'Poppins', sans-serif;
                    height: 100vh;
                    overflow: hidden;
                    color: white;
                    text-align: center;
                }
                video {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    z-index: -1;
                }
                .content {
                    position: relative;
                    top: 35%;
                }
                h1 {
                    font-size: 2.5em;
                    margin-bottom: 20px;
                    text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
                }
                a {
                    text-decoration: none;
                    background-color: #ffffff;
                    color: #1e8449;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-weight: bold;
                    transition: 0.3s;
                }
                a:hover {
                    background-color: #e8f6f3;
                }
            </style>
        </head>
        <body>
            <video autoplay loop muted>
                <source src="https://cdn.pixabay.com/video/2021/10/25/95268-636567421_large.mp4" type="video/mp4">
            </video>
            <div class="content">
                <h1>Welcome to My Flask API 🌿</h1>
                <a href="/student">View Student Info</a>
                <br><br>
                <a href="/register">Register Here</a>
            </div>
        </body>
    </html>
    """

# --- Student List Route ---
@app.route('/student')
def get_student():
    if not students:
        return """
        <html>
            <head>
                <title>No Students Found</title>
                <style>
                    body {
                        font-family: 'Poppins', sans-serif;
                        background: linear-gradient(135deg, #00b894, #0984e3);
                        color: white;
                        text-align: center;
                        padding-top: 150px;
                    }
                    a {
                        text-decoration: none;
                        background-color: #fff;
                        color: #00b894;
                        padding: 10px 20px;
                        border-radius: 5px;
                    }
                    a:hover {
                        background-color: #dfe6e9;
                    }
                </style>
            </head>
            <body>
                <h2>No students have registered yet 😢</h2>
                <a href="/register">Register a Student</a>
            </body>
        </html>
        """
    
    student_list = ""
    for s in students:
        student_list += f"""
            <div class="card">
                <p><b>Name:</b> {s['name']}</p>
                <p><b>Grade:</b> {s['grade']}</p>
                <p><b>Section:</b> {s['section']}</p>
            </div>
        """

    return f"""
    <html>
        <head>
            <title>Registered Students</title>
            <style>
                body {{
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #00b894, #0984e3);
                    color: white;
                    text-align: center;
                    padding: 40px;
                }}
                h2 {{
                    margin-bottom: 20px;
                }}
                .card {{
                    background: white;
                    color: #333;
                    border-radius: 10px;
                    width: 320px;
                    margin: 20px auto;
                    padding: 20px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                    border-top: 5px solid #00b894;
                }}
                a {{
                    text-decoration: none;
                    background-color: #fff;
                    color: #00b894;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-weight: bold;
                }}
                a:hover {{
                    background-color: #dfe6e9;
                }}
            </style>
        </head>
        <body>
            <h2>🌱 Registered Students</h2>
            {student_list}
            <br><br>
            <a href="/">Go Back Home</a>
        </body>
    </html>
    """

# --- Registration Form ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        grade = request.form.get('grade')
        section = request.form.get('section')

        students.append({
            "name": name,
            "grade": grade,
            "section": section
        })

        return redirect(url_for('get_student'))

    return render_template_string("""
    <html>
        <head>
            <title>Student Registration</title>
            <style>
                body {
                    margin: 0;
                    font-family: 'Poppins', sans-serif;
                    overflow: hidden;
                    color: white;
                }
                video {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    z-index: -1;
                }
                .register-box {
                    background-color: rgba(255, 255, 255, 0.95);
                    border-radius: 15px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                    width: 400px;
                    padding: 30px;
                    text-align: center;
                    margin: 100px auto;
                    color: #333;
                    border-top: 6px solid #00b894;
                }
                h2 {
                    color: #0984e3;
                    margin-bottom: 20px;
                }
                input[type="text"], input[type="number"] {
                    width: 80%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    font-size: 1em;
                }
                button {
                    background: linear-gradient(135deg, #00b894, #0984e3);
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 1em;
                    transition: 0.3s;
                }
                button:hover {
                    background: linear-gradient(135deg, #0984e3, #00b894);
                }
                a {
                    display: block;
                    margin-top: 15px;
                    color: #0984e3;
                    text-decoration: none;
                    font-weight: bold;
                }
                a:hover {
                    color: #00b894;
                }
            </style>
        </head>
        <body>
            <video autoplay loop muted>
                <source src="https://cdn.pixabay.com/video/2024/03/02/204983-917464946_large.mp4" type="video/mp4">
            </video>
            <div class="register-box">
                <h2>Student Registration 🌿</h2>
                <form method="POST">
                    <input type="text" name="name" placeholder="Enter your name" required><br>
                    <input type="number" name="grade" placeholder="Enter your grade" required><br>
                    <input type="text" name="section" placeholder="Enter your section" required><br>
                    <button type="submit">Register</button>
                </form>
                <a href="/">← Back to Home</a>
            </div>
        </body>
    </html>
    """)

# --- Run Server ---
if __name__ == '__main__':
    app.run(debug=True)
