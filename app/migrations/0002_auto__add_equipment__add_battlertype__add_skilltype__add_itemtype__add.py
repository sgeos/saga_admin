# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Equipment'
        db.create_table(u'app_equipment', (
            (u'item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.Item'], unique=True, primary_key=True)),
            ('sticky', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('attack', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('shield', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slash_defense', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('bash_defense', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('pierce_defense', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('missile_defense', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('heat_defense', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('cold_defense', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('shock_defense', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('status_defense', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('slash_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bash_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pierce_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('missile_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('heat_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cold_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('shock_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sight_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sound_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('smell_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('air_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('liquid_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ground_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('throw_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('poison_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('blind_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('confusion_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mental_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sleep_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('stun_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pressure_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('death_evade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hp_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mp_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sp_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('strength_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dexterity_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('endurance_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intelligence_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('education_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('social_standing_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('esp_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'app', ['Equipment'])

        # Adding model 'BattlerType'
        db.create_table(u'app_battlertype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'app', ['BattlerType'])

        # Adding model 'SkillType'
        db.create_table(u'app_skilltype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('attack_stat_type', self.gf('django.db.models.fields.CharField')(default='STR', max_length=3)),
            ('hit_stat_type', self.gf('django.db.models.fields.CharField')(default='STR', max_length=3)),
            ('defend_stat_type', self.gf('django.db.models.fields.CharField')(default='STR', max_length=3)),
            ('evade_stat_type', self.gf('django.db.models.fields.CharField')(default='STR', max_length=3)),
        ))
        db.send_create_signal(u'app', ['SkillType'])

        # Adding model 'ItemType'
        db.create_table(u'app_itemtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('skill_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.SkillType'])),
            ('weapon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('shield', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hands', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('damage_type', self.gf('django.db.models.fields.CharField')(default='SL', max_length=2)),
            ('ranged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('head', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('armor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('body', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('arm', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('leg', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['ItemType'])

        # Adding model 'Item'
        db.create_table(u'app_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.ItemType'])),
            ('breakage', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal(u'app', ['Item'])

        # Adding model 'Battler'
        db.create_table(u'app_battler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.BattlerType'])),
            ('male', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('female', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('undead', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hp', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('mp', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('sp', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('strength', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('dexterity', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('endurance', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('intelligence', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('education', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('social_standing', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('esp_bonus', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('skill_type_a', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['app.SkillType'])),
            ('skill_level_a', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('skill_type_b', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['app.SkillType'])),
            ('skill_level_b', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('skill_type_c', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['app.SkillType'])),
            ('skill_level_c', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('skill_type_d', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['app.SkillType'])),
            ('skill_level_d', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('equipment_slot_a', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['app.Equipment'])),
            ('equipment_slot_b', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['app.Equipment'])),
            ('equipment_slot_c', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['app.Equipment'])),
            ('equipment_slot_d', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['app.Equipment'])),
        ))
        db.send_create_signal(u'app', ['Battler'])


    def backwards(self, orm):
        # Deleting model 'Equipment'
        db.delete_table(u'app_equipment')

        # Deleting model 'BattlerType'
        db.delete_table(u'app_battlertype')

        # Deleting model 'SkillType'
        db.delete_table(u'app_skilltype')

        # Deleting model 'ItemType'
        db.delete_table(u'app_itemtype')

        # Deleting model 'Item'
        db.delete_table(u'app_item')

        # Deleting model 'Battler'
        db.delete_table(u'app_battler')


    models = {
        u'app.battler': {
            'Meta': {'object_name': 'Battler'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'education': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'endurance': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'equipment_slot_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['app.Equipment']"}),
            'equipment_slot_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['app.Equipment']"}),
            'equipment_slot_c': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['app.Equipment']"}),
            'equipment_slot_d': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['app.Equipment']"}),
            'esp_bonus': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
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
            'skill_type_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['app.SkillType']"}),
            'skill_type_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['app.SkillType']"}),
            'skill_type_c': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['app.SkillType']"}),
            'skill_type_d': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['app.SkillType']"}),
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
            'defend_stat_type': ('django.db.models.fields.CharField', [], {'default': "'STR'", 'max_length': '3'}),
            'evade_stat_type': ('django.db.models.fields.CharField', [], {'default': "'STR'", 'max_length': '3'}),
            'hit_stat_type': ('django.db.models.fields.CharField', [], {'default': "'STR'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['app']