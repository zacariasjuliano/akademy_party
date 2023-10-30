from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Not, Bool


_GENDER = [
        (None, ''),
        ('masculino', 'Masculino'), ('femenino', 'Femenino'),
        ('nao_binário', 'Não-Binário'), ('genero_fluido', 'Gênero Fluído'),
        ('agenero', 'Agênero'), ('transgenero', 'Transgênero'),
        ('bigenero', 'Bigenero'), ('generoqueer', 'Gêneroqueer'),
        ('two_spirit', 'Two-Spirit'), ('pangenero', 'Pangênero')
    ]

_MARITALSTATUS =  [
        (None, ''),
        ('solteiro(a)', 'Solteiro(a)'), ('casado(a)', 'Casado(a)'),
        ('divorciado(a)', 'Divorciado(a)'), ('viuvo(a)', 'Víuvo(a)'),
        ('separado(a)', 'Separado(a)'), ('uniao_estavel', 'União Estável'),
        ('relacionamento_aberto', 'Relacionamento Aberto'), ('relacao_domestica_registrada', 'Relação Doméstica Registrada'),
        ('casamento_de_fato', 'Casamento de Fato'), ('casamento_civil', 'Casamento Civil'),
        ('casamento_religioso', 'Casamento Religioso')
    ] 


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
        }, help="Data de nascimento.\nEx: dia-mês-ano")    
    gender = fields.Selection(_GENDER, string=u'Gênero',         
        states={
            'invisible': Not(Bool(Eval('is_person'))), 
            'required': Bool(Eval('is_person'))
        })
    marital_status = fields.Selection(_MARITALSTATUS, string=u'Estado civil', 
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
	
