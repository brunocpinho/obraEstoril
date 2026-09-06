import datetime

width = 1200
row_height = 36
header_height = 80
margin_left = 345
chart_width = 805
height = header_height + 16 * row_height + 65

start_date = datetime.date(2026, 6, 1)
end_date = datetime.date(2027, 10, 31)
total_days = (end_date - start_date).days

def date_to_x(d):
    days = (d - start_date).days
    return margin_left + (days / total_days) * chart_width

months = [
    ('Jun/26', datetime.date(2026, 6, 1)),
    ('Jul/26', datetime.date(2026, 7, 1)),
    ('Ago/26', datetime.date(2026, 8, 1)),
    ('Set/26', datetime.date(2026, 9, 1)),
    ('Out/26', datetime.date(2026, 10, 1)),
    ('Nov/26', datetime.date(2026, 11, 1)),
    ('Dez/26', datetime.date(2026, 12, 1)),
    ('Jan/27', datetime.date(2027, 1, 1)),
    ('Fev/27', datetime.date(2027, 2, 1)),
    ('Mar/27', datetime.date(2027, 3, 1)),
    ('Abr/27', datetime.date(2027, 4, 1)),
    ('Mai/27', datetime.date(2027, 5, 1)),
    ('Jun/27', datetime.date(2027, 6, 1)),
    ('Jul/27', datetime.date(2027, 7, 1)),
    ('Ago/27', datetime.date(2027, 8, 1)),
    ('Set/27', datetime.date(2027, 9, 1)),
    ('Out/27', datetime.date(2027, 10, 1)),
]

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background:#ffffff; font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;">')

svg.append('''<defs>
  <linearGradient id="gradDone" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#10b981" />
    <stop offset="100%" stop-color="#059669" />
  </linearGradient>
  <linearGradient id="gradActive" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#3b82f6" />
    <stop offset="100%" stop-color="#1d4ed8" />
  </linearGradient>
  <linearGradient id="gradAlert" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#f59e0b" />
    <stop offset="100%" stop-color="#dc2626" />
  </linearGradient>
  <linearGradient id="gradFuture" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#94a3b8" />
    <stop offset="100%" stop-color="#64748b" />
  </linearGradient>
  <linearGradient id="gradKey" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#f59e0b" />
    <stop offset="100%" stop-color="#d97706" />
  </linearGradient>
</defs>''')

# Background grid & columns
for i, (m_label, m_date) in enumerate(months):
    x1 = date_to_x(m_date)
    next_date = months[i+1][1] if i+1 < len(months) else end_date
    x2 = date_to_x(next_date)
    w_m = x2 - x1
    
    fill = '#f8fafc' if i % 2 == 0 else '#ffffff'
    total_grid_h = 16 * row_height + 25
    svg.append(f'<rect x="{x1:.1f}" y="{header_height-25}" width="{w_m:.1f}" height="{total_grid_h}" fill="{fill}" />')
    svg.append(f'<line x1="{x1:.1f}" y1="{header_height-25}" x2="{x1:.1f}" y2="{header_height + 16 * row_height}" stroke="#e2e8f0" stroke-width="1" />')
    svg.append(f'<text x="{x1 + w_m/2:.1f}" y="{header_height-8}" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">{m_label}</text>')

svg.append(f'<line x1="{margin_left + chart_width:.1f}" y1="{header_height-25}" x2="{margin_left + chart_width:.1f}" y2="{header_height + 16 * row_height}" stroke="#e2e8f0" stroke-width="1" />')

tasks = [
    ("0.0 Fundações e Contenções (ICO 5)", datetime.date(2026, 6, 15), datetime.date(2026, 8, 25), "100%", "url(#gradDone)", "#155724", "102% Finan"),
    ("1.0 Superestrutura de Concreto (ICO 6)", datetime.date(2026, 8, 26), datetime.date(2026, 12, 12), "35%", "url(#gradActive)", "#004085", "43% Finan"),
    ("  ↳ Tubulações Laje Térreo (Eletrodutos)", datetime.date(2026, 9, 4), datetime.date(2026, 9, 15), "80%", "url(#gradAlert)", "#721c24", "Risco Atraso"),
    ("  ↳ Marco: Concretagem Laje Térreo", datetime.date(2026, 9, 16), datetime.date(2026, 9, 16), "16/Set", "#dc2626", "#ffffff", "Marco Crítico"),
    ("2.0 Alvenarias, Vedações e Shafts (ICO 7)", datetime.date(2026, 10, 1), datetime.date(2027, 1, 25), "0%", "url(#gradFuture)", "#334155", "Programado"),
    ("3.0 Instalações Prediais Brutas (Elét/Hid/AC)", datetime.date(2026, 10, 20), datetime.date(2027, 2, 15), "0%", "url(#gradFuture)", "#334155", "Programado"),
    ("4.0 Impermeabilizações e Pré-Acabamentos", datetime.date(2027, 1, 15), datetime.date(2027, 4, 25), "0%", "url(#gradFuture)", "#334155", "Programado"),
    ("5.0 Elevador Residencial (Fábrica 95d + Mont)", datetime.date(2027, 4, 1), datetime.date(2027, 8, 20), "0%", "url(#gradFuture)", "#334155", "Pronto 20/Ago"),
    ("6.0 Esquadrias de Alumínio e Vidros (60d)", datetime.date(2027, 4, 5), datetime.date(2027, 6, 25), "0%", "url(#gradFuture)", "#334155", "Lead Time 60d"),
    ("7.0 Forros Gesso e Porcelanatos 1,20x1,20m", datetime.date(2027, 4, 20), datetime.date(2027, 7, 5), "0%", "url(#gradFuture)", "#334155", "Pós-Cura 28d"),
    ("8.0 Revest. Externos, Beirais ACM e Pintura Fachadas", datetime.date(2027, 4, 25), datetime.date(2027, 7, 10), "0%", "url(#gradFuture)", "#334155", "Pedra/Tijolo/ACM"),
    ("9.0 Marmoraria, Boiler, Solar e Piscina TAJ", datetime.date(2027, 6, 15), datetime.date(2027, 8, 5), "0%", "url(#gradFuture)", "#334155", "Programado"),
    ("10.0 Marcenaria de Interiores (Sob Medida)", datetime.date(2027, 6, 20), datetime.date(2027, 9, 15), "0%", "url(#gradFuture)", "#334155", "Fábrica 45d"),
    ("11.0 Louças, Metais, Luminotécnico e Pintura", datetime.date(2027, 8, 15), datetime.date(2027, 9, 30), "0%", "url(#gradFuture)", "#334155", "Programado"),
    ("12.0 Comissionamento Geral e Limpeza Fina", datetime.date(2027, 9, 25), datetime.date(2027, 10, 15), "0%", "url(#gradFuture)", "#334155", "Programado"),
    ("★ ENTREGA FINAL DAS CHAVES (TURNKEY)", datetime.date(2027, 10, 16), datetime.date(2027, 10, 20), "16 Meses", "url(#gradKey)", "#78350f", "20/10/2027"),
]

