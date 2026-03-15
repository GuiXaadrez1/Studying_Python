# Introducao ao PyWinAuto

O PywinAuto é uma biblioteca Python especializada em **automação de aplicações desktop no Windows. ** Ele permite controlar interfaces gráficas como se fosse um usuário. Exemplos:

- clicar em botões
- preencher campos 
- navegar por menus 
- extrair textos
- automatizar rotinas repetitivas

Internamente ele usa duas APIs do Windows... 

| Backend | API usada     | Aplicações                      |
| ------- | ------------- | ------------------------------- |
| `win32` | Win32 API     | aplicativos antigos (Win32/MFC) |
| `uia`   | UI Automation | apps modernos (WPF, UWP, .NET)  |


na prática:

```bash

Aplicação Windows
       ↓
UI Automation / Win32
       ↓
Pywinauto
       ↓
Script Python

```

Isso transforma o Python em uma ferramenta de RPA (Robotic Process Automation).

## 1. Instalação do Pywinauto - Requisitos

- Sistema Operacional Windows

- Python na versao ≥ 3.8

### Instalação:

```bash
    pip install pywinauto
```
Também é recomendado instalar:

```bash
    pip install pywin32
```

Ferramentas auxiliares importantes:

- inspect.exe

Ela vem no Windows SDK e permite inspecionar elementos da interface. Para encontrar e usar a Ferramenta de Inspeção (Inspect.exe) no Windows, siga estes passos:

- Instale o Windows SDK: O Inspect.exe não é distribuído separadamente. Você precisa baixar e instalar o Windows Software Development Kit (SDK).  Acesse o site oficial da Microsoft para baixar o SDK e, durante a instalação, certifique-se de selecionar a opção para incluir as ferramentas de desenvolvimento.

<a href="https://learn.microsoft.com/pt-br/windows/apps/windows-sdk/"> Baixe o Inspect<a>

- Localize o arquivo: Após a instalação, o Inspect.exe estará localizado no diretório:

```bash
    C:\Program Files (x86)\Windows Kits\10\bin\<versão>\x64\Inspect.exe  
```

- Recomendo que crie um atalho até o executavél para facilitar...

O caminho pode variar ligeiramente dependendo da versão do SDK instalada.

- Execute a ferramenta: Navegue até a pasta e clique duas vezes no Inspect.exe para abri-lo. A ferramenta exibirá uma árvore hierárquica dos elementos da interface do usuário (UI) de qualquer aplicativo aberto, permitindo inspecionar propriedades, padrões de controle e eventos — essencial para testes de acessibilidade e depuração

Alternativas úteis:

- Accessibility Insights for Windows: Ferramenta gratuita da Microsoft para análise de acessibilidade.

- UI Automation Verify: Outra ferramenta do SDK para testes de automação da interface. 

⚠️ Evite baixar Inspect.exe de sites não oficiais, pois pode conter malware. Sempre obtenha o SDK diretamente da Microsoft.