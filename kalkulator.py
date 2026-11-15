import logging

def tambah(a,b):

    try:
        assert a < 0 and b < 0 , " angka tidak boleh kurang dari nol"
        logging.debug("---- perhitungan di mulai------")
        hasil= a+b
        logging.info(f"hasil dari {a} + {b} adalah {hasil}")
        return hasil

    except  AssertionError as e :
        logging.error(f"terdapat error yaitu {e}")
