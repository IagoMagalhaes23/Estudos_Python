# Git e GitHub - Fundamentos

## Tópicos objetivos:
   - Git é um sistema de controle de versão distribuído gratuito e de código aberto projetado para lidar com tudo, desde projetos pequenos a muito grandes com velocidade e eficiência.
   - GitHub é um serviço de hospedagem para desenvolvimento de software e controle de versão usando Git.
   - Criar um repositório
   - Clonar um repositório
   - Fazer commit, push e pull de e para o repositório
   - Reverter um commit
   - Criar branches e pul requests
   - Lidar com merge e conflitos

## Principais comandos

### O que é Git?
    Um sistema de controle de versão, ou VCS, monitora o histórico de alteraçoes à medida que as pessoas e equipes colaboram em projetos em conjunto. Como os desenvolvedores fazem alterações no projeto, qualquer versão anterior do projeto pode ser recuperada a qualquer momento.

    Os desenvolvedores podem revisar o histórico do projeto para descobrir:

    - Quais alterações foram feitas?
    - Quem fez as alterações?
    - Quando as alterações foram feitas?
    - Por que as alterações foram necessárias?
    Os VCSs fornecem a cada colaborador uma visão unificada e consistente de um projeto, evidenciando o trabalho que já está em andamento. Ver um histórico transparente das alterações, quem as fez, e como eles contribuem para o desenvolvimento de um projeto ajuda os integrantes da equipe a manter-se alinhados enquanto trabalham de forma independente.

    Em um sistema de controle de versão distribuído, cada desenvolvedor tem uma cópia completa do projeto e do histórico do projeto. Ao contrário dos sistemas de controle de versão centralizados conhecidos, os DVCSs não precisam de uma conexão constante com um repositório central. Git é o sistema de controle de versão distribuída mais popular. O Git é comumente usado para o desenvolvimento de software de código aberto e comercial, com benefícios significativos para indivíduos, equipes e negócios.

### O que é GitHub?
    GitHub é uma plataforma de hospedagem de código para controle de versão e colaboração. Permite que você e outras pessoas trabalhem em conjunto em projetos de qualquer lugar.

### Como criar um repositório com Git?
    **git init** inicializa um novo repositório Git e começa a acompanhar um diretório existente. Ele adiciona uma subpasta oculta dentro do diretório existente que contém a estrutura de dados interna necessária para o controle de versão.

### Como clonar um repositório com Git?
    **git clone** cria uma cópia local de um projeto que já existe remotamente. O clone inclui todos os arquivos, histórico e branches do projeto.

### Como fazer commit para um repositório com Git?
    **git add** prepara uma alteração. O Git controla as alterações na base de código de um desenvolvedor, mas é necessário testar e tirar um instantâneo das alterações para incluí-las no histórico do projeto. Este comando executa o teste, a primeira parte do processo de duas etapas. Todas as mudanças que são testadas irão tornar-se parte do próximo instantâneo e parte do histórico do projeto. O teste e o commit separados dão aos desenvolvedores total controle sobre o histórico do seu projeto sem alterar como eles codificam e funcionam.

    **git commit** salva o instantâneo no histórico do projeto e conclui o processo de controle de alterações. Em suma, um commit funciona como tirar uma foto. Qualquer item que tenha sido preparado com git add passará a fazer parte do instantâneo com git commit.

    **git status** mostra o status das alterações como não controladas, modificadas ou preparadas.

    **git branch** mostra os branches que estão sendo trabalhados localmente.

### Como fazer um push para um repositório com Git?
    **git push** atualiza o repositório remoto com todos os commits feitos localmente em um branch.

