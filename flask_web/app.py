from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Dữ liệu tạm thời để lưu trữ thông tin người dùng (thay thế cho cơ sở dữ liệu)
users = []

# Route trang chủ
@app.route('/')
def home():
    return render_template('home.html')

# Route trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                flash('Đăng nhập thành công!')
                # flash('Xin chào ' + username + '!' + 'website đang trong quá trình phát triển, vui lòng quay lại sau.')
                return redirect(url_for('home'))
        flash('Đăng nhập thất bại. Vui lòng kiểm tra tên người dùng và mật khẩu.')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username:
                flash('Tên người dùng đã tồn tại. Vui lòng chọn tên khác.', 'danger')
                return redirect(url_for('signup'))
        users.append({'username': username, 'password': password})
        flash('Tạo tài khoản thành công! Bạn có thể đăng nhập ngay bây giờ.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
