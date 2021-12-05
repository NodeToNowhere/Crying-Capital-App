import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.merchant_repository as mer_repo
import repositories.tag_repoository as tag_repo
import repositories.transaction_repository as tran_repo

mer_repo.delete_all()
tag_repo.delete_all()


mer1 = Merchant("Amazon")
mer_repo.save(mer1)

mer2 = Merchant("EvilCorp")
mer_repo.save(mer2)

mer3 = Merchant("ShellCorp")
mer_repo.save(mer3)

print(mer_repo.select(3))

print(mer_repo.select_all)


tag1 = Tag("Utilities")
tag_repo.save(tag1)

tag2 = Tag("Transport")
tag_repo.save(tag2)

tag3 = Tag("Espionage")
tag_repo.save(tag3)

print(tag_repo.select(2))

print(tag_repo.select_all)


tran1 = Transaction(45.55, "12-12-12", "Cigarettes and wine", mer2, tag3)
tran_repo.save(tran1)

tran2 = Transaction(12.22, "11-11-11", "Bus to funeral", mer3, tag2)
tran_repo.save(tran2)

tran3 = Transaction(23.12, "9-9-99", "Spam and juice", mer1, tag1)
tran_repo.save(tran3)

tran4 = Transaction(11.11, "8-8-88", "Monthly debt repayments", mer2, tag3)
tran_repo.save(tran4)
pdb.set_trace()


#Have tag+merchant "none" that fills sql with "none"