import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="Rifa do Casamento — Rafael & Maria Luiza",
    page_icon="💍",
    layout="centered"
)

# ── CONFIG ────────────────────────────────────────────────────────────────────
PIX_KEY    = "malupertence@gmail.com"
VALOR      = "R$ 15,00"
TOTAL_NUMS = 1200
ADMIN_PWD  = "1234"
DATA_FILE  = "reservas.json"

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ── STYLE ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Jost', sans-serif;
    background-color: #FFFFFF;
    color: #3D4A35;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 700px;
}

h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 300 !important;
    color: #3D4A35 !important;
    text-align: center;
}

.hero {
    text-align: center;
    padding: 10px 0 20px;
}

.hero-date {
    font-family: 'Jost', sans-serif;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #6B7566;
    margin-bottom: 4px;
}

.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    font-weight: 300;
    letter-spacing: 0.08em;
    color: #3D4A35;
    line-height: 1.1;
}

.hero-sub {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.1rem;
    color: #6B7566;
    margin-top: 6px;
}

.divider {
    text-align: center;
    color: #C8B99A;
    font-size: 1rem;
    margin: 20px 0;
    letter-spacing: 0.5em;
}

.stat-box {
    background: #FFFFFF;
    border: 1px solid #E8DDD0;
    padding: 16px;
    text-align: center;
    border-radius: 0;
}

.stat-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.8rem;
    color: #6B7F5E;
    display: block;
}

.stat-label {
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #6B7566;
}

.prize-card {
    background: #F7F4EF;
    border: 1px solid #E8DDD0;
    padding: 24px;
    text-align: center;
    margin: 16px 0;
}

.prize-val {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    font-weight: 300;
    color: #6B7F5E;
}

.prize-label {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #6B7566;
    margin-top: 4px;
}

.num-disponivel {
    background: #fff;
    border: 1px solid #E8DDD0;
    color: #3D4A35;
    padding: 6px 4px;
    text-align: center;
    font-size: 0.75rem;
    cursor: pointer;
    font-family: 'Jost', sans-serif;
}

.num-reservado {
    background: #E8DDD0;
    border: 1px solid #E8DDD0;
    color: #aaa;
    padding: 6px 4px;
    text-align: center;
    font-size: 0.75rem;
    font-family: 'Jost', sans-serif;
}

.num-pago {
    background: #C5D0BB;
    border: 1px solid #C5D0BB;
    color: #fff;
    padding: 6px 4px;
    text-align: center;
    font-size: 0.75rem;
    font-family: 'Jost', sans-serif;
}

.pix-card {
    background: #F7F4EF;
    border: 1px solid #E8DDD0;
    padding: 24px;
    text-align: center;
    margin-top: 20px;
}

.pix-key {
    font-family: 'Jost', sans-serif;
    font-size: 1rem;
    background: #fff;
    border: 1px solid #E8DDD0;
    padding: 10px 16px;
    margin: 12px 0;
    word-break: break-all;
}

.label-small {
    font-size: 0.68rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #6B7F5E;
    text-align: center;
    display: block;
    margin-bottom: 4px;
}

/* Fixed leaves on sides */
[data-testid="stAppViewContainer"] {
    background-image: url('https://raw.githubusercontent.com/malupertence-creator/rifa-casamento/main/folhas%20esquerdo.png'),
                      url('https://raw.githubusercontent.com/malupertence-creator/rifa-casamento/main/folhas%20direito.png');
    background-position: left top, right top;
    background-repeat: no-repeat, no-repeat;
    background-size: 13vw 100%, 13vw 100%;
    background-attachment: fixed, fixed;
}

/* hide streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* button style */
.stButton > button {
    background-color: #6B7F5E !important;
    color: white !important;
    border: none !important;
    border-radius: 0 !important;
    font-family: 'Jost', sans-serif !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    padding: 12px 32px !important;
    width: 100%;
}
.stButton > button:hover {
    background-color: #3D4A35 !important;
}

/* input style */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div {
    border-radius: 0 !important;
    border-color: #E8DDD0 !important;
    font-family: 'Jost', sans-serif !important;
}

.stTextInput > label,
.stNumberInput > label,
.stSelectbox > label {
    font-size: 0.7rem !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    color: #6B7566 !important;
}

