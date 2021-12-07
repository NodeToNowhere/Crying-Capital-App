import pdb
from controllers.transaction_controller import transactions
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tags_repo
import repositories.transaction_repository as transaction_repo
from managers.transaction import total


merchant_repo.delete_all()
tags_repo.delete_all()

# transaction_repo.set_default()

mer1 = Merchant("Amazon")
merchant_repo.save(mer1)

mer2 = Merchant("EvilCorp")
merchant_repo.save(mer2)

mer3 = Merchant("ShellCorp")
merchant_repo.save(mer3)

print(merchant_repo.select(3))

print(merchant_repo.select_all())


tag1 = Tag("Utilities")
tags_repo.save(tag1)

tag2 = Tag("Transport")
tags_repo.save(tag2)

tag3 = Tag("Espionage")
tags_repo.save(tag3)

print(tags_repo.select(2))

print(tags_repo.select_all())


tran1 = Transaction(45.55, "12-12-12", "Cigarettes and wine", mer2, tag3)
transaction_repo.save(tran1)

tran2 = Transaction(12.22, "11-11-11", "Bus to funeral", mer3, tag2)
transaction_repo.save(tran2)

tran3 = Transaction(23.12, "9-9-99", "Spam and juice", mer1, tag1)
transaction_repo.save(tran3)

tran4 = Transaction(11.11, "8-8-88", "Monthly debt repayments", mer2, tag3)
transaction_repo.save(tran4)


print("The total is ", total())


pdb.set_trace()


# Have tag+merchant "none" that fills sql with "none"
