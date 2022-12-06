from odoo import fields, models, _
 
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"

    name = fields.Char('name',required=True)
    description = fields.Text('description')
    postcode = fields.Char('postcode')
    date_availability = fields.Date('date_availability')
    expected_price = fields.Float('expected_price',required=True)
    selling_price = fields.Float('selling_price') 
    bedrooms = fields.Integer('bedrooms')
    living_area = fields.Integer('living_area')
    facades = fields.Integer('facades')             
    garage = fields.Boolean('garage') 
    garden = fields.Boolean('garden') 
    garden_area = fields.Integer('garden_area')                                        
    garden_orientation = fields.Selection(
        string='garden_orientation',  
        selection=[('north','north'), ('south','South'), ('east','East'), ('west','West')])