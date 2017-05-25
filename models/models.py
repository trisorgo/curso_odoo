# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _
from datetime import datetime, timedelta

class SessionCheck(models.Model):
    _inherit= 'openacademy.session'
    reserved_attendee_ids = fields.Many2many(comodel_name='res.partner',
                                             string="Reserved_Attendees",
                                             relation="openacademy_reserved_attendees",
                                             column1="openacademy_sessions_id",
                                             column2="res_partner_id")

    # Restricción a la hora de apuntarse a una sesión de un curso.
    # Si la sesión coincide en fecha con alguna sesión del alumno confirmada,
    # mostrar un aviso bloqueante y preguntar si desea ponerse en reserva
    @api.constrains('attendee_ids')
    def _check_session_confirmed_date(self):
        for session in self.env.user.partner_id.session_ids.search([('state','=','confirmed')]):
            if self.env.user.partner_id in session.attendee_ids:
                if (session.start_date >= self.start_date and session.start_date <= self.end_date) or \
                (session.end_date >= self.start_date and session.end_date <= self.end_date):
                    msg="No puede inscribirse.Está inscrito en una sesión confirmada \
                        para las mismas fechas"
                    action_id=self.env.ref('openacademy_sessions.reserve_session')
                    raise exceptions.RedirectWarning(msg,action_id,
                                    _('Añadir a la lista de reserva de plazas'))


    @api.one
    def subscribe_to_session(self):
        # self.attendee_ids = self.attendee_ids + self.env.user.partner_id
        self._check_session_confirmed_date()
        self.sudo().write({'attendee_ids': [(4, [self.env.user.partner_id.id])]})

    @api.one
    def reserve_session(self):
        import pdb; pdb.set_trace()
        if not self.env.user.partner_id in self.reserved_attendee_ids:
            self.sudo().write({'reserved_attendee_ids': [(4, [self.env.user.partner_id.id])]})
