# Dados de faturamento por estado
faturamento_estados = {
    "SP": "R$67836,43",
    "RJ": "R$36678,66",
    "MG": "R$29229,88",
    "ES": "R$27165,48",
    "Outros": "R$19849,53"
}

def formatar_para_float(valor):
    """Converte valores no formato 'R$XXXX,XX' para float"""
    return float(valor.replace("R$", "").replace(".", "").replace(",", "."))

try:
    # Calculando o faturamento total
    valores_float = {estado: formatar_para_float(valor) for estado, valor in faturamento_estados.items()}
    faturamento_total = sum(valores_float.values())
    
    # Calculando o percentual de cada estado
    percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in valores_float.items()}
    
    # Exibindo resultados formatados
    print("=== Percentual de Representacao por Estado ===")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")
    
    print(f"\nFaturamento total da distribuidora: R$ {faturamento_total:,.2f}".replace(".", "X").replace(",", ".").replace("X", ","))

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")