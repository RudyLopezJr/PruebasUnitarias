
import unittest
import mymodule

class TestMyModule(unittest.TestCase):

    #Verificamos si obtenemos la lista de números primos    
    def test_get_prime_numbers(self):
        self.assertEqual(mymodule.get_prime_numbers(10), [2, 3, 5, 7])
    
    #Verificamos si es número primo
    def test_is_prime(self):
        self.assertTrue(mymodule.is_prime(5))
        self.assertFalse(mymodule.is_prime(6))
    
    #En la suma identificamos que de correcta la suma
    def test_sum(self):
        self.assertEqual(mymodule.sum(5, 7), 12)
        #Definimos el error esperado y probamos enviando dos valores
        with self.assertRaises(TypeError):
            mymodule.sum(5, "Python")
if __name__ == "__main__":
    unittest.main()