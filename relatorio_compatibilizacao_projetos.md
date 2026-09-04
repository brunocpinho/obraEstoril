# Relatório Executivo de Compatibilização Multidisciplinar e Clash Detection
**Obra:** Residência Unifamiliar Bruno e Kelly (Casa KeB)  
**Local:** Rua João de Almeida, nº 314 – Bairro Estoril, Belo Horizonte/MG  
**Responsável Técnico pela Coordenação:** Engenheiro Coordenador de Obra  
**Status do Marco Crítico:** Concretagem da laje do Pavimento Térreo em **16/09/2026** (12 dias corridos)  
**Data do Relatório:** 04/09/2026  

---

## 1. Resumo Executivo e Matriz de Criticidade (Clash Detection)

A presente auditoria técnica foi realizada mediante cruzamento aprofundado dos projetos executivos de **Estrutura e Geotecnia** (Engª Andréia Nogueira Sallaberry - CREA 212074931-0), **Instalações Hidrossanitárias, Pluviais e Drenagem** (GLN Engenharia), **Instalações Elétricas e Especiais** (GLN Engenharia) e **Arquitetura Executiva e Interiores** (Pedro Maciel Arquitetura).

| ID | Disciplinas Envolvidas | Localização / Elemento | Criticidade | Conflito Detectado | Diretriz Executiva de Mitigação |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **CL-01** | **Hidráulico x Estrutural** | 1º Pavimento / Cobertura | **CRÍTICA** | Indicação em projeto hidráulico de furo horizontal Ø150mm em viga sem cálculo, reforço ou previsão estrutural. | **Veto formal à furação.** Desviar tubulação por baixo da viga com carenamento ou redirecionar para shaft vertical. |
| **CL-02** | **Hidráulico x Estrutural** | Laje do Térreo (Concretagem 16/09) | **CRÍTICA** | Shafts hidrossanitários (destaque para o shaft de 15x120 cm) interceptando vigotas treliçadas da laje pré-moldada. | Locar gabaritos e passantes antes de 16/09; abrir vigotas e criar nervuras duplas/cambotas. |
| **CL-03** | **Hidráulico x Estrutural x Forro** | Teto da Garagem (Subsolo) | **CRÍTICA** | Fundo de vigas a 2,56m/2,66m somado a tubulações suspensas DN 100/150 colide com forro projetado a 2,60m/2,70m (cano desce a 2,30m). | Eliminar forro plano rebaixado geral; adotar **sancas técnicas/caixotes localizados** sob as tubulações, preservando 2,70m livre. |
| **CL-04** | **Elétrico x Estrutural** | Laje do Térreo / Chegada ao QD2 | **ALTA** | Convergência de mais de 14 eletrodutos sobre a laje de 12 cm (4cm de capa); risco de cortina de conduítes e bicheiras estruturais. | Instalar 2 sleeves Ø75/Ø100mm; garantir espaçamento ≥ 50mm entre tubos e lançar circuitos no entreforro. |
| **CL-05** | **Elétrico x Arquitetura (Interiores)** | Suíte Master (Banheiro) | **ALTA** | Toalheiro térmico na divisória hidro x bacia sem circuito dedicado no QD3 e com risco de choque (Zona 2 da NBR 5410). | Criar Circuito 16 (220V/10A) no QD3 com DR ≤ 30mA e ponto com saída de cabo estanque blindada (IPX4/5). |
| **CL-06** | **Elétrico x Equipamento** | Subsolo x 1º Pavimento | **ALTA** | Motor do Elevador alocado no QD3 (Superior), embora a Casa de Máquinas esteja no Subsolo ao lado do QD1. | Transferir o circuito trifásico do Elevador diretamente para o **QD1 (Subsolo)**, evitando percurso inútil de 3 andares. |
| **CL-07** | **Elétrico x Segurança** | Garagem do Subsolo | **ALTA** | Carregador de Carro Elétrico (7.400W) com cabo 6mm² PVC em regime contínuo opera sobreaquecido (Iz < In); risco de saturação DC no DR. | Redimensionar para **10 mm² EPR/HEPR** e exigir **DR Tipo B (ou Tipo A com módulo RDC-DD 6mA)**. |
| **CL-08** | **Hidráulico x Interiores** | Área Gourmet | **MÉDIA** | Omissão de ponto de água para geladeira/cervejeira e purificador/filtro na bancada gourmet. | Derivar ramal Ø25mm a h=1,20m (cervejeira) e Tê Ø25mm com registro a h=0,55m sob a cuba antes do reboco. |
| **CL-09** | **Estrutural x Cobertura** | Laje L22 (Cobertura) | **ALTA** | Carga de 4,65 toneladas (3x caixas 1.000L + boiler 800L) com sobrecarga pontual nos pés sobre laje treliçada. | Executar painel em concreto maciço na L22 e muretas de apoio alinhadas diretamente sobre as vigas V413, V414 e V422. |
| **CL-10** | **Geotecnia x Estrutura** | Contenção da Piscina (Rev R02) | **ALTA** | 13,2 t de água ladeando caixão do subsolo com estacas de apenas 2,5m vs estacas da casa de 5 a 7m; risco de recalque diferencial e trinca na cuba. | Inspecionar solo das estacas Ø20cm; exigir dreno em PEAD perfurado 6pol, manta asfáltica dupla e impermeabilização flexível bicomponente. |
| **CL-11** | **Telecom x Automação** | Todos os Pavimentos | **ALTA** | Projeto de telecomunicações obsoleto (RJ11 multipar, interfonia predial analógica, zero APs de teto, zero infra de CFTV). | Implantar Rack VDI 19pol 12U no subsolo, 5 pontos de Access Point Wi-Fi no teto (PoE), infra de CFTV nos beirais e fio neutro nos interruptores. |
| **CL-12** | **Interiores x Hidráulico** | Boxes das Suítes 01, 02 e 03 | **MÉDIA** | Ralo linear x porcelanato 1,20x1,20m; risco de recortes finos e infiltração na laje. | Ralo linear com tampa oculta encostado na parede de fundo; caimento unidirecional (1% a 1,5%) e teste de estanqueidade de 72h. |

