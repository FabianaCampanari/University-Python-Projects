# Arquivo de teste para o pytest. Este exemplo inclui várias funções de teste e usa fixtures 
# do pytest para configuração e limpeza

import pytest

# Fixture para configuração e limpeza
@pytest.fixture
def setup_data():
    print("\nSetup")
    data = {"key1": "value1", "key2": "value2"}
    yield data
    print("\nCleanup")

# Função de teste usando a fixture
def test_key1(setup_data):
    assert setup_data["key1"] == "value1"

# Outra função de teste usando a fixture
def test_key2(setup_data):
    assert setup_data["key2"] == "value2"

# Função de teste sem usar a fixture
def test_addition():
    assert 1 + 1 == 2
