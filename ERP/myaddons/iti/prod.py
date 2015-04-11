from openerp.osv import orm, fields

class prod_catagory(orm.Model):
    _name = 'prod.catagory'
    _columns = {
        'name': fields.char('Name'),
        'cat_id': fields.integer('cat_id', required=True),
        'desc': fields.text('description'),
    }


class prod_subcatagory(orm.Model):
    _name = 'prod.subcatagory'
    _columns = {
        'name': fields.char('Name'),
        'subcat_id': fields.integer('subcat_id', required=True),
        'desc': fields.text('description'),
        'catagory_id': fields.many2one('prod.catagory', string='catagory'),
    }


class prod_subsubcatagory(orm.Model):
    _name = 'prod.subsubcatagory'
    _columns = {
        'name': fields.char('Name'),
        'subsubcat_id': fields.integer('subsubcat_id', required=True),
        'desc': fields.text('description'),
        'subcatagory_id': fields.many2one('prod.subcatagory', string='subcatagory'),
    }
#############
class prod_supplier(orm.Model):
    _name = "prod.supplier"
    _columns = {
        'name': fields.char('Supplier Name', required=True),
        'mail': fields.char('Supplier E_mail'),
        'mobile': fields.char('Supplier Mobile'),
        'address': fields.char('Supplier Address'),
        'products_ids': fields.many2many('prod.product', 'products_suppliers', string='products'),
    }


class prod_product(orm.Model):
    _name = 'prod.product'

    def _calc_code(self, cr, uid, ids, name, arg, context=None):
        result = {}
        ids = self.search(cr, uid, [])

        products = self.browse(cr, uid, ids, context)
        for product in products:
            result[product.id] = str(product.code) + " " + str(product.catagory_id.cat_id) + " " + str(
                product.subcatagory_id.subcat_id) + " " + str(product.subsubcatagory_id.subsubcat_id)

        return result



    def set_accepted(self, cr, uid, ids, context=None):
        pass


    _columns = {
        'name': fields.char('Name'),
        'price': fields.float('Price'),
        'amount': fields.integer('Amount'),
        'productdate': fields.date('Productdate'),
        'expirdate': fields.date('Expirdate'),
        'code': fields.integer('Code', size=2, required=True),
        'net_code': fields.function(_calc_code, string='Reference', method=True, type='char', store=True),
        'desc': fields.text('description'),
        'catagory_id': fields.many2one('prod.catagory', string='catagory'),
        'subcatagory_id': fields.many2one('prod.subcatagory', string='subcatagory'),
        'suppliers_ids': fields.many2many('prod.supplier', string="Suppliers"),
        'subsubcatagory_id': fields.many2one('prod.subsubcatagory', string='subsubcatagory'),
        # 'state': fields.selection(string="State", default='new', selection=[
        #     ('new', 'New'),
        #     ('recieved', 'Recieved'),
        #     ('underReview', 'Under Review'),
        #     ('approved', 'Approved'),
        #     ('keeperConfirm', 'Keeper Confirm'),
        #     ('managerConfirm', 'Manager Confirm'),
        #     ('inStock', 'In Stock'),
        # ], readonly=True),
        # 'stock_id': fields.many2one('prod.stock', string='Stock'),
        # 'is_keeper': fields.function(check_keeper, type='boolean', store=False),
    }