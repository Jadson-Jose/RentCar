import requests

def consultar_preco_parallelum(marca_id, modelo_id, ano_codigo):
    url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos/{modelo_id}/anos/{ano_codigo}"
    print(f"Consultando: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            dados = response.json()
            preco_str = dados.get("Valor", "")
            if preco_str:
                preco_limpo = preco_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
                return float(preco_limpo)
    except requests.RequestException as e:
        print(f"Erro ao consultar Parallelum: {e}")
    return None
