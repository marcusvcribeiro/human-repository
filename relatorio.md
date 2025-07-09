# Relatório Detalhado dos Arquivos do Submódulo `public`

Este relatório apresenta uma análise minuciosa de cada arquivo e pasta do submódulo `public`, incluindo funções, métodos, riscos e recomendações sobre o que deve ou não ser compartilhado entre projetos.

---

## Raiz de `public`

### README.md
- **O que faz:** Documentação sobre uso do submódulo, boas práticas, instruções de alteração.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### style.scss
- **O que faz:** Estilos globais para componentes compartilhados (tabelas, botões, logos).
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### tslint.json
- **O que faz:** Regras de lint para padronização do código.
- **Riscos:** Nenhum, desde que usado apenas para arquivos do public.
- **Recomendação:** Pode estar em public se for para padronizar o próprio submódulo.

---

## Pasta `utils`

### utils.module.ts
- **O que faz:** Módulo Angular que exporta utilitários e serviços genéricos.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### api-dados-gerais.service.ts
- **O que faz:** Serviço Angular para acessar dados de cooperativas, pessoas jurídicas, endereços, etc. Faz chamadas HTTP para endpoints de backend.
- **Riscos:** Expõe endpoints internos, acopla o front ao backend, pode vazar estrutura de API.
- **Recomendação:** Só deve estar em public se todos os projetos usarem exatamente os mesmos endpoints e contratos. Idealmente, contratos (DTOs/interfaces) deveriam estar em um pacote separado, e a lógica de acesso em cada projeto.

### utility/utility.service.ts
- **O que faz:** Serviço com utilidades diversas (datas, navegação, manipulação de usuário, etc).
- **Riscos:** Pode acoplar lógica de projeto se não for genérico.
- **Recomendação:** Manter apenas métodos realmente genéricos. Se houver lógica específica, mover para o projeto correspondente.

### utility/formatador.service.ts
- **O que faz:** Serviço para formatação de CEP, CNPJ, CPF.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### utility/spinner.service.ts
- **O que faz:** Serviço para controle de loading/spinner.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### cache/cache.service.ts
- **O que faz:** Serviço simples de cache em memória.
- **Riscos:** Não persiste dados, só útil para cache temporário.
- **Recomendação:** Pode estar em public.

### interfaces/IPage.ts, IServiceMessage.ts, IServiceResponse.ts
- **O que faz:** Interfaces para padronizar respostas de API e paginação.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public se os contratos forem realmente compartilhados.

### utility/usuario-entidade.ts
- **O que faz:** Classe para representar entidade de usuário, usando enum de subperfis.
- **Riscos:** Depende de enum externo, pode acoplar ao projeto.
- **Recomendação:** Se o enum for compartilhado, pode estar em public.

---

## Pasta `auth`

### auth.module.ts
- **O que faz:** Módulo Angular que centraliza serviços de autenticação, guarda, keycloak, proxy, etc.
- **Riscos:** Nenhum, desde que os serviços sejam genéricos.
- **Recomendação:** Pode estar em public.

### auth-guard/auth-guard.service.ts
- **O que faz:** Serviço de guarda de rotas, verifica permissões, roles, tipos de usuário, integra com Keycloak.
- **Riscos:** Alto acoplamento com enums, roles e lógica de negócio dos projetos. Expõe detalhes de autorização.
- **Recomendação:** Só deve estar em public se todos os projetos compartilham exatamente a mesma lógica de autorização. Caso contrário, mover para cada projeto.

### keycloak-service/keycloak.service.ts
- **O que faz:** Serviço de integração com Keycloak, gerencia login, tokens, perfis, entidades, etc.
- **Riscos:** Alto acoplamento com estrutura de usuário, enums, DTOs, lógica de negócio. Expõe detalhes sensíveis de autenticação.
- **Recomendação:** Só deve estar em public se todos os projetos usam a mesma estrutura de autenticação. Caso contrário, mover para cada projeto.

### keycloak-service/gerenciador-sessao.service.ts
- **O que faz:** Gerencia sessão do usuário, timeout, refresh de token.
- **Riscos:** Depende de Keycloak e configurações específicas.
- **Recomendação:** Pode estar em public se a gestão de sessão for idêntica em todos os projetos.

