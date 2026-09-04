#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Verificação Periódica e Sincronização - Obra Estoril
Monitora novos arquivos e modificações na pasta da GLN Engenharia LTDA.
Data de corte inicial: 01/09/2026.
"""

import os
import sys
import json
import hashlib
from datetime import datetime

# Caminhos padrão do projeto
BASE_GLN_DIR = r"C:\Users\bruno\GLN Engenharia LTDA\Gabriel Paiva Moreira Alves - 22- Bruno e Kelly - Estoril"
PROJECT_DIR = r"C:\Users\bruno\Estoril"
STATE_FILE = os.path.join(PROJECT_DIR, ".sync_state.json")
REPORT_FILE = os.path.join(PROJECT_DIR, "relatorio_novos_arquivos.md")

# Data de corte padrão: 01/09/2026 00:00:00
DEFAULT_CUTOFF = datetime(2026, 9, 1, 0, 0, 0)

def compute_file_hash(filepath, max_size=10*1024*1024):
    """Calcula MD5 do arquivo (apenas até max_size para arquivos grandes)."""
    try:
        hasher = hashlib.md5()
        with open(filepath, "rb") as f:
            buf = f.read(max_size)
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception:
        return ""

def load_state():
    """Carrega o estado salvo da última verificação."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Aviso: Não foi possível carregar estado anterior ({e}). Iniciando novo.")
    return {
        "last_check": DEFAULT_CUTOFF.isoformat(),
        "files": {}
    }

def save_state(state):
    """Salva o estado atualizado."""
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar estado: {e}")

def categorize_file(rel_path):
    """Classifica o arquivo para organização no relatório."""
    rel_lower = rel_path.lower()
    if "projeto" in rel_lower or "estrutural" in rel_lower or "arquitet" in rel_lower:
        return "Projetos Técnicos (Arquitetura/Estrutura/Instalações)"
    elif "fechamento financeiro" in rel_lower or "medição" in rel_lower or "medicao" in rel_lower:
        return "Fechamento Financeiro / Medições de Obra"
    elif "ordens de compras" in rel_lower or "nota" in rel_lower or "boleto" in rel_lower:
        return "Ordens de Compra, Faturas e Boletos"
    elif "cronograma" in rel_lower:
        return "Cronograma e Prazos Executivos"
    elif "coletas" in rel_lower:
        return "Coletas e Cotações de Preços"
    elif "diário" in rel_lower or "diario" in rel_lower:
        return "Diários de Obra"
    elif "fotográfico" in rel_lower or "fotografico" in rel_lower:
        return "Registros Multimídia / Fotos"
    return "Outros Documentos"

def scan_folder(target_dir, last_check_dt):
    """Varre a pasta identificando arquivos novos ou alterados."""
    current_files = {}

    if not os.path.exists(target_dir):
        print(f"Erro: Diretório não encontrado: {target_dir}")
        return current_files

    for root, _, files in os.walk(target_dir):
        for fname in files:
            # Ignorar temporários e arquivos de sistema
            if fname.startswith("~$") or fname.startswith("."):
                continue
            
            fpath = os.path.join(root, fname)
            try:
                stat = os.stat(fpath)
            except OSError:
                continue

            mtime_dt = datetime.fromtimestamp(stat.st_mtime)
            rel_path = os.path.relpath(fpath, target_dir)
            size_kb = round(stat.st_size / 1024, 1)

            file_info = {
                "rel_path": rel_path,
                "full_path": fpath,
                "mtime": mtime_dt.isoformat(),
                "mtime_display": mtime_dt.strftime("%d/%m/%Y %H:%M:%S"),
                "size_kb": size_kb,
                "category": categorize_file(rel_path)
            }
            current_files[rel_path] = file_info

    return current_files

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Iniciando verificação em: {BASE_GLN_DIR}")
    state = load_state()
    prev_files = state.get("files", {})
    last_check_str = state.get("last_check", DEFAULT_CUTOFF.isoformat())
    last_check_dt = datetime.fromisoformat(last_check_str)

    current_files = scan_folder(BASE_GLN_DIR, last_check_dt)
    
    added_files = []
    updated_files = []

    for rel_path, info in current_files.items():
        mtime_dt = datetime.fromisoformat(info["mtime"])
        if rel_path not in prev_files:
            # Arquivo novo (ou nunca antes registrado e após a data de corte inicial)
            if mtime_dt >= DEFAULT_CUTOFF:
                added_files.append(info)
        else:
            prev_info = prev_files[rel_path]
            # Se data de modificação ou tamanho mudou
            if info["mtime"] != prev_info.get("mtime") or info["size_kb"] != prev_info.get("size_kb"):
                if mtime_dt >= DEFAULT_CUTOFF:
                    updated_files.append(info)

    print(f"Resumo da verificação:")
    print(f" - Arquivos novos detectados: {len(added_files)}")
    print(f" - Arquivos modificados detectados: {len(updated_files)}")

    if added_files or updated_files:
        now_display = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        report_lines = [
            f"# Relatório de Novos Arquivos e Modificações - Obra Estoril",
            f"\n*Gerado automaticamente em {now_display}*",
            f"\n**Diretório Monitorado:** `{BASE_GLN_DIR}`",
            f"\n**Data de Corte Considerada:** `{DEFAULT_CUTOFF.strftime('%d/%m/%Y %H:%M:%S')}`\n",
            f"## Resumo Executivo",
            f"- **Novos Arquivos:** {len(added_files)}",
            f"- **Arquivos Modificados:** {len(updated_files)}\n"
        ]

        # Agrupar por categoria
        all_changes = added_files + updated_files
        categories = {}
        for item in all_changes:
            cat = item["category"]
            categories.setdefault(cat, []).append(item)

        for cat, items in categories.items():
            report_lines.append(f"### {cat} ({len(items)})")
            for item in items:
                status_tag = "NOVO" if item in added_files else "MODIFICADO"
                report_lines.append(f"- `[{status_tag}]` **{os.path.basename(item['rel_path'])}** ({item['size_kb']} KB) - Modificado em: {item['mtime_display']}")
                report_lines.append(f"  - *Caminho:* `{item['rel_path']}`")
            report_lines.append("")

        with open(REPORT_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines))
        print(f"Relatório gerado em: {REPORT_FILE}")
    else:
        print("Nenhuma alteração detectada desde a última verificação.")

    # Atualiza o estado salvo
    new_state = {
        "last_check": datetime.now().isoformat(),
        "files": {k: {"mtime": v["mtime"], "size_kb": v["size_kb"], "category": v["category"]} for k, v in current_files.items()}
    }
    save_state(new_state)
    print(f"Estado salvo com sucesso em: {STATE_FILE}")

if __name__ == "__main__":
    main()
