# -*- coding: utf-8 -*-
"""Perbaikan permanen bug icon modul Odoo 14.

Akar masalah (odoo/addons/base/models/ir_module.py):
- Halaman Apps me-render <img src="record.icon.value">, yaitu field Char
  'icon' yang TERSIMPAN di database.
- Setiap install/upgrade modul, Odoo memanggil get_values_from_terp() yang
  mengisi 'icon' dari key 'icon' di manifest, atau False kalau tidak ada.
- Akibatnya modul yang manifest-nya tidak mendeklarasikan key 'icon'
  (mayoritas modul) akan tertulis False di DB -> gambar rusak.

Modul ini:
1. Tidak lagi me-reset 'icon' ke False bila manifest tidak punya key 'icon'.
2. Mengisi fallback bawaan Odoo untuk modul yang icon-nya masih kosong.
3. Sekali klik: aksi "Regenerate Icon" / "Fix All Module Icons" di Apps,
   plus perbaikan otomatis saat modul ini di-install (post_init_hook).
"""
from odoo import api, models
from odoo.modules import module as odoo_module


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    def get_values_from_terp(self, terp):
        # Sengaja BUKAN staticmethod: super(Klass, Klass) untuk staticmethod
        # melempar AttributeError di runtime Odoo 14, sedangkan pola
        # super() instance seperti di update_list() terbukti berjalan.
        # Aman karena semua pemanggil di core Odoo memakai instance call:
        # self.get_values_from_terp(terp).
        values = super(IrModuleModule, self).get_values_from_terp(terp)
        if not terp.get('icon'):
            # Manifest tidak mendeklarasikan icon -> jangan sentuh nilai
            # yang sudah tersimpan di database.
            values.pop('icon', None)
        return values

    @api.model
    def update_list(self):
        res = super(IrModuleModule, self).update_list()
        # Modul baru / yang icon-nya masih kosong: pakai logika fallback
        # bawaan Odoo (icon.png modulnya kalau ada, kalau tidak icon base).
        self.action_fix_all_icons()
        return res

    def action_regenerate_icon(self):
        """Tulis ulang icon modul-modul terpilih pakai fallback bawaan Odoo."""
        for mod in self:
            mod.icon = odoo_module.get_module_icon(mod.name)
        return True

    @api.model
    def action_fix_all_icons(self):
        """Perbaiki semua modul yang icon-nya kosong/rusak."""
        empty = self.search([('icon', 'in', (False, ''))])
        for mod in empty:
            mod.icon = odoo_module.get_module_icon(mod.name)
        return True
