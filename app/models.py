from django.db import models
from django_extensions.db.models import AutoSlugField

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
# Create your models here.


class SkillType(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=64)

    STRENGTH = "STR"
    DEXTERITY = "DEX"
    ENDURANCE = "END"
    INTELLIGENCE = "INT"
    EDUCATION = "EDU"
    SOCIAL_STANDING = "SOC"
    ESP = "ESP"
    STAT_TYPE_CHOICES = {
        #(None, "Please select a stat."),
        (STRENGTH, "Strength"),
        (DEXTERITY, "Dexterity"),
        (ENDURANCE, "Endurance"),
        (INTELLIGENCE, "Intelligence"),
        (EDUCATION, "Education"),
        (SOCIAL_STANDING, "Socail Standing"),
        (ESP, "ESP"),
    }
    attack_stat_type = models.CharField(_("Attack Stat Type"), max_length=3, choices=STAT_TYPE_CHOICES, default=STRENGTH)
    hit_stat_type = models.CharField(_("Hit Stat Type"), max_length=3, choices=STAT_TYPE_CHOICES, default=DEXTERITY)
    defend_stat_type = models.CharField(_("Defend Stat Type"), max_length=3, choices=STAT_TYPE_CHOICES, default=ENDURANCE)
    evade_stat_type = models.CharField(_("Evade Stat Type"), max_length=3, choices=STAT_TYPE_CHOICES, default=DEXTERITY)

    def __unicode__(self):
        return self.name

    class Meta:
        pass


class ItemType(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=64)
    skill_type = models.ForeignKey(SkillType)

    # Weapon Flags
    weapon = models.BooleanField(_("Weapon Slot"), default=False)
    shield = models.BooleanField(_("Shield Slot"), default=False)
    hands = models.IntegerField(_("Hands Required"), default=0)
    RECOVERY = "RE"
    SLASH = "SL"
    BASH = "BA"
    PIERCE = "PI"
    MISSILE = "MI"
    HEAT = "HE"
    COLD = "CO"
    SHOCK = "SH"
    STATUS = "ST"
    DAMAGE_TYPE_CHOICES = {
        #(None, "Please select a damage type."),
        (SLASH, "Slash"),
        (BASH, "Bash"),
        (PIERCE, "Pierce"),
        (MISSILE, "Missile"),
        (HEAT, "Heat"),
        (COLD, "Cold"),
        (SHOCK, "Shock"),
        (STATUS, "Status"),
        (RECOVERY, "Recovery"),
    }
    damage_type = models.CharField(_("Damage Type"), max_length=2, choices=DAMAGE_TYPE_CHOICES, default=SLASH)
    ranged = models.BooleanField(_("Ranged Damage"), default=False)

    # Armor Flags
    head = models.BooleanField(_("Head Slot"), default=False)
    armor = models.BooleanField(_("Armor Slot"), default=False)
    body = models.BooleanField(_("Body Slot"), default=False)
    arm = models.BooleanField(_("Arm Slot"), default=False)
    leg = models.BooleanField(_("Leg Slot"), default=False)

    def __unicode__(self):
        return self.name
    

class Item(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=64)
    price = models.IntegerField(_("Price"), default=100)
    weight = models.IntegerField(_("Weight"), default=100)
    type = models.ForeignKey(ItemType)
    breakage = models.IntegerField(_("Breakage"), default=100)
    # Field Effect, Battle Effect, Battle Skill A, Battle Skill B

    def __unicode__(self):
        return self.name


