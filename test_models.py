import os
import unittest
import matplotlib
matplotlib.use('Agg')
import pandas as pd
from models import AlcoholLogisticModel

class TestAlcoholLogisticModel(unittest.TestCase):
    def setUp(self):
        X = pd.DataFrame({'sexo': ['Hombre', 'Mujer'] * 10,
                          'franja_horaria': ['Madrugada', 'Tarde'] * 10})
        y = pd.Series([1, 0] * 10)
        self.modelo = AlcoholLogisticModel(X, X, y, y)
    def test_entrenar_y_predecir(self):
        self.modelo.fit()
        self.assertEqual(len(self.modelo.predict()), 20)
    def test_evaluar(self):
        self.modelo.fit()
        self.modelo.evaluate()
    def test_guardar_y_cargar(self):
        self.modelo.fit()
        self.modelo.save_model('modelo_test.pkl')
        self.modelo.load_model('modelo_test.pkl')
        self.assertEqual(len(self.modelo.predict()), 20)
    def tearDown(self):
        if os.path.exists('modelo_test.pkl'):
            os.remove('modelo_test.pkl')

if __name__ == '__main__':
    unittest.main()