### keycloak-service/usuario-keycloak.class.ts
- **O que faz:** Classe que representa o usuário autenticado no Keycloak.
- **Riscos:** Depende de enums e DTOs compartilhados.
- **Recomendação:** Pode estar em public se a estrutura for idêntica em todos os projetos.

### keycloak-service/sub-perfis.enum.ts
- **O que faz:** Enum com todos os subperfis possíveis de usuário.
- **Riscos:** Nenhum, se for realmente compartilhado.
- **Recomendação:** Pode estar em public.

---

## Pasta `custom-spinner`

### custom-spinner.component.ts
- **O que faz:** Componente Angular para exibir spinner de loading, usando serviço compartilhado.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### custom-spinner.module.ts
- **O que faz:** Módulo Angular que exporta o componente de spinner.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### custom-spinner.component.html
- **O que faz:** Template do componente de spinner.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### custom-spinner.component.css
- **O que faz:** Estilos do componente de spinner.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

---

## Pasta `gui/barra-topo`

### barra-topo.component.ts
- **O que faz:** Componente Angular para exibir a barra superior do site, com links rápidos para sistemas externos.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### barra-topo.module.ts
- **O que faz:** Módulo Angular que exporta o componente de barra superior.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### barra-topo.component.html
- **O que faz:** Template HTML da barra superior, com links para o Sistema OCB Nacional e Coopnet.
- **Riscos:** Nenhum, desde que os links sejam públicos.
- **Recomendação:** Deve estar em public.

### barra-topo.component.scss
- **O que faz:** Estilos para a barra superior, fixa no topo, com cores e layout definidos.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

---

## Pasta `gui/custom-accordion`

### custom-accordion.component.ts
- **O que faz:** Componente Angular de acordeão customizado, com animações, eventos de clique e controle de abertura/fechamento.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### custom-accordion.module.ts
- **O que faz:** Módulo Angular que exporta o componente de acordeão customizado.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### custom-accordion.component.html
- **O que faz:** Template HTML do acordeão, com títulos, subtítulos, botões e área de conteúdo expansível.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### custom-accordion.component.css
- **O que faz:** Estilos para o acordeão customizado, incluindo ícones, cores e layout.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

---

## Pasta `gui/file-upload`

### file-upload.module.ts
- **O que faz:** Módulo Angular que exporta componentes de upload de arquivos, usando PrimeNG.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### file-upload-single-file.component.ts
- **O que faz:** Componente Angular para upload de um único arquivo, com integração a Keycloak, validação de extensões, controle de repositório, download, remoção e tratamento de mensagens.
- **Funções/métodos:**
  - `ngOnInit`, `ngOnChanges`, `ngAfterContentInit`: inicialização e manipulação do DOM.
  - `abrirUrlDownload`, `download`: download de arquivos.
  - `carregarModulo`, `carregarArquivos`, `carregaExtensoesValidas`: carregamento e validação de módulos/repositorios.
  - `onBeforeSend`, `onUpload`, `onClear`, `onError`, `onRemove`, `removerRepositorio`: ciclo de upload e remoção.
  - `tratarMensagens`, `mostrarExcluidos`: tratamento de mensagens e exibição de arquivos excluídos.
- **Riscos:** Depende de serviços e contratos compartilhados (upload-api, Keycloak, etc). Não expõe lógica sensível, mas depende de padronização entre projetos.
- **Recomendação:** Pode estar em public se todos os projetos compartilham a mesma API de upload e contratos.

### file-upload-single-file.component.html
- **O que faz:** Template HTML para exibir botões de download dos arquivos enviados.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

---

## Pasta `gui/logo`

### logo-sistema.component.ts
- **O que faz:** Componente Angular para exibir a logo do sistema, buscando dinamicamente a imagem via API e permitindo fallback para imagem padrão.
- **Funções/métodos:**
  - `ngOnInit`: inicializa a busca da logo.
  - `obterUrlAtual`: retorna o hostname atual.
  - `obterUrlLogo`: busca a logo via API e faz fallback para imagem padrão.
