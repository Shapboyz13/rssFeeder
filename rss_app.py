from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
import sys
import feedparser
import webbrowser
import threading

app = Flask(__name__)

#MYSQL config
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://<UserName>:<Password>@localhost/RSS_python"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

url_data = []

def get_source(feed):
    return {
        'title'     : feed['title'],
        'link'      : feed['link'],
        'published' : feed['published']
    }

def get_feed(db_data):
    rss = db_data.url
    feed = feedparser.parse(rss)
    feed = feed["entries"][0]
    new_feed = get_source(feed)
    new_feed['name']    = db_data.name
    if db_data.title != new_feed.get('title'):
        db_data.title       = new_feed['title']
        db_data.link        = new_feed['link']
        db_data.published   = new_feed['published']
        new_feed['is_read']     = 1
        db.session.commit()
    url_data.append(new_feed)
    return



class rss_model(db.Model):
    __tablename__ = "rss"
    id          = db.Column(db.Integer, primary_key=True)
    url         = db.Column(db.Unicode)
    name        = db.Column(db.Unicode)
    title       = db.Column(db.Unicode)
    link        = db.Column(db.Unicode)
    published   = db.Column(db.Unicode)

    def __init__(self,url,name, is_read=0):
      self.url          = url
      self.name         = name
      self.is_read      = is_read

@app.route('/')
def show_all():
    return render_template('home.html')

@app.route('/article')
def articles():
    global url_data

    url_data = []
    data = rss_model.query.all()
    t = [None] * len(data)
    for i in range(len(data)):
        t[i] = threading.Thread(target=get_feed, args=(data[i],))
        print ("\n\n", "data:",data[i], "\n\n", file=sys.stdout)
        try:
            t[i] = threading.Thread(target=get_feed, args=(data[i],))
            t[i].start()
        except:
           print ("Error: unable to start thread", file=sys.stdout)

    for i in range(len(data)):
        t[i].join()
    return render_template('article.html', chapters = url_data)

@app.route('/add_rss', methods=['GET','POST'])
def add_rss():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        new_rss = rss_model(name = name, url = url)
        db.session.add(new_rss)
        db.session.commit()
        db.session.flush()
        msg="New Manga Added"
        return render_template('home.html',msg=msg)
    return render_template('add_rss.html')

if __name__ == '__main__':
    app.run(debug=True, port=5876)
