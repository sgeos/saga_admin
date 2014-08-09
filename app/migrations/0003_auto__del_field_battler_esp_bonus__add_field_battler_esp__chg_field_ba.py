# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Battler.esp_bonus'
        db.delete_column(u'app_battler', 'esp_bonus')

        # Adding field 'Battler.esp'
        db.add_column(u'app_battler', 'esp',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)


        # Changing field 'Battler.skill_type_d'
        db.alter_column(u'app_battler', 'skill_type_d_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.SkillType']))

        # Changing field 'Battler.skill_type_c'
        db.alter_column(u'app_battler', 'skill_type_c_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.SkillType']))

        # Changing field 'Battler.skill_type_b'
        db.alter_column(u'app_battler', 'skill_type_b_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.SkillType']))

        # Changing field 'Battler.skill_type_a'
        db.alter_column(u'app_battler', 'skill_type_a_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.SkillType']))

        # Changing field 'Battler.equipment_slot_b'
        db.alter_column(u'app_battler', 'equipment_slot_b_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.Equipment']))

        # Changing field 'Battler.equipment_slot_c'
        db.alter_column(u'app_battler', 'equipment_slot_c_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.Equipment']))

        # Changing field 'Battler.equipment_slot_a'
        db.alter_column(u'app_battler', 'equipment_slot_a_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.Equipment']))

        # Changing field 'Battler.equipment_slot_d'
        db.alter_column(u'app_battler', 'equipment_slot_d_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.Equipment']))

    def backwards(self, orm):
        # Adding field 'Battler.esp_bonus'
        db.add_column(u'app_battler', 'esp_bonus',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Deleting field 'Battler.esp'
        db.delete_column(u'app_battler', 'esp')


        # Changing field 'Battler.skill_type_d'
        db.alter_column(u'app_battler', 'skill_type_d_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['app.SkillType']))

        # Changing field 'Battler.skill_type_c'
        db.alter_column(u'app_battler', 'skill_type_c_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['app.SkillType']))

        # Changing field 'Battler.skill_type_b'
        db.alter_column(u'app_battler', 'skill_type_b_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['app.SkillType']))

        # Changing field 'Battler.skill_type_a'
        db.alter_column(u'app_battler', 'skill_type_a_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['app.SkillType']))

        # Changing field 'Battler.equipment_slot_b'
        db.alter_column(u'app_battler', 'equipment_slot_b_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['app.Equipment']))

        # Changing field 'Battler.equipment_slot_c'
        db.alter_column(u'app_battler', 'equipment_slot_c_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['app.Equipment']))

        # Changing field 'Battler.equipment_slot_a'
        db.alter_column(u'app_battler', 'equipment_slot_a_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['app.Equipment']))

        # Changing field 'Battler.equipment_slot_d'
        db.alter_column(u'app_battler', 'equipment_slot_d_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['app.Equipment']))

    models = {
        u'app.battler': {
            'Meta': {'object_name': 'Battler'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'education': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'endurance': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'equipment_slot_a': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['app.Equipment']"}),
            'equipment_slot_b': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['app.Equipment']"}),
            'equipment_slot_c': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['app.Equipment']"}),
            'equipment_slot_d': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['app.Equipment']"}),
            'esp': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'female': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hp': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'male': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'mp': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'skill_level_a': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_level_b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_level_c': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_level_d': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_type_a': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['app.SkillType']"}),
            'skill_type_b': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['app.SkillType']"}),
            'skill_type_c': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['app.SkillType']"}),
            'skill_type_d': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['app.SkillType']"}),
            'social_standing': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'sp': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.BattlerType']"}),
            'undead': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'app.battlertype': {
            'Meta': {'object_name': 'BattlerType'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'app.equipment': {
            'Meta': {'object_name': 'Equipment', '_ormbases': [u'app.Item']},
            'air_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attack': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'bash_defense': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'bash_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'blind_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cold_defense': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'cold_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'confusion_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dexterity_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'education_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'endurance_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'esp_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ground_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'heat_defense': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'heat_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hp_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'intelligence_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'liquid_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mental_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'missile_defense': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'missile_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mp_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pierce_defense': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'pierce_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'poison_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pressure_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'shield': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shock_defense': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'shock_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sight_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slash_defense': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'slash_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sleep_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'smell_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'social_standing_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sound_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sp_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status_defense': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'status_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'strength_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stun_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'throw_evade': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'app.item': {
            'Meta': {'object_name': 'Item'},
            'breakage': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.ItemType']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        u'app.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'arm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'armor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'damage_type': ('django.db.models.fields.CharField', [], {'default': "'SL'", 'max_length': '2'}),
            'hands': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'head': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ranged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shield': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skill_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.SkillType']"}),
            'weapon': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'app.skilltype': {
            'Meta': {'object_name': 'SkillType'},
            'attack_stat_type': ('django.db.models.fields.CharField', [], {'default': "'STR'", 'max_length': '3'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'defend_stat_type': ('django.db.models.fields.CharField', [], {'default': "'END'", 'max_length': '3'}),
            'evade_stat_type': ('django.db.models.fields.CharField', [], {'default': "'DEX'", 'max_length': '3'}),
            'hit_stat_type': ('django.db.models.fields.CharField', [], {'default': "'DEX'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['app']