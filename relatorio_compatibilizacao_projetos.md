# Relatório Executivo de Compatibilização Multidisciplinar e Clash Detection
**Obra:** Residência Unifamiliar Bruno e Kelly (Casa KeB)  
**Local:** Rua João de Almeida, nº 314 – Bairro Estoril, Belo Horizonte/MG  
**Responsável Técnico pela Coordenação:** Engenheiro Coordenador de Obra  
**Status do Marco Crítico:** Concretagem da laje do Pavimento Térreo em **16/09/2026** (12 dias corridos)  
**Data do Relatório:** 04/09/2026  
**Premissa Estrutural Fundamental:** **100% DAS LAJES SÃO MACIÇAS DE CONCRETO ARMADO** (Painéis pré-moldados treliçados maciços Incobráz P25 TR08 justapostos e capeados com concreto usinado fck 30 MPa, com **ZERO USO DE EPS / ISOPOR** em todos os pavimentos: Subsolo, Térreo, 1º Pavimento e Cobertura).

---

## 1. Resumo Executivo e Matriz de Criticidade (Clash Detection)

A presente auditoria técnica foi realizada mediante cruzamento aprofundado dos projetos executivos de **Estrutura e Geotecnia** (Engª Andréia Nogueira Sallaberry - CREA 212074931-0), **Instalações Hidrossanitárias, Pluviais e Drenagem** (GLN Engenharia), **Instalações Elétricas e Especiais** (GLN Engenharia) e **Arquitetura Executiva e Interiores** (Pedro Maciel Arquitetura).

| ID | Disciplinas Envolvidas | Localização / Elemento | Criticidade | Conflito Detectado | Diretriz Executiva de Mitigação |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **CL-01** | **Hidráulico x Estrutural** | 1º Pavimento / Cobertura | **CRÍTICA** | Indicação em projeto hidráulico de furo horizontal Ø150mm em viga sem cálculo, reforço ou previsão estrutural. | **Veto formal à furação.** Desviar tubulação por baixo da viga com carenamento ou redirecionar para shaft vertical. |
| **CL-02** | **Hidráulico x Estrutural** | Laje do Térreo (Concretagem 16/09) | **CRÍTICA** | Laje 100% maciça de 12cm: furação posterior com martelete rompe armaduras tracionadas. Shaft 15x120cm exige emolduramento prévio. | Locar gabaritos e tubos-camisa (passantes) antes de 16/09; prever armaduras de borda em torno dos shafts maciços. |
| **CL-03** | **Hidráulico x Estrutural x Forro** | Teto da Garagem (Subsolo) | **CRÍTICA** | Fundo de vigas a 2,56m/2,66m somado a tubulações suspensas DN 100/150 colide com forro projetado a 2,60m/2,70m (cano desce a 2,30m). | Eliminar forro plano rebaixado geral; adotar **sancas técnicas/caixotes localizados** sob as tubulações, preservando 2,70m livre. |
| **CL-04** | **Elétrico x Estrutural** | Laje do Térreo / Chegada ao QD2 | **ALTA** | Convergência de mais de 14 eletrodutos sobre a laje maciça de 12 cm; risco de cortina de conduítes e bicheiras estruturais. | Instalar 2 sleeves Ø75/Ø100mm; garantir espaçamento ≥ 50mm entre tubos e lançar circuitos terminais no entreforro. |
| **CL-05** | **Elétrico x Arquitetura (Interiores)** | Suíte Master (Banheiro) | **ALTA** | Toalheiro térmico na divisória hidro x bacia sem circuito dedicado no QD3 e com risco de choque (Zona 2 da NBR 5410). | Criar Circuito 16 (220V/10A) no QD3 com DR ≤ 30mA e ponto com saída de cabo estanque blindada (IPX4/5). |
| **CL-06** | **Elétrico x Equipamento** | Subsolo x 1º Pavimento | **ALTA** | Motor do Elevador alocado no QD3 (Superior), embora a Casa de Máquinas esteja no Subsolo ao lado do QD1. | Transferir o circuito trifásico do Elevador diretamente para o **QD1 (Subsolo)**, evitando percurso inútil de 3 andares. |
| **CL-07** | **Elétrico x Segurança** | Garagem do Subsolo | **ALTA** | Carregador de Carro Elétrico (7.400W) com cabo 6mm² PVC em regime contínuo opera sobreaquecido (Iz < In); risco de saturação DC no DR. | Redimensionar para **10 mm² EPR/HEPR** e exigir **DR Tipo B (ou Tipo A com módulo RDC-DD 6mA)**. |
| **CL-08** | **Hidráulico x Interiores** | Área Gourmet | **MÉDIA** | Omissão de ponto de água para geladeira/cervejeira e purificador/filtro na bancada gourmet. | Derivar ramal Ø25mm a h=1,20m (cervejeira) e Tê Ø25mm com registro a h=0,55m sob a cuba antes do reboco. |
| **CL-09** | **Estrutural x Cobertura** | Laje L22 (Cobertura Maciça) | **ALTA** | Carga de 4,65 toneladas (3x caixas 1.000L + boiler 800L). Laje 100% maciça elimina risco de esmagamento, mas exige transmissão correta de cargas. | Construir muretas de apoio alinhadas diretamente sobre as vigas portantes V413, V414, V419 e V422 para transferir aos pilares. |
| **CL-10** | **Geotecnia x Estrutura x Acabamento** | Contenção e Cuba da Piscina (Rev R02) | **ALTA** | 13,2 t de água ladeando caixão do subsolo com estacas de 2,5m vs estacas da casa de 5 a 7m; risco de recalque diferencial e trinca na cuba sob acabamento em placas calibradas de 20x20 cm de **Maldivas Natural (TAJ)**. | Inspecionar solo das estacas Ø20cm; exigir dreno em PEAD perfurado 6pol, manta asfáltica dupla, impermeabilização flexível bicomponente na cuba, teste de estanqueidade de 72h e dupla colagem em argamassa **AC-III branca** (ancoragem IPT 780 kgf, zero dilatação). |
| **CL-11** | **Telecom x Automação** | Todos os Pavimentos | **ALTA** | Projeto de telecomunicações obsoleto (RJ11 multipar, interfonia predial analógica, zero APs de teto, zero infra de CFTV). | Implantar Rack VDI 19pol 12U no subsolo, 5 pontos de Access Point Wi-Fi no teto (PoE), infra de CFTV nos beirais e fio neutro nos interruptores. |
| **CL-12** | **Interiores x Hidráulico** | Boxes das Suítes 01, 02 e 03 | **MÉDIA** | Ralo linear x porcelanato 1,20x1,20m; risco de recortes finos e infiltração na laje. | Ralo linear com tampa oculta encostado na parede de fundo; caimento unidirecional (1% a 1,5%) e teste de estanqueidade de 72h. |

