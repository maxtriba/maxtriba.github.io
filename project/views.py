from flask import render_template

from app import app, pages

@app.route('/')
def index():
	posts = [page for page in pages]
	sorted_posts = sorted(posts, reverse=True,
		key=lambda page: page.meta['date'])
	return render_template('base.html', pages=sorted_posts)

@app.route('/<path:path>/')
def page(path):
	posts = [page for page in pages]
	sorted_posts = sorted(posts, reverse=True,
		key=lambda page: page.meta['date'])
	page = pages.get_or_404(path)
	return render_template('page.html', page=page, pages=sorted_posts)