title: About Flask Blog 
date: 2018-12-12
descr: Flaskblog is a very simple blog made with Flask and Flask-Flatpages
tags: [flask, python, general]
img: 20181212-1.jpeg
imgalt: Screenshot of flaskblog

Flaskblog on GitHub: [github.com/insomnux/flaskblog](https://github.com/insomnux/flaskblog).

Demo on [insomnux.pythonanywhere.com/](http://insomnux.pythonanywhere.com/)

## Features:

Posts are added in `markdown` format in the `pages` directory. Posts must have [YAML metadata](http://www.yaml.org/), followed by a blank line and then the page or post body.

Example:

```
title: My post
date: 2018-12-12
descr: A new awesome post I wrote
tags: [post, new, awesome]
img: cutecat.jpg
imgalt: Photo of my cute cat

# Lorem Ipsum
```

Metadata tags used:

  tag   | used for                                           
--------|--------------------------------------------------------------
 title  | post or page title                                           
 date   | publication date - mandatory for posts                       
 descr  | page or post description                                     
 tags   | tags for the post                                            
 img    | filename of a picture uploaded in `static/pictures`          
 imgalt | alt property for picture (required)                          
 static | `static: True` signifies that an article is a post, not page 

+ Displays post list by post date in `$HOSTNAME/articles/$POSTNAME` - ex: [insomnux.pythonanywhere.com/articles/dolor-sin-amet/](http://insomnux.pythonanywhere.com/articles/dolor-sin-amet/)
+ Static pages (yaml matter: `static: True`) in `$HOSTNAME/$PAGENAME` - ex: [insomnux.pythonanywhere.com/about](http://insomnux.pythonanywhere.com/about/)
+ Tags support
+ Contact form with [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) and [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
+ Code highlighting with [Pygments](http://pygments.org/)

## Credits:

- Tutorials: 
    + [Dead easy yet powerful static website generator with Flask](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)
    + [Using Flask to build static blog builder](http://ju.outofmemory.cn/entry/152919)
    + [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- `paginate.py`: [Using Flask to build static blog builder](http://ju.outofmemory.cn/entry/152919)
- Logo: [pigment/fake-logos](https://github.com/pigment/fake-logos)
- CSS framework: [Milligram - A minimalist CSS framework](https://milligram.io/)
