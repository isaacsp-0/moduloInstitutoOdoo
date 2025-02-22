# -*- coding: utf-8 -*-
# from odoo import http


# class Instituto(http.Controller):
#     @http.route('/instituto/instituto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/instituto/instituto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('instituto.listing', {
#             'root': '/instituto/instituto',
#             'objects': http.request.env['instituto.instituto'].search([]),
#         })

#     @http.route('/instituto/instituto/objects/<model("instituto.instituto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('instituto.object', {
#             'object': obj
#         })
