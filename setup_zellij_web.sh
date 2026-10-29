#!/bin/bash
# ==============================================================================
# ECO-360 PHYXITAL SOLUTIONS — ENTORNO ZELLIJ DEDICADO DESARROLLO WEB
# ==============================================================================

echo "🚀 Configurando entorno Zellij exclusivo para el Portal Web ECO-360..."

# 1. Directorio Raíz de trabajo
WEB_DIR="$HOME/eco360-phyxital.github.io"
if [ ! -d "$WEB_DIR" ]; then
    mkdir -p "$WEB_DIR"
fi
cd "$WEB_DIR" || exit 1

# 2. Alias útiles para la consola
alias web-edit="emacs -nw mapa.html"
alias web-serve="python3 -m http.server 8080"
alias web-map="python3 ./map_console_viewer.py"
alias web-push="git add index.html mapa.html mapa_nodos_eco360.geojson && git commit -m 'feat(web): actualiza portal y mapa 3d' && git push origin main"
alias web-status="git status && git log -n 3 --oneline"

# 3. Copiar recursos si no existen
if [ -f "/workspace/artifacts/mapa_nodos_eco360.geojson" ]; then
    cp /workspace/artifacts/mapa_nodos_eco360.geojson ./
fi

if [ -f "/workspace/artifacts/map_console_viewer.py" ]; then
    cp /workspace/artifacts/map_console_viewer.py ./
fi

# 4. Iniciar sesión Zellij dedicada
echo "✨ Iniciando Zellij con el layout 'layout_web_eco360.kdl'..."
zellij --layout ./layout_web_eco360.kdl attach --create web_eco360
