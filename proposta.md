# Proposta de Transformação do Submódulo `public` em Biblioteca NPM Privada

## 1. Visão Geral

A conversão do submódulo `public` em uma biblioteca NPM privada visa garantir:
- Controle de versionamento e compatibilidade.
- Redução de quebras em projetos consumidores.
- Padronização de processos de contribuição, build e publicação.
- Segurança e rastreabilidade de alterações.

---

## 2. Arquitetura Sugerida

### 2.1 Estrutura de Pastas

```
public-lib/
  ├── src/
  │   ├── utils/
  │   ├── auth/
  │   ├── custom-spinner/
  │   ├── gui/
  │   ├── ... (demais módulos)
  │   └── index.ts
  ├── package.json
  ├── tsconfig.json
  ├── README.md
  ├── CHANGELOG.md
  └── ... (scripts de build, testes, etc)
```

- **Cada domínio (utils, auth, gui, apis, etc) deve ser um módulo Angular próprio**.
- **Exportação centralizada** em `src/index.ts`.
- **Separar contratos (DTOs/interfaces) dos serviços**.
- **Evitar dependências cruzadas desnecessárias entre módulos**.

### 2.2 Modularização
- **Módulos independentes**: cada pasta relevante deve ser um NgModule exportável separadamente.
- **Imports seletivos**: projetos consumidores importam apenas o que precisam.
- **Evitar lógica de negócio**: apenas utilidades, contratos, componentes e integrações genéricas.

---

## 3. Processos e Políticas

### 3.1 Controle de Acesso
- **Acesso de escrita restrito**: apenas mantenedores/designados podem aprovar merges e publicar versões.
- **Sugestão**: criar um time "core" responsável pela biblioteca.
- **Contribuições via PR**: demais devs só contribuem via Pull Request, com revisão obrigatória.

### 3.2 Versionamento e Publicação
- **Versionamento semântico (SemVer)** obrigatório.
- **Publicação apenas via pipeline CI/CD** 
- **Cada release deve gerar uma tag e atualizar o CHANGELOG.md**.
- **Publicação em registry privado (ex: Verdaccio, GitHub Packages, Azure Artifacts, Nexus, etc)**.

### 3.3 Integração e Testes
- **Testes unitários obrigatórios** para todos os módulos.
- **Testes de integração simulando consumo por projetos reais**.
- **CI obrigatória**: PRs só podem ser aprovados se todos os testes passarem.

### 3.4 Documentação
- **Documentação obrigatória** de cada módulo, serviço, componente e contrato.
- **Exemplos de uso** no README.md e/ou Storybook para componentes visuais.
- **Guia de migração** para projetos que usam o submódulo antigo.

---

## 4. Sugestões Específicas por Pasta/Função

### 4.1 Utils
- Consolidar utilitários duplicados (datas, formatação, validação).
- Exportar apenas métodos genéricos.
- Separar contratos em subpasta `interfaces`.

### 4.2 Auth
- Isolar integrações com Keycloak e guards em módulo próprio.
- Evitar acoplamento com enums/DTOs específicos de projetos.

### 4.3 GUI/Componentes
- Cada componente/diretiva/pipe deve ser exportado por um módulo próprio.
- Documentar dependências externas (PrimeNG, ngx-extended-pdf-viewer, etc).

### 4.4 APIs Compartilhadas
- Cada API deve ser um módulo independente.
- Contratos (DTOs) em subpasta `models`, serviços em `services`.
- Não incluir lógica de negócio.

### 4.5 Configuração
- `tsconfig.json` e `package.json` configurados para build de biblioteca Angular.
- Scripts de build, lint, testes e publicação automatizados.

---

## 5. Processo de Contribuição

1. **Fork/branch**: devs criam branch/fork para propor mudanças.
2. **Pull Request**: toda alteração deve ser submetida via PR.
3. **Revisão obrigatória**: pelo menos 1 mantenedor deve aprovar.
4. **Testes automáticos**: PR só pode ser mergeado se todos os testes passarem.
5. **Release**: apenas mantenedores podem publicar nova versão.

---

## 6. Quem Deve Ter Acesso

- **Acesso de escrita/publicação**: apenas mantenedores/core team.
- **Acesso de leitura/instalação**: todos os devs dos projetos consumidores.
- **Sugestão**: mantenedores devem ser devs experientes, com visão de arquitetura e integração entre projetos.

---

## 7. Migração dos Projetos Consumidores

- Atualizar dependências para consumir a biblioteca via NPM registry privado.
- Remover submódulo git antigo.
- Ajustar imports para novo escopo (ex: `@org/public-lib/utils`).
- Seguir guia de migração/documentação.

---

## 8. Benefícios Esperados

- Redução drástica de quebras por alterações não controladas.
- Facilidade de atualização e rollback de versões.
- Padronização e rastreabilidade.
- Melhoria na qualidade e segurança do código compartilhado.

---

> Para dúvidas, consulte a equipe de arquitetura ou mantenedores da biblioteca.
