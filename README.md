# Organizador de Arquivos
![Em Progresso](https://img.shields.io/badge/Status-Em_Progresso-F7DC6F?style=for-the-badge&logo=progress&logoColor=white)

## ✏ Resumo
_Automatização da organização de arquivos, permitindo o armazenamento correto e eficiente de documentos, reduzindo erros humanos e otimizando o fluxo de trabalho da equipe._

## 🛠️ Instalação
```bash
git clone https://github.com/owner/repo.git
cd automacaoAmbev
pip install inputimeout
pip install customtkinter
```
## 💻 Tecnologias
### Linguagem
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Utilizada para desenvolver a lógica de organização automática de arquivos, manipulação de diretórios, leitura e validação de caminhos, padronização de nomes e criação de scripts executáveis (.exe).

---

### 📚 Bibliotecas Principais
**os** → manipulação de arquivos e pastas (criação, verificação e movimentação).

**shutil** → cópia e movimentação de arquivos entre pastas.

**time** → execução periódica do script (agendamento de ciclos).

**re** → manipulação e padronização de nomes de arquivos e pastas através de expressões regulares.

**ctypes** → interação com o sistema operacional para notificações ou controles avançados.

**customtkinter** → criação da interface gráfica (em desenvolvimento) para execução manual pelo usuário.

**inputimeout** → entrada de dados do usuário com tempo limite, garantindo que o script não trave indefinidamente.

### 📌 Lógica do Script

- Configuração inicial: Verifica a existência do arquivo MeuAPP.txt contendo os caminhos de entrada e saída; cria o arquivo se não existir.

- Validação de caminhos: Lê os caminhos configurados e aguarda input do usuário se forem inválidos.

- Padronização e manipulação de nomes: Remove códigos de documentos, palavras curtas e converte tudo para minúsculas; aplica palavras-chave para correspondência correta entre arquivos e pastas.

- Organização de arquivos: Move arquivos automaticamente para a pasta correta ou cria novas pastas quando necessário.

- Execução periódica: Roda a cada 2 horas para processar novos arquivos sem sobrecarregar o computador.

- Interface gráfica (em desenvolvimento): Permite execução manual do script pelo usuário de forma amigável.
