# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from datetime import datetime, timedelta

class SessionCheck(models.Model):
    _inherit= 'openacademy.session'
    reserved_attendee_ids = fields.Many2many('res.partner', string="Reserved_Attendees")

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
                    action_id=self.env.ref('openacademy_sessions.reserve_session_wizard')
                    raise exceptions.RedirectWarning(msg,action_id,
                                    ('Añadir a la lista de reserva de plazas'))


    @api.one
    def subscribe_to_session(self):
        # self.attendee_ids = self.attendee_ids + self.env.user.partner_id
        self._check_session_confirmed_date()
        self.sudo().write({'attendee_ids': [(4, [self.env.user.partner_id.id])]})