for idx, (name, d_start, d_end, pct, fill, text_color, badge) in enumerate(tasks):
    y = header_height + idx * row_height
    
    # Horizontal row separator
    svg.append(f'<line x1="15" y1="{y+row_height}" x2="{margin_left + chart_width:.1f}" y2="{y+row_height}" stroke="#f1f5f9" stroke-width="1" />')
    
    # Task Label
    is_bold = 'font-weight="bold" fill="#0f172a"' if not name.startswith("  ") else 'fill="#475569"'
    svg.append(f'<text x="20" y="{y+22}" font-size="12" {is_bold}>{name}</text>')
    
    bx1 = date_to_x(d_start)
    bx2 = date_to_x(d_end)
    bw = max(bx2 - bx1, 8)
    
    if d_start == d_end:
        svg.append(f'<polygon points="{bx1:.1f},{y+7} {bx1+9:.1f},{y+18} {bx1:.1f},{y+29} {bx1-9:.1f},{y+18}" fill="{fill}" stroke="#b91c1c" stroke-width="1.5" />')
        svg.append(f'<text x="{bx1+14:.1f}" y="{y+22}" font-size="10" font-weight="bold" fill="#dc2626">{pct} ({badge})</text>')
    else:
        svg.append(f'<rect x="{bx1:.1f}" y="{y+9}" width="{bw:.1f}" height="18" rx="4" fill="{fill}" />')
        if bw > 50:
            svg.append(f'<text x="{bx1 + bw/2:.1f}" y="{y+22}" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">{pct}</text>')
        else:
            svg.append(f'<text x="{bx1 + bw + 6:.1f}" y="{y+22}" font-size="10" font-weight="bold" fill="#475569">{pct}</text>')

# Vertical Current Date Red Line (HOJE: 05/09/2026)
today = datetime.date(2026, 9, 5)
today_x = date_to_x(today)
chart_bottom = header_height + len(tasks) * row_height

svg.append(f'<line x1="{today_x:.1f}" y1="{header_height-35}" x2="{today_x:.1f}" y2="{chart_bottom}" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5,4" />')
svg.append(f'<rect x="{today_x - 70:.1f}" y="{header_height-55}" width="140" height="20" rx="10" fill="#ef4444" />')
svg.append(f'<text x="{today_x:.1f}" y="{header_height-41}" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">▼ HOJE: 05/09/2026</text>')

# Legend
leg_y = chart_bottom + 25
svg.append(f'<g transform="translate(40, {leg_y})">')
svg.append('<rect x="0" y="0" width="14" height="14" rx="3" fill="url(#gradDone)" />')
svg.append('<text x="20" y="11" font-size="11" fill="#334155">100% Concluído</text>')

svg.append('<rect x="140" y="0" width="14" height="14" rx="3" fill="url(#gradActive)" />')
svg.append('<text x="160" y="11" font-size="11" fill="#334155">Em Andamento (Destaque)</text>')

svg.append('<rect x="330" y="0" width="14" height="14" rx="3" fill="url(#gradAlert)" />')
svg.append('<text x="350" y="11" font-size="11" fill="#334155">Atenção / Risco de Atraso</text>')

svg.append('<rect x="520" y="0" width="14" height="14" rx="3" fill="url(#gradFuture)" />')
svg.append('<text x="540" y="11" fill="#334155" font-size="11">Programado Futuro</text>')

svg.append('<polygon points="670,0 677,7 670,14 663,7" fill="#dc2626" />')
svg.append('<text x="685" y="11" font-size="11" fill="#b91c1c" font-weight="bold">Marco Crítico</text>')

svg.append('<rect x="790" y="0" width="14" height="14" rx="3" fill="url(#gradKey)" />')
svg.append('<text x="810" y="11" font-size="11" fill="#78350f" font-weight="bold">Entrega Turnkey</text>')
svg.append('</g>')

svg.append('</svg>')

output_path = r'C:\Users\bruno\Estoril\cronograma_gantt.svg'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg))
print(f'Gantt SVG successfully regenerated at {output_path}')
