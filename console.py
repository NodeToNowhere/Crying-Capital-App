import pdb
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as mer_rep
import repositories.tag_repository as tag_rep

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

# pdb.runcall(mer_rep.select_all())
pdb.set_trace()
