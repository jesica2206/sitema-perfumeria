import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def run_project():
    print("🚀 Iniciando suite de validación del TP...")
    
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n✅ TODO FUNCIONA PERFECTO.")
    else:
        print("\n❌ Hubo errores en la validación, revisa los mensajes arriba.")

if __name__ == "__main__":
    run_project()