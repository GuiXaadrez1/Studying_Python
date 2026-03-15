# Conceito Fundamental: Modelo de Automação

Toda automação com pywinauto segue 4 etapas principais.

```bash
1 → Conectar ou iniciar aplicação
2 → Identificar janela
3 → Localizar controle
4 → Executar ação
```

# Fluxo lógica

```bash
Application
     ↓
Window
     ↓
Control
     ↓
Action
```

Ou em código:

```python

# CRIAR UM OBJETO PYWINAUTO PARA INICIALIZAR, EXECUTAR UM PRGRAMA
app = Application().start("program.exe")

# IDENTIFICA UMA JANELA
window = app.window(title="Janela")

# ACESSA UM COMPONENTE DESSA JANELA PELO TITULO DO COMPONENTE...
# NESTE CASO É UM BUTTON "OK"
button = window.child_window(title="OK")

# EXECUTA O EVENTO DE CLICAR
button.click()
```

## Estrutura da Biblioteca
O pywinauto possui alguns módulos principais.

| Módulo                | Função                      |
| --------------------- | --------------------------- |
| `Application`         | conecta ou inicia programas |
| `WindowSpecification` | representa uma janela       |
| `WrapperObject`       | controle específico         |
| `mouse`               | automação de mouse          |
| `keyboard`            | automação de teclado        |


## Conceito Mais Importante - DICAS

Automação com pywinauto depende de 3 habilidades técnicas:

```bash
1. Inspecionar interface
2. Entender árvore de controles
3. Criar seletores estáveis
```
