#!/usr/bin/env python
# coding=utf-8
import web
import model

urls = (
	'/', 'Index',
	'/new', 'New',
	'/view/(\d+)', 'View'
)

t_globals = {
	'datestr': web.datestr
}
render = web.template.render('templates/', base='base', globals=t_globals)

class Index(object):
	def GET(self):
		lists = model.get_lists()
		return render.index(lists)

class View(object):
	def GET(self, id):
		alist = model.get_alist(int(id))
		return render.view(alist)

class New(object):
	form = web.form.Form(
		web.form.Textbox('title', web.form.notnull, size=50, description="List title:"),
		web.form.Textarea('content', web.form.notnull, rows=30, cols=80, description="List content:"),
		web.form.Button('Add list'),
	)

	def GET(self):
		form = self.form()
		return render.new(form)

	def POST(self):
		form = self.form()
		if not form.validates():
			return render.new(form)
		model.new_alist(form.d.title, form.d.content)
		raise web.seeother('/')



app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()