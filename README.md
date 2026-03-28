# Suwit
### Ancient Indonesian Hand Game, Reimagined on GenLayer

Built for the **GenLayer Bradbury Hackathon** | AI Gaming Track

---

## What is Suwit?

Suwit (also known as Suwit-suwitan or Suit) is a traditional Indonesian hand game played by children across the archipelago — on streets, in schoolyards, during breaks. No equipment needed. Just your hands and a friend.

Like Rock Paper Scissors, but Indonesian:
- **Gajah (Elephant)** beats Manusia, loses to Semut
- **Manusia (Human)** beats Semut, loses to Gajah
- **Semut (Ant)** beats Gajah, loses to Manusia

The ant beats the elephant — because it crawls into the elephant's ear.

---

## Why GenLayer?

Regular blockchain smart contracts can only compare exact values. If Player 1 types "rock" and Player 2 types "Rock" — they might not even match.

GenLayer changes everything. Suwit on GenLayer lets players describe their move in **any language, any sentence**. The AI reads both descriptions, understands the intent, and judges the winner — all verified on-chain by multiple validators through the Equivalence Principle.

Player 1: *"aku mengangkat tangan seperti gajah besar yang kuat"*
Player 2: *"aku kecil seperti semut yang merayap"*

The AI correctly reads these Indonesian sentences, maps them to Gajah and Semut, and declares Player 2 the winner. On a blockchain. Trustlessly.

**This is only possible on GenLayer.**

---

## How It Works

1. Two players join the game with `join_game`
2. Each player submits their move as a natural language sentence with `submit_move`
3. Anyone calls `judge` — the AI reads both sentences and decides the winner
4. The result is verified by multiple AI validators through GenLayer's Optimistic Democracy consensus
5. Call `get_game_state` to read the result

---

## The Vision

This project started from a simple question: what happens when you take the oldest, simplest games from real life and bring them into the AI age?

Suwit has been played in Indonesia for generations. No rules written down, no referee needed — everyone just knows. Now, for the first time, a decentralized AI acts as the Hakim (judge), understanding natural human language and settling the outcome on-chain.

Built by a complete beginner from Indonesia with zero prior coding experience — to prove that GenLayer makes intelligent contracts accessible to everyone.

---

## Technical Details

- **Language:** Python (GenLayer SDK)
- **Consensus:** Optimistic Democracy with Equivalence Principle
- **AI Judge:** Uses `gl.eq_principle.prompt_comparative` for verifiable AI judgment
- **Network:** GenLayer Testnet Bradbury
- **Contract Address:** 0x2561c0aA901C87015929C7aAd94d2B9FD3c365d3

---

## Contract Methods

| Method | Type | Description |
|--------|------|-------------|
| `join_game(player_name)` | Write | Join the game as Player 1 or 2 |
| `submit_move(player_name, move_description)` | Write | Submit your move in natural language |
| `judge()` | Write | AI reads both moves and decides winner |
| `get_game_state()` | Read | Returns current game state and winner |
| `reset_game()` | Write | Reset for a new game |

---

## Built With

- [GenLayer Studio](https://studio.genlayer.com) — development and deployment
- [GenLayer SDK](https://sdk.genlayer.com) — intelligent contract framework
- [GenLayer Testnet Bradbury](https://testnet-faucet.genlayer.foundation) — live testnet

---

## Builder

**@Graziqt** — Indonesia
Built during the GenLayer Bradbury Hackathon, March 2026
