import os
import html

def make_info_card():
    # User details
    details = [
        ("Role", "Senior Software Developer"),
        ("Stack", "Javascript, react, next, angular, nodejs, python"),
        ("     ", "mongobd, mysql, postgres, AI-augumented")
    ]
    
    width = 490
    height = 387  # Matches the height of wordmark/portrait usually
    titlebar_h = 28
    pad = 18
    
    bg = "#0d1117"
    bg2 = "#111722"
    frame = "#30363d"
    title_text = "#7d8590"
    ink = "#c9d1d9"
    key_color = "#58a6ff"
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        f'<defs><linearGradient id="wbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{bg2}"/><stop offset="1" stop-color="{bg}"/></linearGradient></defs>',
        f'<rect width="{width}" height="{height}" rx="12" fill="url(#wbg)"/>',
        f'<rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="12" fill="none" stroke="{frame}" stroke-width="1"/>',
        f'<line x1="0" y1="{titlebar_h}" x2="{width}" y2="{titlebar_h}" stroke="{frame}"/>',
    ]
    
    for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        svg.append(f'<circle cx="{pad + i*15}" cy="{titlebar_h/2}" r="4.5" fill="{dot}"/>')
        
    svg.append(f'<text x="{width/2}" y="{titlebar_h/2 + 4}" fill="{title_text}" font-size="11.5" text-anchor="middle">i-am-harshit@github: ~</text>')
    
    y = titlebar_h + 30
    delay = 0.5
    for key, val in details:
        y += 24
        anim = f'<animate attributeName="opacity" from="0" to="1" begin="{delay}s" dur="0.5s" fill="freeze"/>'
        anim += f'<animate attributeName="y" from="{y+10}" to="{y}" begin="{delay}s" dur="0.5s" fill="freeze"/>'
        
        svg.append(f'<g opacity="0">{anim}')
        if key.strip():
            svg.append(f'<text x="{pad}" y="{y}" fill="{key_color}" font-weight="bold" font-size="14">{key}</text>')
            svg.append(f'<text x="{pad + 60}" y="{y}" fill="{ink}" font-size="14">: {html.escape(val)}</text>')
        else:
            svg.append(f'<text x="{pad + 60}" y="{y}" fill="{ink}" font-size="14">  {html.escape(val)}</text>')
        svg.append('</g>')
        
        delay += 0.3
        
    svg.append("</svg>")
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "info-card.svg")
    with open(out_path, "w") as f:
        f.write("\n".join(svg))
    print(f"wrote {out_path}")

if __name__ == "__main__":
    make_info_card()