div[data-testid="stTab"] button {
    font-family: 'Jost', sans-serif !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    font-size: 0.75rem !important;
}
</style>
""", unsafe_allow_html=True)

# ── LOAD ──────────────────────────────────────────────────────────────────────
data = load_data()
reservados = {int(k): v for k, v in data.items()}
total_reservados = len(reservados)
total_disponiveis = TOTAL_NUMS - total_reservados

# ── HERO ──────────────────────────────────────────────────────────────────────
# Hero layout with leaves
left_col, center_col, right_col = st.columns([1, 3, 1])

with left_col:
    try:
        st.image("folhas esquerdo.png", use_container_width=True)
    except:
        pass

with center_col:
    try:
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.image("hero.png", use_container_width=True)
    except:
        pass
    st.markdown("""
<div class="hero">
  <div class="hero-date">02 · 10 · 2027</div>
  <div class="hero-title" style="white-space:nowrap;font-size:clamp(1.4rem,3.5vw,2.6rem);">RAFAEL & MARIA LUIZA</div>
  <div class="hero-sub">Participe e ajude a celebrar o nosso amor</div>
</div>
""", unsafe_allow_html=True)
    try:
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.image("casal.png", use_container_width=True)
    except:
        pass

with right_col:
    try:
        st.image("folhas direito.png", use_container_width=True)
    except:
        pass

# ── DIVIDER ───────────────────────────────────────────────────────────────────
st.markdown('<div class="divider">— ✦ —</div>', unsafe_allow_html=True)

# ── COMO FUNCIONA ─────────────────────────────────────────────────────────────
st.markdown('<span class="label-small">Como funciona</span>', unsafe_allow_html=True)
st.markdown('<h2>Cada número é uma chance de ganhar</h2>', unsafe_allow_html=True)
st.markdown("""
<p style="text-align:center;color:#6B7566;font-size:0.92rem;line-height:1.8;">
Escolha um ou mais números, faça o pagamento via PIX e torça muito.<br>
O sorteio acontece no dia do nosso casamento.
</p>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="prize-card">
  <div class="prize-val">{VALOR}</div>
  <div class="prize-label">por número · pagamento via PIX</div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="stat-box"><span class="stat-num">{TOTAL_NUMS}</span><span class="stat-label">números totais</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="stat-box"><span class="stat-num">{total_disponiveis}</span><span class="stat-label">disponíveis</span></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="stat-box"><span class="stat-num">{total_reservados}</span><span class="stat-label">reservados</span></div>', unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
aba1, aba2 = st.tabs(["✦  Participar", "✦  Administração"])