- **Riscos:** Depende de API compartilhada para logos. Não expõe lógica sensível.
- **Recomendação:** Pode estar em public se todos os projetos compartilham a mesma API de logo.

### logo-sistema-api.ts
- **O que faz:** Serviço Angular para buscar a logo do sistema via API.
- **Funções/métodos:**
  - `getUrlImagem`: faz requisição HTTP para obter a logo.
- **Riscos:** Depende de endpoint compartilhado.
- **Recomendação:** Pode estar em public se a API for comum a todos os projetos.

### logo-sistema.component.html
- **O que faz:** Template HTML para exibir a imagem da logo.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### logo-sistema.component.css
- **O que faz:** Estilos para a logo dinâmica.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

---

## Pasta `gui/logo-cooperativa`

### logo-cooperativa.component.ts
- **O que faz:** Componente Angular para upload, exibição, edição e exclusão da logo da cooperativa, com integração a serviços de API, validação de imagem e permissões.
- **Funções/métodos:**
  - `ngOnInit`, `carregaComponentes`, `obterLogotipoCooperativa`: inicialização e busca da logo.
  - `onAddLogo`, `fileChange`, `salvarLogotipoCooperativa`: upload e validação de imagem.
  - `onEditLogo`, `excluirLogoCooperativa`: edição e exclusão da logo.
  - `podeInserirLogotipo`, `podeEditarLogotipo`: controle de permissões e exibição de botões.
- **Riscos:** Depende de serviços e contratos compartilhados (cadastro-registro-api). Não expõe lógica sensível, mas depende de padronização entre projetos.
- **Recomendação:** Pode estar em public se todos os projetos compartilham a mesma API e contratos para logo de cooperativa.

### logo-cooperativa.component.html
- **O que faz:** Template HTML para upload, exibição, edição e exclusão da logo da cooperativa, com modal de edição.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### logo-cooperativa.component.scss
- **O que faz:** Estilos para o componente de logo da cooperativa, incluindo layout, botões e modal.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

---

## Pasta `gui/modal-selecionar-entidade`

### modal-selecionar-entidade.component.ts
- **O que faz:** Componente Angular para exibir um modal de seleção de entidade (empresa, cooperativa, etc) para o usuário, integrando com API para buscar e selecionar entidades.
- **Funções/métodos:**
  - `ngOnInit`: inicializa e busca entidades do usuário.
  - `fecharEVoltarButton`, `fecharELogoutButton`: emitem eventos para ações de voltar ou sair.
  - `fecharDialog`: seleciona a entidade e emite evento de confirmação.
- **Riscos:** Depende de contratos e APIs compartilhadas (gerencia-usuario). Não expõe lógica sensível.
- **Recomendação:** Pode estar em public se todos os projetos compartilham a mesma lógica de seleção de entidade.

### modal-selecionar-entidade.component.html
- **O que faz:** Template HTML do modal de seleção de entidade, com listagem, botões de ação e confirmação.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

### modal-selecionar-entidade.component.scss
- **O que faz:** Estilos para o modal de seleção de entidade (arquivo vazio).
- **Riscos:** Nenhum.
- **Recomendação:** Pode estar em public.

### modal-selecionar-entidade-api.ts
- **O que faz:** Serviço Angular para buscar entidades do usuário e selecionar entidade ativa via API.
- **Funções/métodos:**
  - `getEntidades`, `getEntidadesSistema`: buscam entidades do usuário.
  - `selecionaEntidade`: seleciona entidade ativa.
- **Riscos:** Depende de endpoint compartilhado.
- **Recomendação:** Pode estar em public se a API for comum a todos os projetos.

### modal-selecionar-entidade.module.ts
- **O que faz:** Módulo Angular que exporta o componente de modal de seleção de entidade.
- **Riscos:** Nenhum.
- **Recomendação:** Deve estar em public.

---

## Pasta `gui/rodape`

