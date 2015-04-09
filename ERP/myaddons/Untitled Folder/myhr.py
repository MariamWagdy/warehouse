from openerp.osv import orm, fields

class myhr_employees(orm.Model):

    gender=[('m','Male'),('f','Female')]
    career=[('n','normal employee'),
            ('m','manager for normal emoployee'),
            ('k','keeper for warehouse'),
            ('mk','manager for warehouse')
    ,('sm','supermanager for all warehouses')
    ,('mc','member  of  committee'),]

    _name = 'myhr.employee'
    _columns = {
        'name':fields.char('Name',size=50,required=True),
        'tel':fields.char('Telephone'),
        'picture':fields.binary('Image'),
        'age':fields.integer('Age',size=3),
        'salary':fields.float('Salary',size=8),
        'gender':fields.selection(gender,'Gender'),
        'career':fields.selection(career,'Career'),


    }









