from flask import Flask, redirect
app = Flask(__name__)

@app.route('/about-me')
def index():
    aboutme = """ <p><strong>About me</strong></p>
<p><em>Name</em> : Acay Nguyen<br /> <em>Work</em> : Galileo Vietnam<br /> <em>University</em> : NEU</p>
<p></p>
<p><img src="http://www.cayxanhhoalac.com.vn/wp-content/uploads/2014/07/xuongrong.jpg" alt="" width="209" height="158" /></p> """
    return aboutme

@app.route('/school')
def school():
    return redirect("http://techkids.vn")


if __name__ == '__main__':
  app.run(debug=True)
