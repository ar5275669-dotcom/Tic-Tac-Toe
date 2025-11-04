import streamlit as st

# Page setup
st.set_page_config(page_title="Tic Tac Toe", page_icon="❌", layout="centered")
st.title("🎮 Tic Tac Toe")
st.caption("Play a simple two-player Tic Tac Toe game!")

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# Function to check for a winner
def check_winner(board):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combos:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Function to handle a move
def make_move(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.current_player
        winner = check_winner(st.session_state.board)
        if winner:
            st.session_state.winner = winner
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Game grid UI
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        with cols[j]:
            if st.button(st.session_state.board[index] or " ", key=index, use_container_width=True):
                make_move(index)

# Show game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("🤝 It's a draw!")
    else:
        st.success(f"🏆 Player {st.session_state.winner} wins!")
else:
    st.markdown(f"**Player {st.session_state.current_player}'s turn**")

# Restart button
if st.button("🔁 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.experimental_rerun()
