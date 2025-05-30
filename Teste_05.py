def inverter_string(texto):
    """
    Inverte os caracteres de uma string manualmente.
    
    Args:
        texto (str): A string a ser invertida
        
    Returns:
        str: A string invertida
    """
    if not isinstance(texto, str):
        raise ValueError("A entrada deve ser uma string")
        
    return texto[::-1]  # Forma mais pythonica de inverter uma string

def main():
    try:
        # Entrada do usuario
        entrada = input("Digite uma string para inverter (ou 'sair' para encerrar): ")
        
        # Verifica se o usuario quer sair
        if entrada.lower() == 'sair':
            print("Encerrando o programa...")
            return
            
        # Inverte e exibe o resultado
        resultado = inverter_string(entrada)
        print(f"\nString original: {entrada}")
        print(f"String invertida: {resultado}")
        print("-" * 50 + "\n")
        
        # Permite inverter outra string
        main()
        
    except Exception as e:
        print(f"\nErro: {str(e)}")
        print("Tente novamente.\n")
        main()

if __name__ == "__main__":
    print("=== Inversor de Strings ===")
    print("Digite 'sair' a qualquer momento para encerrar.\n")
    main()