class Equipment(Item):
    sticky = models.BooleanField(_("Sticky"), default=False)

    # Weapon
    attack = models.IntegerField(_("Attack"), default=100)

    # Armor, only applies when blocking if shield
    shield = models.BooleanField(_("Shield"), default=False)

    # Armor Defense
    slash_defense = models.IntegerField(_("Slash Defense"), default=100)
    bash_defense = models.IntegerField(_("Bash Defense"), default=100)
    pierce_defense = models.IntegerField(_("Pierce Defense"), default=100)
    missile_defense = models.IntegerField(_("Missile Defense"), default=100)
    heat_defense = models.IntegerField(_("Heat Defense"), default=100)
    cold_defense = models.IntegerField(_("Cold Defense"), default=100)
    shock_defense = models.IntegerField(_("Shock Defense"), default=100)
    status_defense = models.IntegerField(_("Status Defense"), default=100)

    # Armor Evasion
    slash_evade = models.IntegerField(_("Slash Evade"), default=0)
    bash_evade = models.IntegerField(_("Bash Evade"), default=0)
    pierce_evade = models.IntegerField(_("Pierce Evade"), default=0)
    missile_evade = models.IntegerField(_("Missile Evade"), default=0)
    heat_evade = models.IntegerField(_("Heat Evade"), default=0)
    cold_evade = models.IntegerField(_("Cold Evade"), default=0)
    shock_evade = models.IntegerField(_("Shock Evade"), default=0)
    status_evade = models.IntegerField(_("Status Evade"), default=0)

    # Special Evasion
    sight_evade = models.IntegerField(_("Sight Evade"), default=0)
    sound_evade = models.IntegerField(_("Sound Evade"), default=0)
    smell_evade = models.IntegerField(_("Smell Evade"), default=0)
    air_evade = models.IntegerField(_("Air Evade"), default=0)
    liquid_evade = models.IntegerField(_("Liquid Evade"), default=0)
    ground_evade = models.IntegerField(_("Ground Evade"), default=0)
    throw_evade = models.IntegerField(_("Throw Evade"), default=0)

    # Status Effect Evasion
    poison_evade = models.IntegerField(_("Poison Evade"), default=0)
    blind_evade = models.IntegerField(_("Blind Evade"), default=0)
    confusion_evade = models.IntegerField(_("Confusion Evade"), default=0)
    mental_evade = models.IntegerField(_("Mental Evade"), default=0)
    sleep_evade = models.IntegerField(_("Sleep Evade"), default=0)
    stun_evade = models.IntegerField(_("Stun Evade"), default=0)
    pressure_evade = models.IntegerField(_("Pressure Evade"), default=0)
    death_evade = models.IntegerField(_("Death Evade"), default=0)

    # Stat Bonus
    hp_bonus = models.IntegerField(_("Hit Point Bonus"), default=0)
    mp_bonus = models.IntegerField(_("Magic Point Bonus"), default=0)
    sp_bonus = models.IntegerField(_("Skill Point Bonus"), default=0)
    strength_bonus = models.IntegerField(_("Strength Bonus"), default=0)
    dexterity_bonus = models.IntegerField(_("Dexterity Bonus"), default=0)
    endurance_bonus = models.IntegerField(_("Endurance Bonus"), default=0)
    intelligence_bonus = models.IntegerField(_("Intelligence Bonus"), default=0)
    education_bonus = models.IntegerField(_("Education Bonus"), default=0)
    social_standing_bonus = models.IntegerField(_("Socal Standing Bonus"), default=0)
    esp_bonus = models.IntegerField(_("ESP Bonus"), default=0)


class BattlerType(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=64)

    def __unicode__(self):
        return self.name

 
class Battler(TimeStampedModel):
    name = models.CharField(max_length=64)

    type = models.ForeignKey(BattlerType)
    male = models.BooleanField(_("Male"), default=False)
    female = models.BooleanField(_("Female"), default=False)
    undead = models.BooleanField(_("Undead"), default=False)

    # Points
    hp = models.IntegerField(_("Hit Points"), default=100)
    mp = models.IntegerField(_("Magic Points"), default=100)
    sp = models.IntegerField(_("Skill Points"), default=100)

    # Stats
    strength = models.IntegerField(_("Strength"), default=100)
    dexterity = models.IntegerField(_("Dexterity"), default=100)
    endurance = models.IntegerField(_("Endurance"), default=100)
    intelligence = models.IntegerField(_("Intelligence"), default=100)
    education = models.IntegerField(_("Education"), default=100)
    social_standing = models.IntegerField(_("Socal Standing"), default=100)
    esp = models.IntegerField(_("ESP"), default=100)

    # Skills
    skill_type_a = models.ForeignKey(SkillType, related_name='+', blank=True, null=True, default=None)
    skill_level_a = models.IntegerField(_("Skill Level A"), default=0)
    skill_type_b = models.ForeignKey(SkillType, related_name='+', blank=True, null=True, default=None)
    skill_level_b = models.IntegerField(_("Skill Level B"), default=0)
    skill_type_c = models.ForeignKey(SkillType, related_name='+', blank=True, null=True, default=None)
    skill_level_c = models.IntegerField(_("Skill Level C"), default=0)
    skill_type_d = models.ForeignKey(SkillType, related_name='+', blank=True, null=True, default=None)
    skill_level_d = models.IntegerField(_("Skill Level D"), default=0)

    # Equipment
    equipment_slot_a = models.ForeignKey(Equipment, related_name='+', blank=True, null=True, default=None)
    equipment_slot_b = models.ForeignKey(Equipment, related_name='+', blank=True, null=True, default=None)
    equipment_slot_c = models.ForeignKey(Equipment, related_name='+', blank=True, null=True, default=None)
    equipment_slot_d = models.ForeignKey(Equipment, related_name='+', blank=True, null=True, default=None)

    # Calculated Attack
    # Calculated Defense

    def __unicode__(self):
        return self.name

