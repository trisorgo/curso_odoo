from openerp import models, fields, api

class WizardReservePlaces(models.TransientModel):
    _name = 'openacademy.wizard_reserve'

    reserved_attendee_ids = fields.Many2many('res.partner', string="Reserved_Attendees")

    @api.one
    def reserve_place(self):
        if not self.env.user.partner_id in self.reserved_attendee_ids:
            self.sudo().write({'reserved_attendee_ids': [(4, [self.env.user.partner_id.id])]})
