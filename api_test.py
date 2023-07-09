import xmlrpc.client

url = 'http://localhost:8069'
db = 'db_test01'
username = 'admin'
password = 'admin'


#  authentication
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})
# print("uid-------->>",uid)

if uid:
    print("authentication success")
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    # for search method
    pratner = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
    print("Search Item---->>", pratner)
    
    pratner_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
    print("Count Item---->>", pratner_count)
    
    # for read method
    pratner_record = models.execute_kw(db, uid, password, 'res.partner', 'read', [pratner], {'fields': ['id', 'name']})
    print('\npratner-Read---->>', pratner_record)


    # search read
    pratner_search_read = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['id', 'name']})
    print('\npratner-Search-Read---->>', pratner_search_read)
    