
import requests
from crud import CRUD





crud = CRUD()
print(crud.list_records())
print(crud.retrieve_record('recT5rsoYpPaoMMo2'))
print(crud.create_record())
print(crud.update_record("recT5rsoYpPaoMMo2"))
print(crud.delete_record('recT5rsoYpPaoMMo2'))
print(crud.retrieve_record("recT5rsoYpPaoMMo2"))