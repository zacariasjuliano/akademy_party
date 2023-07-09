from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Not, Bool

class Party(metaclass=PoolMeta):
    'Party'
    __name__= 'party.party'
    _rec_name = 'name'

    is_person = fields.Boolean(
        "Pessoa", 
        states={
            'invisible': Bool(Eval('is_institution')), 
            'required': Not(Bool(Eval('is_institution')))
        }, depends=['is_institution'], 
        help="A entidade é uma pessoa.")
    is_institution = fields.Boolean(
        "Instituição", 
        states={
            'invisible':  Bool(Eval('is_person')), 
            'required': Not(Bool(Eval('is_person')))
        }, depends=['is_person'], 
        help="A entidade é uma instituição ou organização.")
    date_birth = fields.Date(
        'Nascimento', 
        states={
            'invisible': Not(Bool(Eval('is_person'))), 
            'required': Bool(Eval('is_person'))            
        }, help="Data de nascimento.")    
    gender = fields.Selection([
            (None, ''),
            ('Masculino', 'Masculino'), ('Femenino', 'Femenino') 
        ], string=u'Genêro',         
        states={
            'invisible': Not(Bool(Eval('is_person'))), 
            'required': Bool(Eval('is_person'))
        })
    marital_status = fields.Selection([
            (None, ''),
            ('Solteiro(a)', 'Solteiro(a)'), ('Casado(a)', 'Casado(a)'),
            ('Divorciado(a)', 'Divorciado(a)'), ('Víuvo(a)', 'Víuvo(a)')
        ], string=u'Estado civil', 
        states={
            'invisible': Not(Bool(Eval('is_person'))), 
            'required': Bool(Eval('is_person'))
        })
    bi_number = fields.Char(
        'B.I nº', size=15,
        states={
            'invisible': Not(Bool(Eval('is_person'))), 
            'required': Bool(Eval('is_person'))
        }, help="Número do bilhete de intidade.")
    father = fields.Many2One(
        'party.party', 'Pai',
        states={
            'invisible': Not(Bool(Eval('is_person')))
        }, help="Nome do pai.")
    mother = fields.Many2One(
        'party.party', 'Mãe',
        states={
            'invisible': Not(Bool(Eval('is_person')))
        }, help="Nome da mãe.")
	
