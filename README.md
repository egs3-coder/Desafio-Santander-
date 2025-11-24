# Desafio Santander Dev Week 2023 - Reimaginação do Pipeline ETL

Este projeto é a **reimaginação** do desafio de Projeto da Santander Dev Week 2023 da DIO, conforme solicitado: aplicar o conceito de um pipeline ETL (Extração, Transformação e Carga) em um **novo domínio de aplicação**, sem depender diretamente de APIs externas.

## 1. Domínio de Aplicação Escolhido

O domínio escolhido é a **Gestão de Desempenho Acadêmico de Estudantes**.

| Componente Original (Santander) | Componente Reimaginação (Acadêmico) |
| :--- | :--- |
| **Cliente Bancário** | **Estudante Universitário** |
| **Conta e Cartão** | **Curso e Média de Notas (GPA)** |
| **Mensagem de Marketing (IA)** | **Dica de Estudo Personalizada (Lógica de Regras)** |
| **API Externa (GET/PUT)** | **Simulação de Base de Dados Local (JSON)** |

## 2. O Pipeline ETL Reimagindo

O pipeline foi implementado no arquivo `etl_estudante.py` e segue a mesma estrutura lógica do desafio original, mas com fontes e destinos de dados simulados localmente.

### **E**xtract (Extração)

1.  **Fonte de IDs:** Os IDs dos estudantes são extraídos do arquivo `SDW2023.csv` (reutilizado do desafio original).
2.  **Fonte de Dados:** Os dados completos dos estudantes (Nome, Curso, GPA) são extraídos de um arquivo JSON local (`student_data.json`), simulando a chamada a uma API ou banco de dados.

### **T**ransform (Transformação)

1.  **Lógica de Negócio:** Em vez de usar uma API externa de IA (como o GPT-4), a transformação é realizada por uma **lógica de regras simples** baseada no GPA (Grade Point Average) do estudante.
2.  **Personalização:** Uma **Dica de Estudo Personalizada** é gerada para cada estudante, simulando a função da IA Generativa. A mensagem varia conforme a faixa de GPA, incentivando a excelência, a consistência ou a busca por ajuda.
3.  **Restrição:** A mensagem gerada é limitada a 100 caracteres, replicando a restrição de tamanho do desafio original.

### **L**oad (Carga)

1.  **Destino de Dados:** Os dados transformados (com a nova dica de estudo) são carregados de volta em um novo arquivo JSON local (`student_data_updated.json`), simulando a atualização de um registro em um banco de dados ou a chamada a um endpoint `PUT` de uma API.

## 3. Arquivos do Projeto

| Arquivo | Descrição |
| :--- | :--- |
| `etl_estudante.py` | O código-fonte principal do pipeline ETL reimaginado em Python. |
| `SDW2023.csv` | Arquivo CSV de entrada com os IDs dos estudantes a serem processados. |
| `student_data.json` | **Simulação da API/DB:** Dados iniciais dos estudantes antes do processamento. |
| `student_data_updated.json` | **Resultado da Carga:** Dados dos estudantes após a execução do ETL, contendo as dicas personalizadas. |

## 4. Como Executar

1.  Certifique-se de ter o Python e a biblioteca `pandas` instalados.
2.  Execute o script principal:
    ```bash
    python3 etl_estudante.py
    ```
3.  O console exibirá o passo a passo da execução, e o resultado final será salvo em `student_data_updated.json`.

---

### Exemplo de Saída (Console)

```
Dados iniciais salvos em student_data.json
IDs de estudantes a processar: [1, 2, 3, 4, 5]

--- Fase de Extração (E) ---
Extraído: Alice (Ciência da Computação)
Extraído: Bruno (Engenharia Civil)
Extraído: Carla (Medicina)
Extraído: Daniel (Direito)
Extraído: Eduarda (Arquitetura)

--- Fase de Transformação (T) ---
Dica gerada para Alice: Ótimo trabalho, Alice! Mantenha o foco em Ciência da Computação. Tente revisar seus materiais de est...
Dica gerada para Bruno: Bruno, você está no caminho certo em Engenharia Civil. Identifique as áreas mais desafiadoras e dedi...
Dica gerada para Carla: Parabéns, Carla! Seu desempenho em Medicina é excelente. Considere se aprofundar em um tópico de pes...
Dica gerada para Daniel: Olá, Daniel. Em Direito, é crucial reavaliar sua estratégia de estudos. Busque ajuda de professores ...
Dica gerada para Eduarda: Ótimo trabalho, Eduarda! Mantenha o foco em Arquitetura. Tente revisar seus materiais de estudo com ...

--- Fase de Carga (L) ---
Carregado: Dados de Alice atualizados com sucesso.
Carregado: Dados de Bruno atualizados com sucesso.
Carregado: Dados de Carla atualizados com sucesso.
Carregado: Dados de Daniel atualizados com sucesso.
Carregado: Dados de Eduarda atualizados com sucesso.

Dados finais salvos em student_data_updated.json

--- Pipeline ETL Concluído ---
```
