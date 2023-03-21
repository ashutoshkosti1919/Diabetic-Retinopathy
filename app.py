from flask import Flask, render_template ,request,jsonify
from  werkzeug.utils import secure_filename
# from flask_wtf import Flaskforms
# from flask_uploads import UploadSet,IMAGES,configure_uploads,req
import os 
# import sys

UPLOAD_FOLDER='D:\minor 2\static'
ALLOWED_EXTENSIONS = set['pdf','png','jpg']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1).lower() in ALLOWED_EXTENSIONS

# from wtforms import FileField ,SubmitField

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
# app.config['SECRET_KEY']='supersecretkey'
# app.config['UPLOADED_PHOTOS_DEST']='uploads'
# photos=UploadSet('photos',IMAGES)
# configure_uploads(app,photos)


@app.route('/')
def home():
    return render_template('mainindex.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/uploadd')
def uploadd():
    return render_template('upload.html')

@app.route("/upload",methods=["GET","POST"])
def upload_image():
    # if request.methods =="POST":
    if 'file' not in request.files:
       return jsonify({'error ': 'media not provided'}),400
    
    image = request.files['file']
    if image.filename =='':
        print("File name is invalid")
        #    return redirect(request.url)
    if image and allowed_file(image.filename):
        filename=secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return jsonify({'msg':'media uploaded successfully'})


@app.route('/signupindex')
def signupindex():
    return render_template('signupindex.html')

# @app.route('/uploads/<filename>')
# def get_file(filename):
#   return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)

# @app.route('/upload',methods=['GET','POST'])
# def uploadf():
#     form=uploadfile()
#     if form.validate_on_submit:
#       filename=photos.save(form.photo.data)
#       file_url=url_for('get_file',filename=filename)
#     else:
#       file_url=None
#     return render_template('index.html',form=form,file_url=file_url)  
  
    # return render_template('mainindex.html',form=form)


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/serv')
def serv():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True,port=8000)