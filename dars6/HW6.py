# S #
# class UserManager:
#     def get_user(self, user_id):
#         return f"User ID: {user_id}, Username: JohnDoe"

# class UserValidator:
#     def validate_user(self, user):
#         if "Username" in user:
#             return True
#         return False


# user_manager = UserManager()
# user = user_manager.get_user(123)
# validator = UserValidator()
# is_valid = validator.validate_user(user)

# print(user)  
# print(is_valid)  

# O #
# class PaymentProcessor:
#     def process_payment(self, payment):
#         return "umumiy to'lovni ishlash logikasi"

# class CreditCardPayment(PaymentProcessor):
#     def process_payment(self, payment):
#         return "kredit kartasi orqali to'lovni ishlash klogikasi"

# class PayPalPayment(PaymentProcessor):
#     def process_payment(self, payment):
      
#         return "PayPal orqali to'lovni ishlash uchun maxsus logika"

# payment = CreditCardPayment()
# result = payment.process_payment(100)
# print(result)  

# L #
# class DataStore:
#     def read(self, key):
#         pass

#     def write(self, key, value):
#         pass

# class SQLiteDatabase(DataStore):
#     def read(self, key):
#         # SQLite dan o'qish logikasi
#         pass

#     def write(self, key, value):
#         # SQLite ga yozish logikasi
#         pass

# class FileStore(DataStore):
#     def read(self, key):
#         # Fayldan o'qish logikasi
#         pass

#     def write(self, key, value):
#         # Faylga yozish logikasi
#         pass

# I #
# class Printer:
#     def print_document(self, document):
#         pass

# class Scanner:
#     def scan_document(self):
#         pass

# class MultiFunctionDevice(Printer, Scanner):
#     def print_document(self, document):
#         print("Printing document")

#     def scan_document(self):
#         print("Scanning document")

# class OrdinaryPrinter(Printer):
#     def print_document(self, document):
#         print("Printing document")

# D #
# class DBConnection:
#     def connect(self):
#         pass

# class MySQLConnection(DBConnection):
#     def connect(self):
#         print("Connecting to MySQL database")

# class OracleConnection(DBConnection):
#     def connect(self):
#         print("Connecting to Oracle database")

# class DataManager:
#     def __init__(self, db_connection):
#         self.db_connection = db_connection

#     def fetch_data(self):
#         self.db_connection.connect()
#         # bazadan ma'lumotlarni olish uchun kod