---

## 2. Checklist Operacional de Canteiro

| Prazo Limite | Responsável | Ação de Canteiro Obrigatória | Status |
| :---: | :---: | :--- | :---: |
| **10/09/2026** | Mestre / Carpinteiro | Ajustar fôrmas da laje do Térreo para shafts 15x120cm e 15x62cm entre vigotas, adicionando nervuras duplas. | PENDENTE |
| **12/09/2026** | Eng. de Obra | Emitir determinação formal proibindo furo Ø150mm na viga; redirecionar tubo pluvial por baixo da estrutura. | PENDENTE |
| **14/09/2026** | Eletricista / Mestre | Instalar 2 sleeves rígidos de Ø75/Ø100mm na laje do Térreo na prumada do alimentador QD1 -> QD2. | PENDENTE |
| **14/09/2026** | Hidráulico / Mestre | Posicionar e ancorar todos os tubos-camisa para bacias sanitárias e ralos na laje do Térreo. | PENDENTE |
| **15/09/2026** | Eng. de Obra | Fiscalizar o lançamento de eletrodutos sobre a laje, garantindo espaçamento de 50mm e proibindo feixes contínuos. | PENDENTE |
| **16/09/2026** | Construtora GLN | **Concretagem das vigas e laje do Pavimento Térreo com concreto usinado fck 30 MPa e vibração controlada.** | MARCO CRÍTICO |
| **28/09/2026** | Eletricista | Transferir circuito do Elevador para o QD1 e redimensionar Carregador de Carro Elétrico para cabo 10mm² EPR. | PROGRAMADO |
| **05/10/2026** | Encanador / Obra | Rasgar alvenaria do Gourmet e instalar pontos de água fria para cervejeira (h=1,20m) e filtro (h=0,55m). | PROGRAMADO |
| **15/10/2026** | Gesseiro / Arq. | Demarcar no teto da garagem as sancas técnicas em drywall sob os coletores suspensos de esgoto, mantendo forro a 2,70m nos vãos. | PROGRAMADO |
| **Fase Cobertura** | Calculista / Obra | Executar painel em concreto maciço na laje L22 e muretas de apoio alinhadas sobre as vigas V413, V414 e V422 para as 3 caixas e boiler. | PROGRAMADO |
| **Fase Acabamento** | Pedreiro / Impermeab. | Assentar ralos lineares ocultos colados na parede de fundo dos boxes e aplicar teste de estanqueidade de 72 horas. | PROGRAMADO |
