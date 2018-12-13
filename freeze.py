from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

'''
For urls that are not linked with url_for
@freezer.register_generator
def static_urls():
    yield "/my-url-1/"
    yield "/my-url-2/"
'''

if __name__ == '__main__':
    freezer.freeze()