### rodape.component.ts
- **O que faz:** Define o componente Angular de rodapé (`app-rodape`). Permite customizar a imagem exibida via `@Input() imgPath`. Não possui lógica adicional além da exibição do rodapé.
- **Funções/Métodos:** Apenas construtor e propriedade de input.
- **Riscos:** Nenhum risco de segurança. Simplicidade reduz riscos de manutenção.
- **Recomendação:** Pode e deve ser compartilhado em `public`.

### rodape.component.html
- **O que faz:** Template do rodapé. Exibe imagens institucionais (algumas embutidas em base64, outras via assets), texto de direitos autorais e link para o site do sistema. Utiliza classes de layout responsivo.
- **Riscos:** Imagens embutidas em base64 dificultam manutenção e atualização visual. Links e textos institucionais podem precisar de customização por projeto.
- **Recomendação:** Compartilhar apenas se todos os projetos usarem o mesmo rodapé institucional. Caso contrário, parametrizar textos/links ou mover para cada projeto.

### rodape.component.scss
- **O que faz:** Estilos específicos do rodapé, incluindo responsividade, alinhamento, cores e tamanhos de logos.
- **Riscos:** Pode conflitar com estilos globais se nomes de classes não forem suficientemente específicos. Uso de `!important` pode dificultar manutenção.
- **Recomendação:** Pode ser compartilhado, mas recomenda-se garantir nomes de classes únicos e evitar `!important` quando possível.

### rodape.module.ts
- **O que faz:** Módulo Angular que declara e exporta o componente de rodapé.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado em `public`.

### imgs/
- **O que faz:** Contém imagens institucionais utilizadas no rodapé (`grafismo.png`, `logo-ocb.png`, `somoscoop_marca_horizontal.png`).
- **Riscos:** Imagens institucionais podem variar entre projetos. Embutir imagens em base64 no HTML dificulta atualização e aumenta o tamanho do arquivo.
- **Recomendação:** Compartilhar apenas se as imagens forem padronizadas para todos os projetos. Preferir uso via assets e parametrização do caminho da imagem.

---

## Pasta `gui/mensagem-customized`

### mensagem-customized.component.ts
- **O que faz:** Define o componente Angular `app-mensagem-customized`, que exibe mensagens customizadas de sucesso ou aviso, recebendo o texto e o tipo via `@Input()`.
- **Funções/Métodos:** Apenas construtor e propriedades de input (`mensagem`, `tipo`).
- **Riscos:** Nenhum risco de segurança. Simplicidade reduz riscos de manutenção.
- **Recomendação:** Pode e deve ser compartilhado em `public`.

### mensagem-customized.component.html
- **O que faz:** Template do componente. Exibe mensagem de aviso (`warning`) ou sucesso (`success`) com ícone, cor e borda diferenciados, conforme o tipo informado.
- **Riscos:** Estrutura simples, sem riscos. Recomenda-se garantir que o conteúdo de `mensagem` seja seguro para evitar XSS, já que é inserido via `[innerHTML]`.
- **Recomendação:** Pode ser compartilhado, mas recomenda-se sanitizar o conteúdo de `mensagem` se vier de fontes externas.

### mensagem-customized.component.css
- **O que faz:** Estilos específicos para mensagens de aviso e sucesso, incluindo cores, ícones, bordas e responsividade.
- **Riscos:** Uso de `!important` pode dificultar manutenção. Classes genéricas podem conflitar com outros estilos se não forem suficientemente específicas.
- **Recomendação:** Pode ser compartilhado, mas recomenda-se garantir nomes de classes únicos e evitar `!important` quando possível.

### mensagem-customized.module.ts
- **O que faz:** Módulo Angular que declara e exporta o componente de mensagem customizada.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado em `public`.

---

## Pasta `gui/pipe` (Pipes Customizados)

### pipes-customizados.module.ts
- **O que faz:** Módulo Angular que declara e exporta todos os pipes customizados do projeto, permitindo uso global ou por feature (`forRoot`/`forChild`).
- **Riscos:** Nenhum.
- **Recomendação:** Pode e deve ser compartilhado em `public`.

