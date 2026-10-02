# Fix Module Icons (Odoo 14)

Stops app icons on the Apps page from disappearing every time you install or upgrade a module.

**Price:** Free

## The problem

Odoo 14 renders each Apps card from the stored `ir.module.module.icon` field.
On every install/upgrade, Odoo rewrites that field from the `icon` key of the
module manifest. Modules without an `icon` key get their stored icon reset to
empty — broken images rotating through your Apps list.

## The fix

1. `get_values_from_terp`: manifest without `icon` key → stored icon left untouched
2. `update_list`: empty icons get Odoo's standard fallback
3. Installing this module automatically repairs all broken icons
4. Manual repair: Apps → select module(s) → Action → **Regenerate Icon**

## License

LGPL-3
