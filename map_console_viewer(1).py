#!/usr/bin/env python3
import json
import os
import sys

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[38;2;0;240;255m"      # #00F0FF
GREEN = "\033[38;2;0;230;165m"     # #00E6A5
RED = "\033[38;2;255;0;127m"       # #FF007F
GOLD = "\033[38;2;255;215;0m"      # #FFD700
PURPLE = "\033[38;2;189;147;249m"  # #BD93F9

GEOJSON_PATH = "./mapa_nodos_eco360.geojson"
if not os.path.exists(GEOJSON_PATH):
    GEOJSON_PATH = "/workspace/artifacts/mapa_nodos_eco360.geojson"

def render_map():
    if not os.path.exists(GEOJSON_PATH):
        print(f"{RED}Error: No se encontró {GEOJSON_PATH}{RESET}")
        return

    with open(GEOJSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    features = data.get("features", [])
    
    lats = [f["geometry"]["coordinates"][1] for f in features]
    lons = [f["geometry"]["coordinates"][0] for f in features]
    
    min_lat, max_lat = min(lats), max(lats)
    min_lon, max_lon = min(lons), max(lons)
    
    width = 54
    height = 16
    grid = [[" " for _ in range(width)] for _ in range(height)]
    
    for f in features:
        lon, lat = f["geometry"]["coordinates"]
        props = f["properties"]
        cat = props.get("categoria", "otros")
        
        x = int((lon - min_lon) / (max_lon - min_lon + 1e-6) * (width - 1))
        y = int((max_lat - lat) / (max_lat - min_lat + 1e-6) * (height - 1))
        
        char = "●"
        color = CYAN
        if cat == "gobierno": color = CYAN; char = "🏛"
        elif cat == "espera_publica": color = GOLD; char = "⏳"
        elif cat == "fincas": color = GREEN; char = "🍇"
        elif cat == "vecinal": color = RED; char = "🏘"
        elif cat == "simulacion": color = PURPLE; char = "🎭"
        elif cat == "ciencia_cordillera": color = BOLD + CYAN; char = "🏔"
            
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = f"{color}{char}{RESET}"

    print(f"\n{BOLD}{CYAN}=============================================================={RESET}")
    print(f"{BOLD}{GOLD}  🌐 VISOR TERMINAL INTERACTIVO — MAPA DE NODOS ECO-360 PHYXITAL{RESET}")
    print(f"{BOLD}{CYAN}=============================================================={RESET}")
    print(f" Nodos Activos: {BOLD}{len(features)}{RESET} | Ubicación: {BOLD}San Rafael & Distritos{RESET}\n")

    print("┌" + "─" * width + "┐")
    for row in grid:
        print("│" + "".join(row) + "│")
    print("└" + "─" * width + "┘")
    
    print(f"\n{BOLD}Categorías y Simulación:{RESET}")
    print(f" {CYAN}🏛 Gobierno{RESET} | {GOLD}⏳ Espera (EcoQ){RESET} | {GREEN}🍇 Fincas{RESET} | {RED}🏘 Vecinal{RESET} | {PURPLE}🎭 Avatares Live{RESET}")
    print(f"\n{BOLD}Últimos Eventos de Telemetría (Live Feed):{RESET}")
    print(f" {GREEN}[15:42:01] Node_01 Búnker:{RESET} Loopback OK (127.0.0.1, 0 dB)")
    print(f" {GOLD}[15:42:04] EE-01 Registro Civil:{RESET} Módulo EcoQ Activo (Turnero Fluido)")
    print(f" {PURPLE}[15:42:08] Avatar UbicaPet:{RESET} Perro 'Choco' en Rango BLE (Correa Invisible OK)\n")

if __name__ == "__main__":
    render_map()
