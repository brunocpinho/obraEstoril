# Regras do Projeto Obra Estoril - Antigravity

## Trigger de Inicialização (Startup)
Toda vez que uma nova conversa, sessão ou interação neste projeto for iniciada no Antigravity:
1. **Verificação de Novos Arquivos:** Executar imediatamente o script de monitoramento:
   ```bash
   python "C:\Users\bruno\Estoril\scripts\verificar_novos_arquivos.py"
   ```
2. **Análise de Alterações:** Se o script detectar novos arquivos ou modificações em `C:\Users\bruno\GLN Engenharia LTDA\Gabriel Paiva Moreira Alves - 22- Bruno e Kelly - Estoril`:
   - Ler o arquivo `relatorio_novos_arquivos.md`.
   - Realizar a auditoria técnica e financeira dos arquivos identificados.
   - Atualizar os arquivos correspondentes do projeto (`diario_de_obra.md`, `dashboard_obra.md`, `lista_pendencias_e_riscos.md`, `base_de_conhecimento.md`).
   - Notificar o usuário sobre os impactos no cronograma, custos e engenharia.

## Verificação Recorrente Diária
- Uma rotina diária automática está agendada para as **18:00** todos os dias para conferir se a construtora GLN disponibilizou novas medições, notas fiscais, fotos ou pranchas de projeto.

## Diretrizes de Documentação
- Manter o `diario_de_obra.md` em ordem cronológica estrita.
- Cruzar dados de medições com faturas, notas e ordens de compra auditadas.
- Sincronizar as alterações de projeto com os commits no Git (`obraEstoril`).
