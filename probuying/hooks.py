# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "probuying"
app_title = "ProBuying"
app_publisher = "Aisha"
app_description = "Buying purpose"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "aisha@gmail.com"
app_license = "MIT"




fixtures = ["Custom Field","Print Format",
	{"dt": "Custom Field",
		"filters": [
			[
	"name", "in", ["Sales Order-authorised_sign",
	"Sales Order-company_seal_",
	"Sales Order-so_approved_by", 
	"Purchase Order-po__approved_date",
	"Sales Order-company_seal_", 
	"Purchase Order-po__approved_date",
        "Sales Order-so_approved_date"
				]
			]
]},
	{"dt": "Print Format", 
	"filters": [
	[
	"name","in", ["Mareeb Sales Order"]
	]
	]}

	]










# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/probuying/css/probuying.css"
# app_include_js = "/assets/probuying/js/probuying.js"

# include js, css files in header of web template
# web_include_css = "/assets/probuying/css/probuying.css"
# web_include_js = "/assets/probuying/js/probuying.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "probuying.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "probuying.install.before_install"
# after_install = "probuying.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "probuying.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"probuying.tasks.all"
# 	],
# 	"daily": [
# 		"probuying.tasks.daily"
# 	],
# 	"hourly": [
# 		"probuying.tasks.hourly"
# 	],
# 	"weekly": [
# 		"probuying.tasks.weekly"
# 	]
# 	"monthly": [
# 		"probuying.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "probuying.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "probuying.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "probuying.task.get_dashboard_data"
# }

