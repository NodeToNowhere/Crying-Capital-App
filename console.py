import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.merchant_repository as mer_rep
import repositories.tag_repository as tag_rep
import repositories.transaction_repository as tran_rep

mer_rep.delete_all()
tag_rep.delete_all()


mer1 = Merchant("Amazon")
mer_rep.save(mer1)

mer2 = Merchant("EvilCorp")
mer_rep.save(mer2)

mer3 = Merchant("ShellCorp")
mer_rep.save(mer3)

print(mer_rep.select(3))

print(mer_rep.select_all)


tag1 = Tag("Utilities")
tag_rep.save(tag1)

tag2 = Tag("Transport")
tag_rep.save(tag2)

tag3 = Tag("Espionage")
tag_rep.save(tag3)

print(tag_rep.select(2))

print(tag_rep.select_all)


tran1 = Transaction(45.55, "12/12/12", "Cigarettes and wine", mer2, tag3)
tran_rep.save(tran1)

tran2 = Transaction(12.22, "11/11/11,", "Bus to funeral", mer3,tag2)
tran_rep.save(tran2)

tran2 = Transaction(23.12, "9/9/09", "Spam and juice", mer1, tag1)
tran_rep.save(tran2)

pdb.set_trace()
