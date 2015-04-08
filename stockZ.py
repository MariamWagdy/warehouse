# __author__ = 'zainab'
from openerp.osv import fields,orm


class stock_stock(orm.Model):
    _name = "stock.stock"
    _description = "stock"
    _columns = {
        'stockName': fields.char('Stock Name',size=128,required=True,select=True),
        # 'product': fields.many2one('Product#class', required=True),
        'quantity': fields.char('quantity', required=True),
        'notes':fields.text('Notes', required=True),

    }
