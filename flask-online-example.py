#need to think how this could be used - how URL is generated and what the subpage would show and why

from flask import Flask, render_template, abort
 
app = Flask(__name__)
 
PRODUCTS = {
    'location1': {
        'lon': 546,
        'lat': -124,
        'placename': 'ECB',
    },
    'location2': {
        'lon': 549,
        'lat': -126,
        'placename': 'Ellen Terry',
    },
    'location3': {
        'lon': 550,
        'lat': -130,
        'placename': 'The Hub',
    },
    'location4': {
        'lon': 560,
        'lat': -120,
        'placename': 'Frank Herbert Gallery',
    }
}
 
@app.route('/')
@app.route('/home')
def home():
    return render_template('index-flask.html', products=PRODUCTS)
 
@app.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 3000)