from trytond.pool import Pool
from . import party

def register():
	Pool.register(
		party.Party,
		
		module='akademy_party', type_='model'
	)

