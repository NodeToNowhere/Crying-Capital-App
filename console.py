import pdb
from models.merchant import Merchant

import repositories.merchant_repository as mer_rep


mer_rep.delete_all()


mer1 = Merchant("Amazon")
mer_rep.save(mer1)

mer2 = Merchant("EvilCorp")
mer_rep.save(mer2)

mer3 = Merchant("ShellCorp")
mer_rep.save(mer3)