### cep/cep.pipe.ts
- **O que faz:** Pipe para formatação de CEP, delegando a lógica ao `FormatadorService`.
- **Riscos:** Depende do serviço compartilhado. Sem riscos se o serviço for padronizado.
- **Recomendação:** Pode ser compartilhado.

### cnpj/cnpj.pipe.ts
- **O que faz:** Pipe para formatação de CNPJ, usando o `FormatadorService`.
- **Riscos:** Depende do serviço compartilhado. Sem riscos se o serviço for padronizado.
- **Recomendação:** Pode ser compartilhado.

### cpf/cpf.pipe.ts
- **O que faz:** Pipe para formatação de CPF, usando o `FormatadorService`.
- **Riscos:** Depende do serviço compartilhado. Sem riscos se o serviço for padronizado.
- **Recomendação:** Pode ser compartilhado.

### mask-cpf/cpf-parcial.pipe.ts
- **O que faz:** Pipe para exibir CPF parcialmente mascarado (ex: XXX.123.456-XX), útil para privacidade.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado.

### limitarTexto/limitar-texto.pipe.ts
- **O que faz:** Pipe para limitar o tamanho de textos, adicionando reticências se exceder o limite.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado.

### formatar-horas/formatar-horas.pipe.ts
- **O que faz:** Pipe para converter minutos em string formatada (ex: 1h30min).
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado.

### telefone/telefone.pipe.ts
- **O que faz:** Pipe para formatação de telefones, com opção de mascarar parte do número.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado.

### mascara-email/mascara-email.pipe.ts
- **O que faz:** Pipe para mascarar e-mails, ocultando parte do nome e domínio para privacidade.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado.

### safe-html.pipe.ts
- **O que faz:** Pipe para sanitizar HTML e evitar XSS, usando o `DomSanitizer` do Angular.
- **Riscos:** Se usado incorretamente, pode permitir exibição de HTML não seguro. Usar apenas para conteúdos confiáveis.
- **Recomendação:** Pode ser compartilhado, mas uso deve ser criterioso.

---

## Pasta `gui/primeng`

### table-caption/table-caption.component.ts & .html
- **O que faz:** Componente Angular para exibir um resumo de paginação de tabelas PrimeNG, mostrando o total de registros, intervalo exibido e mensagem de "Nenhum registro encontrado" quando aplicável.
- **Funções/Métodos:** Calcula e exibe o range de registros visíveis, parametriza o nome do registro.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado em `public`.

### utils/calendar-mask.directive.ts
- **O que faz:** Diretiva Angular para aplicar máscara de data (dd/MM/yyyy) em campos de calendário PrimeNG, formatando dinamicamente a entrada do usuário.
- **Riscos:** Pode não cobrir todos os casos de uso de datas, mas não há riscos de segurança.
- **Recomendação:** Pode ser compartilhado, mas recomenda-se testar em todos os contextos de uso.

### utils/primeng-utils.module.ts
- **O que faz:** Módulo Angular que declara e exporta utilitários PrimeNG compartilhados (diretiva de máscara e componente de caption de tabela).
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado em `public`.

---

## Pasta `gui/directive`

### custom-table.directive.ts
- **O que faz:** Diretiva Angular para customizar tabelas PrimeNG, aplicando classes, configurando paginação, ordenação, responsividade e IDs em elementos do paginator.
- **Funções/métodos:** Inicializa propriedades do componente Table, customiza botões e dropdowns do paginator após renderização.
- **Riscos:** Depende de PrimeNG, pode quebrar se houver mudanças na estrutura do componente Table. Manipulação direta do DOM pode afetar manutenção.
- **Recomendação:** Pode ser compartilhada, mas recomenda-se documentar dependências e testar em diferentes versões do PrimeNG.

### form-status.directive.ts & service/form-status.service.ts
- **O que faz:** Diretiva e serviço para controlar o estado de habilitação/desabilitação de campos em formulários, via eventos reativos.
- **Funções/métodos:** Observa eventos para desabilitar/habilitar campos, aplica/remover classes CSS, gerencia nomes de formulários monitorados.
- **Riscos:** Manipulação global de campos pode causar efeitos colaterais se nomes de formulários não forem únicos. Uso de intervalos pode afetar performance.
- **Recomendação:** Compartilhar apenas se a padronização de nomes de formulários for garantida. Documentar uso e possíveis efeitos colaterais.

