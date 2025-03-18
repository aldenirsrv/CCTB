# #!/bin/bash

# # Definir os tipos de commit
# commit_types=("feat" "fix" "docs" "style" "refactor" "perf" "test" "chore")

# # Função para selecionar o tipo de commit
# select_commit_type() {
#   type=$(dialog --menu "Select the type of change you're committing:" 15 50 8 \
#     "feat" "A new feature" \
#     "fix" "A bug fix" \
#     "docs" "Documentation only changes" \
#     "style" "Code style changes" \
#     "refactor" "A code change that neither fixes a bug nor adds a feature" \
#     "perf" "A performance improvement" \
#     "test" "Adding or changing tests" \
#     "chore" "Other changes that don't modify src or test files" \
#     3>&1 1>&2 2>&3)
    
#   if [ $? -ne 0 ]; then
#     clear
#     echo "Canceled"
#     exit 1
#   fi
# }

# # Função para obter o escopo do commit
# get_commit_scope() {
#   scope=$(dialog --inputbox "What is the scope of this change (e.g. component or file name): (press enter to skip)" 8 50 3>&1 1>&2 2>&3)
#   if [ $? -ne 0 ]; then
#     clear
#     echo "Canceled"
#     exit 1
#   fi
# }

# # Função para obter o subject (título) do commit
# get_commit_subject() {
#   subject=$(dialog --inputbox "Write a short, imperative tense description of the change:" 8 50 3>&1 1>&2 2>&3)
#   if [ $? -ne 0 ]; then
#     clear
#     echo "Canceled"
#     exit 1
#   fi
# }

# # Função para obter o corpo do commit (opcional)
# get_commit_body() {
#   body=$(dialog --inputbox "Provide a longer description of the change: (press enter to skip)" 8 50 3>&1 1>&2 2>&3)
# }

# # Função para obter se o commit tem mudanças quebradoras
# get_commit_breaking() {
#   is_breaking=$(dialog --yesno "Are there any breaking changes?" 6 50 3>&1 1>&2 2>&3)
#   if [ $? -eq 0 ]; then
#     breaking_body=$(dialog --inputbox "A BREAKING CHANGE commit requires a body. Please enter a longer description of the commit itself:" 8 50 3>&1 1>&2 2>&3)
#   fi
# }

# # Função para obter se o commit afeta algum problema
# get_commit_issues() {
#   is_issue_affected=$(dialog --yesno "Does this change affect any open issues?" 6 50 3>&1 1>&2 2>&3)
#   if [ $? -eq 0 ]; then
#     issues=$(dialog --inputbox "Add issue references (e.g. 'fix #123', 're #123'):" 8 50 3>&1 1>&2 2>&3)
#   fi
# }

# # Função para gerar o commit message
# generate_commit_message() {
#   scope_parsed=""
#   if [ -n "$scope" ]; then
#     scope_parsed="($scope)"
#   fi

#   # Gerar a mensagem de commit
#   commit_message="$type$scope_parsed: $subject"
#   if [ -n "$body" ]; then
#     commit_message="$commit_message\n\n$body"
#   fi
#   if [ -n "$breaking_body" ]; then
#     commit_message="$commit_message\n\nBREAKING CHANGE: $breaking_body"
#   fi
#   if [ -n "$issues" ]; then
#     commit_message="$commit_message\n\n$issues"
#   fi

#   echo -e "$commit_message"
# }

# # Função principal
# main() {
#   clear
#   echo "Start creating your commit message"

#   # Coletar informações
#   select_commit_type
#   get_commit_scope
#   get_commit_subject
#   get_commit_body
#   get_commit_breaking
#   get_commit_issues

#   # Gerar a mensagem de commit
#   commit_message=$(generate_commit_message)

#   # Exibir a mensagem de commit gerada
#   dialog --msgbox "Generated Commit Message:\n\n$commit_message" 15 50

#   # Exibir a mensagem no terminal
#   echo -e "\nGenerated Commit Message:\n$commit_message"

#   # Pedir confirmação para executar o commit
#   dialog --yesno "Do you want to proceed with the commit?" 6 50 3>&1 1>&2 2>&3
#   if [ $? -eq 0 ]; then
#     echo "$commit_message" | git commit -F -
#     clear
#   else
#     clear
#     echo "Commit canceled"
#     exit 1
    
#   fi
# }

# main


-------
#!/bin/bash

# Definindo os tipos de commit
commit_types=("feat" "fix" "docs" "style" "refactor" "perf" "test" "chore")

