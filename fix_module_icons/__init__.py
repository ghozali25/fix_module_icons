# -*- coding: utf-8 -*-
from . import models
from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    """Otomatis perbaiki semua icon yang rusak saat modul di-install."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.module.module'].action_fix_all_icons()