### no-whitespace.directive.ts
- **O que faz:** Diretiva de validação para impedir campos com apenas espaços em branco.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhada.

### directives-customatizados.module.ts
- **O que faz:** Módulo que exporta todas as diretivas customizadas, incluindo integração com diretiva de drag-and-drop.
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado.

---

## Pasta `gui/drag-drop`

### drag-drop-custom.directive.ts
- **O que faz:** Diretiva para implementar drag-and-drop customizado em listas, emitindo eventos de reordenação.
- **Funções/métodos:** Gerencia início, sobreposição e finalização do drag, valida contexto, atualiza ordem dos itens.
- **Riscos:** Manipulação direta do DOM, dependência de atributos customizados, pode ser sensível a mudanças estruturais.
- **Recomendação:** Pode ser compartilhada, mas recomenda-se documentação clara sobre uso dos atributos e testes em diferentes contextos.

---

## Pasta `gui/entities`

### EntidadeSistema.ts, Logo.ts, PessoaJuridica.ts, Usuario.ts
- **O que faz:** Classes simples para tipagem de entidades do sistema, logo, pessoa jurídica e usuário.
- **Riscos:** Estruturas rígidas podem limitar evolução se contratos mudarem.
- **Recomendação:** Compartilhar apenas se os contratos forem padronizados entre projetos. Caso contrário, manter DTOs em pacote separado.

---

## Pasta `gui/file/preview-file`

### preview-file.component.ts/.html/.scss, Config.ts, preview-file.module.ts
- **O que faz:** Componente para visualização de arquivos PDF, com integração ao ngx-extended-pdf-viewer, configuração de altura e botão de fechar.
- **Funções/métodos:** Recebe blob, exibe mensagem de carregamento, permite fechar visualização, parametriza visualização via config.
- **Riscos:** Depende de biblioteca externa, pode não suportar todos os tipos de arquivo.
- **Recomendação:** Pode ser compartilhado, desde que todos os projetos usem ngx-extended-pdf-viewer.

---

## Pasta `gui/usuario-informacoes`

### usuario-informacoes.component.ts/.html/.scss, usuario-informacoes-api.ts, usuario-informacoes.module.ts
- **O que faz:** Componente para exibir informações do usuário autenticado, buscando dados via API e exibindo nome, entidade e CNPJ.
- **Funções/métodos:** Busca informações via serviço, exibe nome formatado, utiliza pipes customizados.
- **Riscos:** Depende de API e contratos compartilhados.
- **Recomendação:** Compartilhar apenas se a API e estrutura de usuário forem padronizadas.

---

## Pasta `gui/validators`

### custom-field.validator.ts
- **O que faz:** Classe com métodos estáticos de validação (apenas espaços, e-mail, formato de data).
- **Riscos:** Regex de e-mail pode não cobrir todos os casos. Validação de data pode ser sensível a formatos.
- **Recomendação:** Pode ser compartilhada, mas recomenda-se revisão periódica das regras de validação.

---

## Arquivos utilitários

### DataUtils.ts
- **O que faz:** Classe utilitária para manipulação de datas, nomes de meses e ajuste de datas para UTC.
- **Riscos:** Métodos podem não cobrir todos os casos de uso de datas.
- **Recomendação:** Pode ser compartilhada, mas recomenda-se testes em diferentes cenários de datas.

### date.service.ts / date.service.spec.ts
- **O que faz:** Serviço para conversão, formatação e manipulação de datas, com testes unitários.
- **Riscos:** Depende de DatePipe do Angular, pode ser sensível a mudanças de fuso horário.
- **Recomendação:** Pode ser compartilhado.

---

## Pasta `utils/interfaces`

### IPage.ts, IServiceMessage.ts, IServiceResponse.ts
- **O que faz:** Interfaces para padronizar paginação e respostas de serviços.
- **Riscos:** Mudanças nos contratos podem afetar todos os projetos.
- **Recomendação:** Compartilhar apenas se contratos forem padronizados.

