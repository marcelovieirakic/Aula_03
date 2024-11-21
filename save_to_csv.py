import pandas as pd

caminho_arquivo_xlsx = '/mnt/c/Users/marcelovieira/Downloads/RECUP_PARC_ENTRE_151_211.xlsx'
caminho_arquivo_csv = '/mnt/c/Users/marcelovieira/Downloads/arquivo_unido_parcelamento.csv'

try:
    print("Lendo todas as abas do arquivo Excel...")
    todas_as_abas = pd.read_excel(caminho_arquivo_xlsx, sheet_name=None)
    print(f"Lidas {len(todas_as_abas)} abas.")

    print("Concatenando dados...")
    dados_unidos = pd.concat(todas_as_abas.values(), ignore_index=True)
    print(f"Total de linhas após concatenação: {len(dados_unidos)}")

    print("Salvando o arquivo CSV....")
    dados_unidos.to_csv(caminho_arquivo_csv, index=False)
    print("Arquivo CSV criado com sucesso:", caminho_arquivo_csv)
except Exception as listar_erro:
    print("Ocorreu um erro:", listar_erro)