---

## 2. Interface Estrutural x Hidrossanitário (Lajes 100% Maciças de Concreto)

### 2.1. Concretagem da Laje do Térreo (16/09/2026): Painéis Treliçados Maciços
- **Tipologia Estrutural:** A laje é composta por **painéis pré-moldados treliçados maciços de concreto (Incobráz P25 TR08)**, montados justapostos sem blocos de enchimento (sem EPS), com capeamento de concreto usinado fck 30 MPa e malha superior Q-92 (espessura total  = 12	ext{ cm}$).
- **Implicações Críticas de uma Laje 100% Maciça:**
  1. **Severidade Extrema de Cortes Posteriores:** Diferente de lajes com EPS onde furos acidentais podem atingir o enchimento, em uma laje maciça toda a seção de 12cm é concreto estrutural e aço. **Qualquer perfuração posterior com martelete ou serra-copo cortará armaduras inferiores de tração e diagonais da treliça.**
  2. **Proibição de Tubulações Horizontais Embutidas:** Pela NBR 6118 (item 13.2.3), tubulações embutidas não podem superar 1/3 da espessura da laje maciça (	ext{ mm}$). Sem EPS, nenhuma tubulação horizontal de esgoto ou pluvial pode transitar por dentro da laje maciça. **100% dos coletores horizontais devem ser executados suspensos sob a laje (no entreforro) ou sobre a laje no contrapiso.**
  3. **Emolduramento Prévio de Shafts:** O **Shaft do Lavabo/Gourmet (15 x 120 cm)** e os shafts do Banheiro 01 (15 x 62 cm) e Cozinha (15 x 47 cm) devem ter seus gabaritos de madeira resinada e armaduras de borda perfeitamente travados nas fôrmas antes de 16/09.
  4. **Tubos-Camisa Pré-Concretagem:** Todos os passantes verticais para bacias sanitárias e colunas devem ser chumbados antes do lançamento do concreto usinado.

