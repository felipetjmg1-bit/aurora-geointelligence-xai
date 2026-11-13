"""AURORA GEOINTELLIGENCE COMMAND CENTER — CPU-first Gradio demo."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import gradio as gr
from aurora_geointelligence.core import run_analysis


def analyze(upload, n_clusters, index_type, band_a, band_b):
    if not upload:
        raise gr.Error("Envie uma imagem PNG, JPEG, TIFF ou GeoTIFF.")
    try:
        return run_analysis(
            upload,
            int(n_clusters),
            index_type or None,
            int(band_a) if band_a is not None else None,
            int(band_b) if band_b is not None else None,
        )
    except (ValueError, OSError) as exc:
        raise gr.Error(str(exc)) from exc
    except Exception as exc:  # keep UI errors legible; details remain in server logs
        print(f"Analysis failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise gr.Error("A análise falhou. Verifique o formato e os parâmetros da imagem.") from exc


with gr.Blocks(title="AURORA GEOINTELLIGENCE COMMAND CENTER", theme=gr.themes.Soft(primary_hue="emerald", secondary_hue="cyan"), analytics_enabled=False, css="""
.gradio-container {max-width: 1280px !important; margin: auto; background: #07111f; color: #e9f3fb}
#aurora-header {background: linear-gradient(115deg,#0b1c2b,#0c3440); border: 1px solid #17485a; border-radius: 18px; padding: 24px}
#aurora-header h1 {color:#f5fbff; margin-bottom: 6px}
#aurora-header p {color:#b4d4df; margin: 0}
footer {display:none !important}
""") as demo:
    gr.Markdown("""
    <div id="aurora-header">
      <h1>AURORA GEOINTELLIGENCE COMMAND CENTER</h1>
      <p>Sovereign Multimodal Earth Intelligence · MVP de pesquisa da Impulso Digital Soluções em I.A. Ltda.</p>
    </div>
    """)
    gr.Markdown("""
    **Transparência científica:** a segmentação padrão agrupa cores com MiniBatchKMeans e não atribui classes semânticas. O sistema não declara acurácia porque não há rótulos de referência. Índices espectrais só são calculados quando as bandas são selecionadas pelo pesquisador.
    """)
    with gr.Row():
        with gr.Column(scale=1):
            upload = gr.File(label="Imagem de entrada", file_types=[".png", ".jpg", ".jpeg", ".tif", ".tiff"], type="filepath")
            clusters = gr.Slider(2, 8, value=5, step=1, label="Número de grupos visuais (2–8)")
            index_type = gr.Dropdown(choices=["Nenhum", "NDVI", "NDWI"], value="Nenhum", label="Índice espectral opcional")
            with gr.Row():
                band_a = gr.Number(value=1, precision=0, label="Banda A (1-based)")
                band_b = gr.Number(value=2, precision=0, label="Banda B (1-based)")
            gr.Markdown("NDVI: A=NIR, B=vermelho. NDWI: A=verde, B=SWIR. A semântica não é inferida. Para RGB simples, mantenha “Nenhum”.")
            run = gr.Button("Executar análise", variant="primary")
        with gr.Column(scale=2):
            original = gr.Image(label="Pré-visualização da imagem", type="pil")
            overlay = gr.Image(label="Sobreposição de grupos visuais (não semânticos)", type="pil")
            index_view = gr.Image(label="Visualização do índice espectral (se solicitado)", type="pil")
            download = gr.File(label="Baixar pacote de resultados (JSON + PNG)")
            report = gr.Code(label="Relatório rastreável (JSON)", language="json", lines=18)
    run.click(analyze, inputs=[upload, clusters, index_type, band_a, band_b], outputs=[original, overlay, index_view, download, report])
    gr.Markdown("**Desenvolvido no Brasil pela Impulso Digital Soluções em I.A. Ltda.** · Projeto experimental; não é ferramenta de decisão ambiental validada.")

if __name__ == "__main__":
    demo.queue(default_concurrency_limit=2).launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", "7860")))
