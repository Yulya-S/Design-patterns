import connexion

from Src.data_reposity import data_reposity
from Src.start_service import start_service
from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.nomenclature_service import nomenclature_service

app = connexion.FlaskApp(__name__)
app.add_api("../swagger.yaml")

reposity = data_reposity()
manager = settings_manager()
manager.open("../settings.json")
receipt = receipt_book_menager()
start = start_service()
nomenclature_service = nomenclature_service()

start.create(".")
