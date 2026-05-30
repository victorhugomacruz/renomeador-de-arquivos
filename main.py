import os

def obter_pasta_alvo():
    # Define o nome do arquivo de configuração (ficará na mesma pasta do script/executável)
    arquivo_txt = "caminho.txt"
    
    # Verifica se o arquivo txt já existe
    if not os.path.exists(arquivo_txt):
        # Se não existir, cria o arquivo com um caminho de exemplo
        with open(arquivo_txt, 'w', encoding='utf-8') as f:
            f.write(r"D:\Área de Trabalho\imagensvideo")
            
        print(f"⚠️ AVISO: O arquivo '{arquivo_txt}' não existia e foi criado agora.")
        print("Por favor, abra ele, cole o caminho correto da pasta e rode o robô novamente.")
        return None
    
    # Lê o caminho dentro do txt
    with open(arquivo_txt, 'r', encoding='utf-8') as f:
        # .strip() remove espaços vazios ou quebras de linha acidentais
        caminho = f.read().strip() 
        
    return caminho

def renomear_arquivos():
    pasta = obter_pasta_alvo()
    
    if not pasta:
        return  # Interrompe o processo se o txt acabou de ser criado e precisa ser preenchido
        
    # Verifica se a pasta lida do txt realmente existe no computador
    if not os.path.exists(pasta):
        print(f"❌ AVISO: A pasta informada no 'caminho.txt' não foi encontrada: \n{pasta}")
        return

    # Lista todos os itens dentro da pasta
    arquivos = [arq for arq in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, arq))]
    
    # Filtra arquivos que são imagens ou VÍDEOS
    extensoes_validas = (
        '.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', 
        '.mp4', '.mkv', '.avi', '.mov', '.webm'
    )
    arquivos_alvo = [arq for arq in arquivos if arq.lower().endswith(extensoes_validas)]

    total_arquivos = len(arquivos_alvo)
    
    if total_arquivos == 0:
        print(f"Nenhum arquivo de imagem ou vídeo encontrado no local especificado.")
        return

    print(f"✅ O robô encontrou {total_arquivos} arquivos. Preparando para renomear...\n")

    # =========================================================================
    # PASSO 1: Renomear para nomes temporários
    # =========================================================================
    print("Passo 1/2: Protegendo contra conflito de nomes...")
    arquivos_temporarios = []
    
    for i, nome_antigo in enumerate(arquivos_alvo):
        caminho_antigo = os.path.join(pasta, nome_antigo)
        
        # Separa o nome do arquivo da extensão (ex: pega apenas o '.jpg' ou '.mp4')
        extensao = os.path.splitext(nome_antigo)[1]
        
        # Cria um nome temporário
        nome_temporario = f"temp_robo_{i}{extensao}"
        caminho_temp = os.path.join(pasta, nome_temporario)
        
        os.rename(caminho_antigo, caminho_temp)
        
        # Guarda o caminho temporário e a extensão
        arquivos_temporarios.append((caminho_temp, extensao))

    # =========================================================================
    # PASSO 2: Renomear para a numeração final (1, 2, 3...)
    # =========================================================================
    print("Passo 2/2: Aplicando a numeração final...\n")
    
    # O comando 'start=1' faz a contagem começar no 1 em vez do 0
    for i, (caminho_temp, extensao) in enumerate(arquivos_temporarios, start=1):
        novo_nome = f"{i}{extensao}"
        caminho_novo = os.path.join(pasta, novo_nome)
        
        os.rename(caminho_temp, caminho_novo)
        print(f"Renomeado -> {novo_nome}")

    print(f"\n🎉 Processo concluído com sucesso!")
    print(f"Todos os {total_arquivos} arquivos foram renomeados de 1 a {total_arquivos}.")

if __name__ == "__main__":
    renomear_arquivos()
    
    # Pausa final
    input("\nPressione [ENTER] para fechar o robô...")