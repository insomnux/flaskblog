import pygments, markdown
from flask import Flask, flash, redirect, render_template, render_template_string, request, url_for
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from flask_mail import Mail, Message
from models.paginate import Paginate as Paginate
from models.forms import ContactForm as ContactForm

def my_markdown(text):
    markdown_text = render_template_string(text)
    pygmented_text = markdown.markdown(markdown_text, extensions=["codehilite", "fenced_code"])
    return pygmented_text

app = Flask(__name__)
#app.config.from_object("config")
app.config.from_object("config_public")
app.config["FLATPAGES_HTML_RENDERER"] = my_markdown
pages = FlatPages(app)
mail = Mail(app)


# 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs("monokai"), 200, {"Content-Type":"text/css"}

@app.route("/")
def index(num = 0):
    posts = [p for p in pages if "date" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page: page.meta["date"])
    ppaginate=Paginate(app.config["PAGES_NUMBER_PER_PAGE"],sorted_pages)
    if (num >= ppaginate.get_total_number()):
        return redirect(url_for("index_extend"))

    return render_template("index.html",num=num,pages=ppaginate.get_number_pages(num),config=app.config,current_number=num,total_num=ppaginate.get_total_number()- 1)

@app.route("/index/<string:num>.html")
def index_extend(num):
    num=int(num)
    posts = [p for p in pages if "date" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page: page.meta["date"])
    ppaginate=Paginate(app.config["PAGES_NUMBER_PER_PAGE"],sorted_pages)
    if (num >= ppaginate.get_total_number()):
        num = 0

    return render_template("index.html",num=num,pages=ppaginate.get_number_pages(num),config=app.config,current_number=num,total_num=ppaginate.get_total_number()- 1)

@app.route("/<path:path>/")
def staticpage(path):
    p = pages.get_or_404(path)
    staticpage = p if "static" in p.meta else None
    if page == None:
        return page_not_found(404)

    return render_template("page.html", page=staticpage)

@app.route("/articles/<path:path>/")
def page(path):
    p = pages.get_or_404(path)
    page = p if "date" in p.meta else None
    if page == None:
        return page_not_found(404)
    return render_template("post.html", page=page)

@app.route("/tag/<string:tag>/")
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get("tags", [])]
    return render_template("tags.html", pages=tagged, tag=tag)

@app.route("/contact", methods=("GET", "POST"))
def contact():
    form = ContactForm()
    error = None
    
    if request.method == "POST":
        if form.validate() == False:
            error = "Please fill in all fields"
        else:
            msg = Message(
                    "Message from " + form.name.data + "," + form.email.data,
                    sender="mail@example.net",
                    recipients=["mail@example.net"])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            flash("Message sent.")
            return redirect( url_for("contact") )
        
    return render_template("contact.html", form=form, error=error)

if __name__ == "__main__":
    app.run()