# ── ABA PARTICIPAR ────────────────────────────────────────────────────────────
with aba1:
    st.markdown('<div class="divider">— ✦ —</div>', unsafe_allow_html=True)
    st.markdown('<span class="label-small">Escolha seu número</span>', unsafe_allow_html=True)
    st.markdown('<h2>Reserve agora</h2>', unsafe_allow_html=True)

    # Busca
    busca = st.number_input("Buscar número (1 a 1200)", min_value=1, max_value=TOTAL_NUMS, value=None, placeholder="Ex: 42")

    # Legenda
    st.markdown("""
    <div style="display:flex;gap:16px;flex-wrap:wrap;font-size:0.72rem;color:#6B7566;margin:8px 0 12px;">
      <span><span style="display:inline-block;width:12px;height:12px;background:#fff;border:1px solid #E8DDD0;margin-right:5px;vertical-align:middle;"></span>Disponível</span>
      <span><span style="display:inline-block;width:12px;height:12px;background:#E8DDD0;margin-right:5px;vertical-align:middle;"></span>Reservado</span>
      <span><span style="display:inline-block;width:12px;height:12px;background:#C5D0BB;margin-right:5px;vertical-align:middle;"></span>Pago</span>
    </div>
    """, unsafe_allow_html=True)

    # Grid
    cols_per_row = 10
    start = max(1, (busca - 5)) if busca else 1
    end = min(TOTAL_NUMS + 1, start + 200)

    grid_html = '<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:4px;max-height:300px;overflow-y:auto;margin-bottom:16px;">'
    for n in range(1, TOTAL_NUMS + 1):
        num_str = str(n).zfill(4)
        if n in reservados:
            status = reservados[n].get("status", "")
            if status == "pago":
                grid_html += f'<div class="num-pago">{num_str}</div>'
            else:
                grid_html += f'<div class="num-reservado">{num_str}</div>'
        else:
            grid_html += f'<div class="num-disponivel">{num_str}</div>'
    grid_html += '</div>'
    st.markdown(grid_html, unsafe_allow_html=True)

    # Seleção
    disponiveis = [n for n in range(1, TOTAL_NUMS + 1) if n not in reservados]

    if not disponiveis:
        st.warning("Todos os números já foram reservados.")
    else:
        numero = st.selectbox(
            "Número escolhido",
            disponiveis,
            format_func=lambda x: str(x).zfill(4),
            index=0 if not busca else (disponiveis.index(busca) if busca in disponiveis else 0)
        )
        nome = st.text_input("Seu nome completo")
        whatsapp = st.text_input("WhatsApp", placeholder="(11) 99999-9999")

        if st.button("RESERVAR NÚMERO"):
            if not nome or not whatsapp:
                st.error("Preencha seu nome e WhatsApp.")
            elif numero in reservados:
                st.error("Este número já foi reservado. Escolha outro.")
            else:
                reservados[numero] = {
                    "nome": nome,
                    "whatsapp": whatsapp,
                    "status": "aguardando pagamento",
                    "data": datetime.now().strftime("%d/%m/%Y %H:%M")
                }
                save_data({str(k): v for k, v in reservados.items()})
                st.success(f"✓ Número {str(numero).zfill(4)} reservado! Agora faça o pagamento via PIX.")
                st.markdown(f"""
                <div class="pix-card">
                  <div style="font-size:0.7rem;letter-spacing:0.25em;text-transform:uppercase;color:#6B7F5E;margin-bottom:6px;">Pagamento</div>
                  <h3 style="margin-bottom:8px;">Pague via PIX</h3>
                  <p style="font-size:0.85rem;color:#6B7566;">Após pagar, envie o comprovante via WhatsApp para confirmação.</p>
                  <div class="pix-key">{PIX_KEY}</div>
                  <p style="font-size:0.78rem;color:#6B7566;margin-top:12px;">Valor: <strong>{VALOR}</strong></p>
                </div>
                """, unsafe_allow_html=True)
                st.rerun()

# ── ABA ADMIN ─────────────────────────────────────────────────────────────────
with aba2:
    st.markdown('<div class="divider">— ✦ —</div>', unsafe_allow_html=True)
    st.markdown('<span class="label-small">Área restrita</span>', unsafe_allow_html=True)
    st.markdown('<h2>Administração</h2>', unsafe_allow_html=True)

    if "admin_ok" not in st.session_state:
        st.session_state.admin_ok = False

    if not st.session_state.admin_ok:
        senha = st.text_input("Senha de acesso", type="password")
        if st.button("ENTRAR"):
            if senha == ADMIN_PWD:
                st.session_state.admin_ok = True
                st.rerun()
            else:
                st.error("Senha incorreta.")
    else:
        st.success("Acesso liberado.")

        filtro = st.selectbox("Filtrar por status", ["Todos", "aguardando pagamento", "pago", "cancelado"])

        if not reservados:
            st.info("Nenhuma reserva ainda.")
        else:
            for num, info in sorted(reservados.items()):
                if filtro != "Todos" and info.get("status") != filtro:
                    continue
                status = info.get("status", "")
                emoji = "⏳" if status == "aguardando pagamento" else "✅" if status == "pago" else "❌"
                with st.expander(f"{emoji} Nº {str(num).zfill(4)} — {info['nome']}"):
                    st.write(f"**WhatsApp:** {info['whatsapp']}")
                    st.write(f"**Status:** {status}")
                    st.write(f"**Data:** {info.get('data', '—')}")
                    col1, col2 = st.columns(2)
                    with col1:
                        if status != "pago" and st.button(f"✅ Confirmar pagamento", key=f"confirm_{num}"):
                            reservados[num]["status"] = "pago"
                            save_data({str(k): v for k, v in reservados.items()})
                            st.rerun()
                    with col2:
                        if st.button(f"❌ Cancelar reserva", key=f"cancel_{num}"):
                            del reservados[num]
                            save_data({str(k): v for k, v in reservados.items()})
                            st.rerun()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:40px 0 20px;font-size:0.72rem;letter-spacing:0.15em;text-transform:uppercase;color:#C8B99A;">
  Rafael & Maria Luiza · 02.10.2027 · Feito com amor 🤍
</div>
""", unsafe_allow_html=True)
