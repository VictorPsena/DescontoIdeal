# model.py
# Exemplo: aqui você coloca o carregamento do modelo e a função que processa as 4 entradas.
# Substitua a função fake por sua lógica real (por exemplo, carregar um modelo Keras e predizer).

import numpy as np
# se usar keras: from tensorflow import keras

def process_inputs(inputs):
    """
    inputs: lista de 4 floats [x1, x2, x3, x4]
    retorna: lista de valores (por exemplo, [v1, v2, v3])
    """
    # validar
    if not isinstance(inputs, (list, tuple)) or len(inputs) != 4:
        raise ValueError("A função espera uma lista com 4 valores numéricos.")

    # ------ EXEMPLO SIMPLES (substituir pela sua lógica) ------
    arr = np.array(inputs, dtype=float).reshape(1, -1)
    # exemplo: retorno de 3 valores derivados
    v1 = float(np.sum(arr))            # soma
    v2 = float(np.mean(arr))           # média
    v3 = float(np.prod(arr)) if np.all(arr != 0) else 0.0  # produto (cuidado com overflow)
    retorno = [v1, v2, v3]
    # ---------------------------------------------------------

    return retorno