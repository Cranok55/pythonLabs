from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    roots = ''
    a = b = c = ''
    if request.method == 'POST':
        a = request.form.get('a', '')
        b = request.form.get('b', '')
        c = request.form.get('c', '')
        try:
            a_val = float(a)
            b_val = float(b)
            c_val = float(c)
            D = b_val**2 - 4*a_val*c_val
            if a_val == 0:
                roots = "Это не квадратное уравнение (a = 0)."
            elif D > 0:
                root1 = (-b_val + D**0.5) / (2*a_val)
                root2 = (-b_val - D**0.5) / (2*a_val)
                roots = f"Два корня: {root1} и {root2}"
            elif D == 0:
                root = -b_val / (2*a_val)
                roots = f"Один корень: {root}"
            else:
                roots = "Корней нет (дискриминант < 0)"
        except ValueError:
            roots = "Ошибка: введены некорректные данные."
    return render_template('index.html', roots=roots, a=a, b=b, c=c)

if __name__ == '__main__':
    app.run(debug=True)
