# Regras do Projeto Obra Estoril - Antigravity

## Base de Conhecimento e Diretórios OneDrive Oficiais
O projeto ObraEstoril utiliza como fontes contínuas de verdade e contexto operacional os seguintes diretórios locais sincronizados:

1. **OneDrive / SharePoint GLN (Construtora):**
   - **Pasta de Engenharia e Documentos:** `C:\Users\bruno\GLN Engenharia LTDA\Gabriel Paiva Moreira Alves - 22- Bruno e Kelly - Estoril`
     - `01- Projetos` (Arquitetura, Estrutural, Elétrico, Hidrossanitário)
     - `05- Fechamento financeiro Cliente` (Planilhas de medições)
     - `07- Ordens de compras` & `10 - Coletas` (Aço, concreto, insumos)
     - `13 - Relatórios mensais` (Relatórios de evolução da construtora)
     - `16- Cronograma` (Plano de ações semanal, gargalos e prazos)
   - **OneDrive Institucional GLN:** `C:\Users\bruno\OneDrive - GLN Engenharia LTDA`

2. **OneDrive Pessoal (Exclusivo da Obra):**
   - **Caminho Único Autorizado:** `C:\Users\bruno\OneDrive\Bruno\Documentos pessoais\Imoveis Proprios\Casa KeB Estoril`
     - `Construção\Registros de Fotos e Vídeos`: Fotos, vídeos e vistorias de campo do proprietário
     - Orçamentos e contratos diretos da obra
   - **Isolamento Estrito de Escopo:** Somente a pasta `Casa KeB Estoril` acima deve ser considerada no OneDrive pessoal. Nenhuma outra pasta (como `Financeiro` ou diretórios familiares) faz parte do escopo da ObraEstoril.

---

## Trigger de Inicialização (Startup)
Toda vez que uma nova conversa, sessão ou interação neste projeto for iniciada no Antigravity:
1. **Verificação de Novos Arquivos:** Executar imediatamente o script de monitoramento:
   ```bash
   python "C:\Users\bruno\Estoril\scripts\verificar_novos_arquivos.py"
   ```
2. **Análise de Alterações:** Se o script detectar novos arquivos ou modificações na pasta da GLN (`C:\Users\bruno\GLN Engenharia LTDA\Gabriel Paiva Moreira Alves - 22- Bruno e Kelly - Estoril`):
   - Ler o arquivo `relatorio_novos_arquivos.md`.
   - Realizar a auditoria técnica e financeira dos arquivos identificados.
   - Atualizar os arquivos correspondentes do projeto (`diario_de_obra.md`, `dashboard_obra.md`, `lista_pendencias_e_riscos.md`, `base_de_conhecimento.md`).
   - Notificar o usuário sobre os impactos no cronograma, custos e engenharia.

## Verificação Recorrente em Dias Úteis
- Uma rotina automática está agendada para as **10:00**, **13:00** e **18:00** em **dias úteis (segunda a sexta)** para conferir se a construtora GLN disponibilizou novas medições, notas fiscais, fotos, coletas ou pranchas de projeto.

## Diretrizes de Consulta e Documentação
- Todas as consultas técnicas ou financeiras sobre a Obra Estoril devem cruzar as medições e projetos da GLN com as vistorias do OneDrive pessoal.
- Manter o `diario_de_obra.md` em ordem cronológica estrita.
- Cruzar dados de medições com faturas, notas e ordens de compra auditadas.
- Sincronizar as alterações de projeto com os commits no Git (`obraEstoril`). **REGRA ESTRITA:** Sempre que fizer um commit, execute obrigatoriamente o push imediato (`git push`) para manter o repositório GitHub sincronizado sem pendências.
