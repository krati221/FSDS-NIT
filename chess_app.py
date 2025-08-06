import streamlit as st
import chess
import chess.svg
from io import StringIO
import base64

# Helper to render chess board as SVG in Streamlit
def render_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
    return f'<img src="data:image/svg+xml;base64,{b64}"/>'

# Initialize session state
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()
if 'move_history' not in st.session_state:
    st.session_state.move_history = []

st.title("Chess Game with Streamlit")

# Show the board
board_svg = chess.svg.board(st.session_state.board, size=400)
st.markdown(render_svg(board_svg), unsafe_allow_html=True)

# Move input
st.write("Enter your move in UCI format (e.g., e2e4):")
move_input = st.text_input("Move", "")

if st.button("Make Move"):
    try:
        move = chess.Move.from_uci(move_input)
        if move in st.session_state.board.legal_moves:
            st.session_state.board.push(move)
            st.session_state.move_history.append(move_input)
        else:
            st.error("Illegal move!")
    except Exception as e:
        st.error(f"Invalid move format: {e}")

# Show move history
st.write("Move History:")
st.write(st.session_state.move_history)

# Show game status
if st.session_state.board.is_checkmate():
    st.success("Checkmate!")
elif st.session_state.board.is_stalemate():
    st.info("Stalemate!")
elif st.session_state.board.is_check():
    st.warning("Check!")

if st.button("Reset Game"):
    st.session_state.board = chess.Board()
    st.session_state.move_history = []