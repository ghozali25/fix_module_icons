# -*- coding: utf-8 -*-
{
    'name': 'Fix Module Icons',
    'version': '14.0.2.0.1',
    'summary': 'Prevent app icons from disappearing after module install/upgrade',
    'description': """
Fix Module Icons
================

Prevents module icons on the Apps page from breaking every time you
install or upgrade a module (Odoo 14).

Root cause
----------
Odoo 14 renders each app card with ``<img src="record.icon.value">``,
reading the stored ``ir.module.module.icon`` field. On every install or
upgrade, Odoo rewrites that field from the ``icon`` key of the module
manifest (``get_values_from_terp``). Modules whose manifest has no
``icon`` key get their stored icon reset to ``False``, so the image
breaks -- rotating through your Apps list with each installation.

What this module does
---------------------
1. ``get_values_from_terp``: if the manifest has no ``icon`` key, the
   already-stored icon value is left untouched (no more reset to False).
2. ``update_list``: modules with an empty icon get Odoo's standard
   fallback (``/<module>/static/description/icon.png``, else the base icon).
3. One-click repair, no scripts needed:
   - Installing this module automatically repairs all broken icons.
   - Apps -> select module(s) -> Action -> **Regenerate Icon**.
   - Apps -> Action -> **Fix All Module Icons**.

Your original module icons are preserved -- no placeholders.

Bahasa Indonesia
----------------
Mencegah icon modul di halaman Apps rusak setiap install/upgrade modul.
Setiap install/upgrade, Odoo menulis ulang field ``ir.module.module.icon``
dari key ``icon`` di manifest; modul yang manifest-nya tidak punya key
``icon`` akan tertulis ``False`` sehingga gambarnya rusak bergiliran.
Modul ini memastikan icon yang sudah tersimpan tidak di-reset, dan icon
kosong diisi fallback bawaan Odoo. Icon asli tiap modul tetap dipakai.

Tidak perlu script: saat modul ini di-install, semua icon rusak otomatis
diperbaiki. Tersedia juga aksi sekali-klik "Regenerate Icon" dan
"Fix All Module Icons" di menu Apps.
""",
    'author': 'Ahmad Ghozali',
    'license': 'LGPL-3',
    'depends': ['base'],
    'images': ['static/description/thumbnail.png'],
    'data': [
        'views/ir_module_actions.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
    'auto_install': False,
}
