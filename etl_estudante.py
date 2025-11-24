import pandas as pd
import json
import os

# --- Configuração ---
SOURCE_CSV = 'SDW2023.csv' # Reutilizando o arquivo de IDs, mas agora como StudentIDs
STUDENT_DATA_FILE = 'student_data.json' # Simulação do banco de dados/API de usuários
OUTPUT_DATA_FILE = 'student_data_updated.json' # Simulação do banco de dados/API após a carga

# Dados simulados de estudantes (Simulação da API GET /users/{id})
# O campo 'news' será 'tips' (dicas)
initial_student_data = [
    {
        "id": 1,
        "name": "Alice",
        "course": "Ciência da Computação",
        "current_gpa": 8.5,
        "tips": []
    },
    {
        "id": 2,
        "name": "Bruno",
        "course": "Engenharia Civil",
        "current_gpa": 7.2,
        "tips": []
    },
    {
        "id": 3,
        "name": "Carla",
        "course": "Medicina",
        "current_gpa": 9.1,
        "tips": []
    },
    {
        "id": 4,
        "name": "Daniel",
        "course": "Direito",
        "current_gpa": 6.8,
        "tips": []
    },
    {
        "id": 5,
        "name": "Eduarda",
        "course": "Arquitetura",
        "current_gpa": 8.0,
        "tips": []
    }
]

# Salvar os dados iniciais para simular a fonte de dados (API/DB)
with open(STUDENT_DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(initial_student_data, f, indent=2)

print(f"Dados iniciais salvos em {STUDENT_DATA_FILE}")

# --- Funções do Pipeline ETL ---

def extract(student_ids):
    """
    Extração (E): Lê os IDs do CSV e simula a busca de dados do estudante.
    """
    print("\n--- Fase de Extração (E) ---")
    
    # Simulação da API GET /users/{id}
    all_students = {}
    with open(STUDENT_DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for student in data:
            all_students[student['id']] = student

    students = []
    for student_id in student_ids:
        student = all_students.get(student_id)
        if student:
            print(f"Extraído: {student['name']} ({student['course']})")
            students.append(student)
        else:
            print(f"ID {student_id} não encontrado na base de dados simulada.")
            
    return students

def transform(students):
    """
    Transformação (T): Gera uma dica de estudo personalizada (simulação de IA).
    """
    print("\n--- Fase de Transformação (T) ---")
    
    # Simulação da IA Generativa (GPT-4) com lógica de regras simples
    def generate_study_tip(student):
        name = student['name']
        course = student['course']
        gpa = student['current_gpa']
        
        if gpa >= 9.0:
            tip = f"Parabéns, {name}! Seu desempenho em {course} é excelente. Considere se aprofundar em um tópico de pesquisa ou mentorar colegas para consolidar seu conhecimento."
        elif gpa >= 8.0:
            tip = f"Ótimo trabalho, {name}! Mantenha o foco em {course}. Tente revisar seus materiais de estudo com mais frequência para alcançar a excelência."
        elif gpa >= 7.0:
            tip = f"{name}, você está no caminho certo em {course}. Identifique as áreas mais desafiadoras e dedique tempo extra a elas. A consistência é a chave!"
        else:
            tip = f"Olá, {name}. Em {course}, é crucial reavaliar sua estratégia de estudos. Busque ajuda de professores ou tutores para melhorar seu GPA. Não desista!"
            
        # Limitar a 100 caracteres, simulando a restrição do desafio original
        return tip[:100] + '...' if len(tip) > 100 else tip

    for student in students:
        tip = generate_study_tip(student)
        print(f"Dica gerada para {student['name']}: {tip}")
        
        # Adiciona a nova dica à lista de dicas (simulando o campo 'news')
        student['tips'].append({
            "icon": "📚", # Ícone de livro para simular o ícone da API
            "description": tip
        })
        
    return students

def load(students):
    """
    Carga (L): Atualiza os dados dos estudantes na base de dados simulada.
    """
    print("\n--- Fase de Carga (L) ---")
    
    # Simulação da API PUT /users/{id}
    
    # 1. Carregar o estado atual do "banco de dados"
    if os.path.exists(STUDENT_DATA_FILE):
        with open(STUDENT_DATA_FILE, 'r', encoding='utf-8') as f:
            all_students = json.load(f)
    else:
        all_students = []

    # 2. Criar um mapa de IDs para facilitar a atualização
    student_map = {s['id']: s for s in all_students}
    
    # 3. Atualizar os dados dos estudantes processados
    for student in students:
        student_id = student['id']
        if student_id in student_map:
            # Atualiza o registro existente com os novos dados (incluindo as novas dicas)
            student_map[student_id] = student
            print(f"Carregado: Dados de {student['name']} atualizados com sucesso.")
        else:
            # Adiciona um novo registro se não existir (caso improvável aqui, mas boa prática)
            student_map[student_id] = student
            print(f"Carregado: Novo estudante {student['name']} adicionado.")

    # 4. Salvar o estado atualizado no arquivo de saída
    updated_students_list = list(student_map.values())
    with open(OUTPUT_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(updated_students_list, f, indent=2)
        
    print(f"\nDados finais salvos em {OUTPUT_DATA_FILE}")
    
    return updated_students_list

# --- Execução do Pipeline ---

def run_etl():
    # E: Extrair IDs do CSV
    try:
        df = pd.read_csv(SOURCE_CSV)
        student_ids = df['UserID'].tolist()
        print(f"IDs de estudantes a processar: {student_ids}")
    except FileNotFoundError:
        print(f"Erro: Arquivo {SOURCE_CSV} não encontrado.")
        return

    # E: Extrair dados dos estudantes
    students_data = extract(student_ids)
    
    if not students_data:
        print("Nenhum dado de estudante extraído. Encerrando.")
        return

    # T: Transformar (gerar dicas)
    students_transformed = transform(students_data)

    # L: Carregar (atualizar a base de dados)
    students_loaded = load(students_transformed)
    
    print("\n--- Pipeline ETL Concluído ---")
    
if __name__ == "__main__":
    run_etl()
