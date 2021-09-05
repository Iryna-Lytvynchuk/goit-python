import crochet
crochet.setup()

from flask import Flask , render_template, jsonify, request, redirect, url_for
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import time
import os
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from test_spyder.test_spyder.spiders.authors import QuotesSpider

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


output_data = []
crawl_runner = CrawlerRunner()


@app.route('/')
def index():
	return render_template("index.html") 

@app.route('/', methods=['POST'])
def submit():
    if request.method == 'POST':
        s = request.form['url'] 
        global baseURL
        baseURL = s
        
       
        if os.path.exists("<path_to_outputfile.json>"): 
        	os.remove("<path_to_outputfile.json>")

        return redirect(url_for('scrape')) 


@app.route("/scrape")
def scrape():

    scrape_with_crochet(baseURL=baseURL) 
    time.sleep(20) 
    return jsonify(output_data)

@crochet.run_in_reactor
def scrape_with_crochet(baseURL):

    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    
    eventual = crawl_runner.crawl(QuotesSpider, category = baseURL)
    return eventual

def _crawler_result(item, response, spider):
    output_data.append(dict(item))


api = Api(app, version='1.0', title='Sample API',
    description='A sample API',
)

@api.route('/doc/<id>')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    def get(self, id):
        return {}

    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)


if __name__== "__main__":
    app.run(debug=True)