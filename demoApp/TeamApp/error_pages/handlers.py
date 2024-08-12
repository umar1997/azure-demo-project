from flask import render_template, Blueprint

error_pages_ = Blueprint('error_pages', __name__)

@error_pages_.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html') , 404
    # error_pages in the render is the folder name in templates

@error_pages_.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html') , 403