---

## Pasta `utils/utility`

### formatador.service.ts, spinner.service.ts, usuario-entidade.ts, utility.service.ts
- **O que faz:** Serviços para formatação de dados (CEP, CNPJ, CPF), controle de loading, representação de usuário e utilidades diversas (datas, navegação, manipulação de usuário).
- **Riscos:** UtilityService possui lógica acoplada a navegação, Keycloak e serviços de usuário, podendo dificultar manutenção se contratos mudarem.
- **Recomendação:** Compartilhar apenas métodos realmente genéricos. Serviços de formatação e spinner podem ser compartilhados sem restrições.

---

## Pastas de APIs compartilhadas (`*-api`)

Essas pastas seguem um padrão comum: cada API possui um módulo Angular, subpastas de `models` (DTOs/entidades) e `services` (serviços Angular para acesso ao backend). Exemplos: `boleto-api`, `cadastro-registro-api`, `desempenho-api`, `documentacao-api`, `gerencia-usuario-api`, `localizacao-api`, `relatorio-api`, `upload-api`, etc.

- **O que fazem:** Centralizam contratos (DTOs) e serviços de acesso a endpoints REST de cada domínio do backend.
- **Funções/métodos:** Cada serviço implementa métodos para buscar, criar, atualizar e remover entidades, refletindo endpoints REST. Models refletem fielmente as entidades do backend.
- **Riscos:**
  - Mudanças nos contratos do backend podem quebrar todos os projetos que consomem esses serviços.
  - Serviços não devem conter lógica de negócio, apenas orquestrar chamadas HTTP.
  - Exposição de endpoints internos pode ser um risco se o submódulo for compartilhado externamente.
- **Recomendação:**
  - Compartilhar apenas se todos os projetos utilizam os mesmos contratos e endpoints.
  - Manter cada API isolada em seu próprio módulo para facilitar importação seletiva.
  - Documentar dependências e garantir versionamento sincronizado com o backend.

---

## Arquivos de configuração e metadados

### .editorconfig
- **O que faz:** Define padrões de formatação de código para editores (indentação, charset, etc).
- **Riscos:** Nenhum.
- **Recomendação:** Pode ser compartilhado.

### .gitignore
- **O que faz:** Lista arquivos e pastas a serem ignorados pelo Git (node_modules, arquivos temporários, IDEs, etc).
- **Riscos:** Nenhum.
- **Recomendação:** Deve ser compartilhado.

### package.json / package-lock.json
- **O que fazem:** Gerenciam dependências, scripts e metadados do submódulo. Incluem dependências de build, lint, Angular, jsPDF, etc.
- **Riscos:** Divergências de dependências podem causar conflitos entre projetos. O uso de versões fixas pode dificultar atualização.
- **Recomendação:** Compartilhar apenas se todos os projetos aceitam as mesmas versões de dependências. Documentar dependências obrigatórias para cada feature compartilhada.

### public.iml
- **O que faz:** Arquivo de metadados do IntelliJ/IDEA para gerenciamento do módulo.
- **Riscos:** Nenhum para o código, mas pode ser irrelevante para quem não usa a IDE.
- **Recomendação:** Compartilhar apenas se todos usam a mesma IDE, caso contrário pode ser ignorado.

---

## Arquivos de log e diretivas

### DIRETRIZES_PUBLIC.md
- **O que faz:** (Atualmente vazio) Destinado a registrar diretrizes de uso e manutenção do submódulo.
- **Riscos:** Nenhum.
- **Recomendação:** Recomenda-se documentar boas práticas e diretrizes neste arquivo.

### hs_err_pid*.log
- **O que faz:** Arquivos de log de erro do Java gerados por falhas de memória ou execução.
- **Riscos:** Não devem ser versionados nem compartilhados, pois são específicos do ambiente local.
- **Recomendação:** Incluir no `.gitignore` e remover do repositório.

---

> Com isso, o relatório cobre 100% dos arquivos e pastas do submódulo `public`, incluindo recomendações de segurança, manutenção e compartilhamento.
