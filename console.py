import pdb
from models.merchant import Merchant

import repositories.merchant_repository as mer_rep




mer1 = Merchant('Amazon')
mer_rep.save(mer1)

mer2 = Merchant('EvilCorp')
mer_rep.save(mer1)

