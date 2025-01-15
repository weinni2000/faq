from odoo import http
from odoo.http import request


class Demo(http.Controller):
    @http.route(
        "/minimal_owl",
        type="http",
        auth="public",
        website=True,
    )
    def minimal_owl(self):
        return request.render("minimal_owl.minimal_owl_template", {})
