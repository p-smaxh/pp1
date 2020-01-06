from p8_1 import SMS
from p8_2 import Email
sms = SMS("889222111","662512623")
sms.set_message("Informuje ze zadanie zrobione zostało")
sms.sent()
print()
email = Email("adam@adam.pl","basia@basia.pl","Meldunek")
email.set_message("Informuje ze zadanie zrobione zostało essa")
email.sent()