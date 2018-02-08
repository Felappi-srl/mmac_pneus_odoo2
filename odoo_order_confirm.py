#!/usr/bin/python
print("Content-type:text/html\r\n")
# import request
# import sys
import cgi, cgitb

#recuper id ordine
form = cgi.FieldStorage()
ordine = form.getvalue('ordine')

print(ordine[0])

if ordine!=None:

    url= 'http://34.240.79.218:8069'
    db= 'odoo'
    username='procedure@tyreo.com'
    password='Fela1681'

    import xmlrpclib
    common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
    common.version()
    uid = common.authenticate(db, username, password, {})

    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    order_id = models.execute_kw(db, uid, password,'sale.order', 'search',[[['name', '=', ordine]]])
    print(order_id)
    print(models.execute_kw(db, uid, password, 'sale.order', 'action_confirm', order_id))
else:
    print("Parametro ordine non valorizzato")