# Etapa 1: Selecionar o tipo de commit
select_commit_type() {
  type=$(dialog --clear --menu "Select the type of change you're committing:" 15 50 8 \
    "feat" "A new feature" \
    "fix" "A bug fix" \
    "docs" "Documentation changes" \
    "style" "Code style improvements" \
    "refactor" "Code refactoring" \
    "perf" "Performance improvements" \
    "test" "Test-related changes" \
    "chore" "Miscellaneous changes" \
    3>&1 1>&2 2>&3)
  
  # Verifica se uma opção foi selecionada
  if [ -z "$type" ]; then
    echo "No type selected, exiting..."
    exit 1
  fi
  echo "$type"
}

# Etapa 2: Obter o escopo do commit
get_commit_scope() {
  scope=$(dialog --clear --inputbox "What is the scope of this change (e.g. component or file name): (press enter to skip)" 10 50 3>&1 1>&2 2>&3)
  echo "$scope"
}

# Etapa 3: Obter o subject (título) do commit
get_commit_subject() {
  subject=$(dialog --clear --inputbox "Write a short, imperative tense description of the change:" 10 50 3>&1 1>&2 2>&3)
  echo "$subject"
}

# Etapa 4: Obter o corpo do commit (opcional)
get_commit_body() {
  body=$(dialog --clear --inputbox "Provide a longer description of the change: (press enter to skip)" 10 50 3>&1 1>&2 2>&3)
  echo "$body"
}

# Etapa 5: Perguntar se o commit tem mudanças quebradoras
# Função para obter se o commit tem mudanças quebradoras
get_commit_breaking() {
  is_breaking=$(dialog --yesno "Are there any breaking changes?" 6 50 3>&1 1>&2 2>&3)
  if [ $? -eq 0 ]; then
    breaking_body=$(dialog --inputbox "A BREAKING CHANGE commit requires a body. Please enter a longer description of the commit itself:" 8 50 3>&1 1>&2 2>&3)
  fi
}

get_commit_issues() {
  is_issue_affected=$(dialog --yesno "Does this change affect any open issues?" 6 50 3>&1 1>&2 2>&3)
  if [ $? -eq 0 ]; then
    issues=$(dialog --inputbox "Add issue references (e.g. 'fix #123', 're #123'):" 8 50 3>&1 1>&2 2>&3)
  fi
}

# Etapa 7: Confirmar e Gerar o Commit Message
generate_commit_message() {
  # Adicionar escopo se existir
  if [ -n "$scope" ]; then
    scope_parsed="($scope)"
  else
    scope_parsed=""
  fi

  # Gerar a mensagem de commit
  commit_message="$type$scope_parsed: $subject"
  if [ -n "$body" ]; then
    commit_message="$commit_message\n\n$body"
  fi
  if [ -n "$breaking_body" ]; then
    commit_message="$commit_message\n\nBREAKING CHANGE: $breaking_body"
  fi
  if [ -n "$issues" ]; then
    commit_message="$commit_message\n\n$issues"
  fi

  echo -e "$commit_message"
}

# Etapa 8: Finalizar e Pedir para o usuário Confirmar o Commit
final_confirmation() {
  dialog --clear --yesno "Do you want to proceed with the commit?\n $commit_message" 10 50 3>&1 1>&2 2>&3
  if [ $? -eq 0 ]; then
    # Executa o commit e captura o erro, caso ocorra
    commit_output=$(echo -e "$commit_message" | git commit -F - 2>&1)
    commit_status=$?

    if [ $commit_status -ne 0 ]; then
      # Se o commit falhou, mostramos a mensagem de erro
      dialog --clear --msgbox "Commit failed: $commit_output" 10 50
    else
      # Se o commit foi bem-sucedido, mostramos a mensagem de sucesso
      dialog --clear --msgbox "Commit successfully created!" 10 50
    fi
  else
    dialog --clear --msgbox "Commit canceled" 10 50
  fi
}

# Função principal para executar as etapas
main() {
  # Perguntar pelo tipo de commit
  type=$(select_commit_type)
  
  # Perguntar pelo escopo
  scope=$(get_commit_scope)

  # Perguntar pelo subject
  subject=$(get_commit_subject)

  # Perguntar pelo corpo do commit
  body=$(get_commit_body)

  # Perguntar se há mudanças quebradoras
  breaking_body=$(get_commit_breaking)

  # Perguntar se afeta algum problema
  issues=$(get_commit_issues)

  # Gerar a mensagem de commit
  commit_message=$(generate_commit_message)

  # Finalizar e confirmar o commit
  final_confirmation

  # Limpar a tela
  clear
}

# Chamar a função principal
main