### Como fazer um pull request para um repositório com Git?
    Os pull requests são o centro da colaboração em GitHub. Ao abrir um pull request, você está propondo suas alterações e solicitando que alguém analise e faça pull na sua contribuição e os mescle no seu branch. Os pull requests mostram diffs, ou diferenças, do conteúdo de ambos os branches. As alterações, adições e subtrações são exibidas em cores diferentes.

    Assim que você fizer um commit, você poderá abrir um pull request e começar uma discussão, mesmo antes de o código ser concluído.

    **git pull** atualiza a linha de desenvolvimento local com atualizações do equivalente remoto. Os desenvolvedores usam este comando se um colega fez commits em um branch remoto, e eles gostaria de refletir essas alterações no seu ambiente local.

### Como reverter um commit?
    O **git reset** por sua vez é um comando que restaura um estado anterior do HEAD, por isso que usamos o HEAD ao desfazer commits, para indicar qual o estado anterior que você quer voltar.

    O HEAD é um ponteiro que indica qual branch e commit você está. Ele é usado com frequência e muitas vezes sem você mesmo saber que ele é acessado para trocar de branches por exemplo.

### Como criar uma branch?
    O Branch permite que você tenha diferentes versões de um repositório de uma só vez.

    Por padrão, seu repositório tem um branch chamado main que é considerado o branch definitivo. Você pode criar branches adicionais com base em main no repositório. Você pode usar branches para ter diferentes versões de um projeto de uma só vez. Isso é útil quando você deseja adicionar novas funcionalidades a um projeto sem alterar a principal fonte de código. O trabalho feito em diferentes branches não aparecerá no branch principal até que você faça o merge, que abordaremos mais tarde neste guia. Você pode usar branches para fazer experimentos e edições antes de fazer commit delas em main.

    Usando o comando **git checkout** é possivel criar uma nova branch.

### Como fazer um merge?
    Às vezes, uma solicitação de pull pode introduzir alterações no código que entram em conflito com o código existente em main. Se houver algum conflito, o GitHub irá alertar você sobre o código conflitante e impedirá a fusão até que os conflitos sejam resolvidos. Você pode criar um commit que resolve os conflitos ou usar comentários na pull request para discutir os conflitos com os integrantes da equipe.

    **git merge** mescla as linhas de desenvolvimento. De modo geral, esse comando é usado para combinar alterações feitas em dois branches distintos. Por exemplo, um desenvolvedor faria merge quando quisesse combinar alterações de um branch de recurso no branch principal para implantação.

### Como lidar com conflitos?
    Quando executa uma operação de git rebase, você geralmente move commits. Por causa disso, podem ocorrer conflitos de merge. Isso significa que dois ou mais commits modificaram a mesma linha do mesmo arquivo, e o Git não sabe qual alteração aplicar.

    Depois que você reordenar e tratar os commits usando git rebase, caso ocorra um conflito de mesclagem, o Git informará isso com a seguinte mensagem impressa no terminal:
        error: could not apply fa39187... something to add to patch A

        When you have resolved this problem, run "git rebase --continue".
        If you prefer to skip this patch, run "git rebase --skip" instead.
        To check out the original branch and stop rebasing, run "git rebase --abort".
        Could not apply fa39187f3c3dfd2ab5faa38ac01cf3de7ce2e841... Change fake file

    Aqui, o Git está indicando o commit que está causando o conflito (fa39187). Você tem três opções:

    - Execute git rebase --abort para desfazer por completo a troca de base. O Git retornará você ao estado do branch em que ele estava antes de git rebase ser chamado.
    - Execute git rebase --skip para ignorar por completo o commit. Isso significa que nenhuma das alterações apresentadas pelo commit com problema será incluída. Essa opção dificilmente é usada.
    - Você pode corrigir o conflito.

    Abra Git Bash.

    Navegue até o repositório Git local que tem o conflito de merge.

    cd REPOSITORY-NAME
    Gere uma lista dos arquivos afetados pelo conflito de merge. Neste exemplo, o arquivo styleguide.md tem um conflito de mesclagem.

    $ git status
    > # On branch branch-b
    > # You have unmerged paths.
    > #   (fix conflicts and run "git commit")
    > #
    > # Unmerged paths:
    > #   (use "git add ..." to mark resolution)
    > #
    > # both modified:      styleguide.md
    > #
    > no changes added to commit (use "git add" and/or "git commit -a")
    Abra seu editor de texto favorito, como o Visual Studio Code, e procure o arquivo que contém conflitos de mesclagem.

    Para ver o início do conflito de mesclagem no arquivo, pesquise o marcador de conflito <<<<<<< no arquivo. Ao abrir o arquivo no editor de texto, você verá as alterações do branch HEAD ou base após a linha <<<<<<< HEAD. Em seguida, você verá =======, o que divide as alterações das alterações no outro branch, seguido de >>>>>>> BRANCH-NAME. Neste exemplo, uma pessoa escreveu "abra um problema" no branch HEAD ou base e outra pessoa escreveu "faça sua pergunta no IRC" no branch de comparação ou branch-a.

    If you have questions, please
    <<<<<<< HEAD
    open an issue
    =======
    ask your question in IRC.
    >>>>>>> branch-a
    Decida se você deseja manter apenas as alterações do seu branch, manter apenas as alterações do outro branch, ou fazer uma nova alteração, que pode incorporar alterações de ambos os branches. Exclua os marcadores de conflito <<<<<<<, =======, >>>>>>> e faça as alterações desejadas na mesclagem final. Neste exemplo, as duas alterações são incorporadas ao merge final:

    If you have questions, please open an issue or ask in our IRC channel if it's more urgent.
    Adicione ou faça stage das alterações.

    $ git add .
    Faça o commit das suas alterações com um comentário.

    $ git commit -m "Resolved merge conflict by incorporating both suggestions."

