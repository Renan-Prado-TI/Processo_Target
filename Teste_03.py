import json

def formatar_numero(valor):
    """Formata o numero com 4 casas decimais e ponto como separador"""
    return f"{float(valor):.4f}"

try:
    # Tenta abrir e ler o arquivo JSON
    with open('dados_01.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    
    # Verifica se existem dados para processar
    if not dados:
        print("O arquivo esta vazio!")
    else:
        # Filtrando valores validos (maiores que zero)
        valores_validos = [float(dia["valor"]) for dia in dados if isinstance(dia.get("valor"), (int, float)) and dia["valor"] > 0]
        
        if not valores_validos:
            print("Nao foram encontrados valores validos para processar.")
        else:
            # Calculando estatisticas
            menor_faturamento = min(valores_validos)
            maior_faturamento = max(valores_validos)
            media_mensal = sum(valores_validos) / len(valores_validos)
            dias_acima_da_media = sum(1 for valor in valores_validos if valor > media_mensal)
            
            # Encontrando os dias com menor e maior faturamento
            dia_menor = next((dia for dia in dados if float(dia["valor"]) == menor_faturamento), None)
            dia_maior = next((dia for dia in dados if float(dia["valor"]) == maior_faturamento), None)
            
            # Exibindo os resultados formatados
            print("=== Analise de Faturamento Mensal ===")
            print(f"\nMenor faturamento: R$ {formatar_numero(menor_faturamento)}" + 
                  (f" (Dia {dia_menor['dia']})" if dia_menor else ""))
            print(f"Maior faturamento: R$ {formatar_numero(maior_faturamento)}" +
                  (f" (Dia {dia_maior['dia']})" if dia_maior else ""))
            print(f"Media mensal: R$ {formatar_numero(media_mensal)}")
            print(f"Dias com faturamento acima da media: {dias_acima_da_media}")
            print(f"Total de dias analisados: {len(dados)}")
            print(f"Dias com faturamento: {len(valores_validos)}")
            print(f"Dias sem faturamento: {len(dados) - len(valores_validos)}")

except FileNotFoundError:
    print("Erro: O arquivo 'dados_01.json' nao foi encontrado no diretorio atual.")
except json.JSONDecodeError:
    print("Erro: O arquivo nao esta em um formato JSON valido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {str(e)}")