DEBUG = True

# Flatpages
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = [".md", ".markdown"]
FLATPAGES_MARKDOWN_EXTENSION =["codehilite", "fenced_code", "tables"]
PAGES_NUMBER_PER_PAGE = 5

# Mail server
MAIL_SERVER = "smtp.server.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = "user@example.net"
MAIL_PASSWORD = "password"

# Protection for Cross-site Request Forgery (CSRF)
CSRF_ENABLED     = True
CSRF_SESSION_KEY = "secretcsrf"

# Secret key for signing cookies
SECRET_KEY = "secret"