## Exemplos

### Contribuir para um repositório existente
    # download a repository on GitHub to our machine
    # Replace `owner/repo` with the owner and name of the repository to clone
    git clone https://github.com/owner/repo.git

    # change into the `repo` directory
    cd repo

    # create a new branch to store any new changes
    git branch my-branch

    # switch to that branch (line of development)
    git checkout my-branch

    # make changes, for example, edit `file1.md` and `file2.md` using the text editor

    # stage the changed files
    git add file1.md file2.md

    # take a snapshot of the staging area (anything that's been added)
    git commit -m "my snapshot"

    # push changes to github
    git push --set-upstream origin my-branch

### Inicie um novo repositório e publique-o em GitHub
    Primeiro, você deverá criar um novo repositório em GitHub. Para obter mais informações, confira "Olá, Mundo". Não inicialize o repositório com um arquivo LEIAME, .gitignore ou License. Este repositório vazio irá aguardar seu código.
    
    # create a new directory, and initialize it with git-specific functions
    git init my-repo

    # change into the `my-repo` directory
    cd my-repo

    # create the first file in the project
    touch README.md

    # git isn't aware of the file, stage it
    git add README.md

    # take a snapshot of the staging area
    git commit -m "add README to initial commit"

    # provide the path for the repository you created on github
    git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git

    # push changes to github
    git push --set-upstream origin main

### contribuir para um branch existente em GitHub
    Este exemplo pressupõe que você já tenha um projeto chamado repo no computador e que um novo branch tenha sido enviado por push para o GitHub desde a última vez que as alterações foram feitas localmente.

    # change into the `repo` directory
    cd repo

    # update all remote tracking branches, and the currently checked out branch
    git pull

    # change into the existing branch called `feature-a`
    git checkout feature-a

    # make changes, for example, edit `file1.md` using the text editor

    # stage the changed file
    git add file1.md

    # take a snapshot of the staging area
    git commit -m "edit file1"

    # push changes to github
    git push

## Referências
- https://docs.github.com/pt/get-started/quickstart/hello-world
- https://docs.github.com/pt/get-started/using-git/about-git
- https://pt.stackoverflow.com/questions/411048/como-criar-uma-nova-branch-no-github
- https://jtemporal.com/desfazendo-um-ou-mais-commits/
- https://docs.github.com/pt/get-started/using-git/resolving-merge-conflicts-after-a-git-rebase
- https://docs.github.com/pt/pull-requests/
collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line