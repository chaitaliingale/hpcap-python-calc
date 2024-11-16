from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Chaitali Ingale" 
    pnr = "240840141007" 
    # List of students
    std_names = ['Chaitali', 'Apurva', 'Shraddha', 'Khushi']
    
    # Print std_names using a for loop in Python
    print("std_names:")
    for std in std_names:
        print(std)
    return render_template('index.html', name=name, pnr=pnr)

print "This is used for git"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
