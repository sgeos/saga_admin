from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import SkillType, ItemType, Item, Equipment, BattlerType, \
                    Battler
import reversion


class SkillTypeAdmin(reversion.VersionAdmin):
    pass


class ItemTypeAdmin(reversion.VersionAdmin):
    pass


class ItemAdmin(reversion.VersionAdmin):
    pass


class EquipmentAdmin(reversion.VersionAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'weight', 'type', 'breakage', 'sticky')
        }),
        ('Weapon', {
            'classes': ('collapse',),
            'fields': ('attack',)
        }),
        ('Armor', {
            'classes': ('collapse',),
            'fields': ('shield',)
        }),
        ('Armor Defense', {
            'classes': ('collapse',),
            'fields': ('slash_defense', 'bash_defense', 'pierce_defense', 'missile_defense',
                       'heat_defense', 'cold_defense', 'shock_defense', 'status_defense')
        }),
        ('Armor Evasion', {
            'classes': ('collapse',),
            'fields': ('slash_evade', 'bash_evade', 'pierce_evade', 'missile_evade', 
            'heat_evade', 'cold_evade', 'shock_evade', 'status_evade')
        }),
        ('Special Evasion', {
            'classes': ('collapse',),
            'fields': ('sight_evade', 'sound_evade', 'smell_evade', 'air_evade', 
                       'liquid_evade', 'ground_evade', 'throw_evade')
        }),
        ('Status Effect Evasion', {
            'classes': ('collapse',),
            'fields': ('poison_evade', 'blind_evade', 'confusion_evade', 'mental_evade', 
                       'sleep_evade', 'stun_evade', 'pressure_evade', 'death_evade')
        }),
        ('Stat Bonus', {
            'classes': ('collapse',),
            'fields': ('hp_bonus', 'mp_bonus', 'sp_bonus', 
                       'strength_bonus', 'dexterity_bonus', 'endurance_bonus', 'intelligence_bonus', 
                       'education_bonus', 'social_standing_bonus', 'esp_bonus')
        }),
    )



class BattlerTypeAdmin(reversion.VersionAdmin):
    pass


class BattlerAdmin(reversion.VersionAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'male', 'female', 'undead')
        }),
        ('Points', {
            'classes': ('collapse',),
            'fields': ('hp', 'mp', 'sp')
        }),
        ('Stats', {
            'classes': ('collapse',),
            'fields': ('strength', 'dexterity', 'endurance', 'intelligence', 'education', 'social_standing', 'esp')
        }),
        ('Skills', {
            'classes': ('collapse',),
            'fields': ('skill_type_a', 'skill_level_a', 'skill_type_b', 'skill_level_b',
                       'skill_type_c', 'skill_level_c', 'skill_type_d', 'skill_level_d')
        }),
        ('Equipment', {
            'classes': ('collapse',),
            'fields': ('equipment_slot_a', 'equipment_slot_b', 'equipment_slot_c', 'equipment_slot_d')
        }),
    )


admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(BattlerType, BattlerTypeAdmin)
admin.site.register(Battler, BattlerAdmin)