### 2.2. Veto a Furo em Viga Ø150mm (Folha 03/16 do Hidráulico)
- A Folha 03/16 prescreve furo horizontal Ø150mm em viga para o extravasor do Poço Absorvente. As pranchas estruturais 13/14 e 17/18 **não contemplam esse furo**.
- Em vigas de largura 14cm (1º Pavimento), a passagem é fisicamente impossível. Em vigas de 19cm, o furo de 18cm destrói estribos e bielas de compressão.
- **Diretriz de Canteiro:** Veto formal à furação em viga. O tubo Ø150mm deve passar por baixo da estrutura com carenamento em drywall ou descer por shaft vertical.

### 2.3. Cargas Especiais na Cobertura (Laje L22 100% Maciça)
- **Carga Concentrada:** 3 caixas d agua de 1.000L + Boiler Solar de 800L + barrilete e pressurizador = **4.650 kgf (4,65 toneladas)**.
- **Vantagem da Laje Maciça:** Sendo a laje L22 maciça de concreto armado, o risco de esmagamento de EPS é eliminado, conferindo rigidez e resistência ao puncionamento muito superiores.
- **Diretriz:** Construir muretas estruturais de concreto armado alinhadas diretamente sobre as vigas portantes **V413 (14x40), V414 (14x30), V419 (14x40) e V422 (14x30)**, transmitindo as reações dos pés do boiler diretamente aos pilares e evitando flechas diferidas.

---

## 3. Checklist Operacional de Canteiro

| Prazo Limite | Responsável | Ação de Canteiro Obrigatória | Status |
| :---: | :---: | :--- | :---: |
| **10/09/2026** | Mestre / Carpinteiro | Ajustar fôrmas da laje maciça do Térreo para shafts 15x120cm e 15x62cm, com armaduras de borda. | PENDENTE |
| **12/09/2026** | Eng. de Obra | Emitir determinação formal proibindo furo Ø150mm na viga; redirecionar tubo pluvial por baixo da estrutura. | PENDENTE |
| **14/09/2026** | Eletricista / Mestre | Instalar 2 sleeves rígidos de Ø75/Ø100mm na laje do Térreo na prumada do alimentador QD1 -> QD2. | PENDENTE |
| **14/09/2026** | Hidráulico / Mestre | Posicionar e ancorar todos os tubos-camisa para bacias sanitárias e ralos na laje maciça do Térreo. | PENDENTE |
| **15/09/2026** | Eng. de Obra | Fiscalizar o lançamento de eletrodutos sobre a laje, garantindo espaçamento de 50mm e proibindo feixes contínuos. | PENDENTE |
| **16/09/2026** | Construtora GLN | **Concretagem das vigas e laje maciça do Térreo com concreto usinado fck 30 MPa e vibração controlada.** | MARCO CRÍTICO |
| **28/09/2026** | Eletricista | Transferir circuito do Elevador para o QD1 e redimensionar Carregador de Carro Elétrico para cabo 10mm² EPR. | PROGRAMADO |
| **05/10/2026** | Encanador / Obra | Rasgar alvenaria do Gourmet e instalar pontos de água fria para cervejeira (h=1,20m) e filtro (h=0,55m). | PROGRAMADO |
| **15/10/2026** | Gesseiro / Arq. | Demarcar no teto da garagem as sancas técnicas em drywall sob os coletores suspensos de esgoto, mantendo forro a 2,70m nos vãos. | PROGRAMADO |
| **Fase Cobertura** | Calculista / Obra | Construir muretas de apoio alinhadas sobre as vigas V413, V414 e V422 para as 3 caixas e boiler sobre a laje maciça L22. | PROGRAMADO |
| **Fase Acabamento** | Pedreiro / Impermeab. | Assentar ralos lineares ocultos colados na parede de fundo dos boxes (pisos 1,20x1,20m) e aplicar teste de estanqueidade de 72 horas. | PROGRAMADO |
| **Fase Acabamento** | Azulejista / Obra | Assentar rocha natural **Maldivas Natural 20x20 cm (TAJ)** na piscina com dupla colagem em argamassa **AC-III branca**, execução de boleamento in situ em degraus/bordas e rejunte epóxi impermeável anti-fungo. | PROGRAMADO |
