# [CLUE] Conventional Current vs. Electron Flow (battery terminals, anode/cathode, which way current "flows")
> Cover everything below and lecture it from memory.
> (From Altius FLE 1 CPF Q13 — "which part acts as the positive terminal?" Missed: picked the electrode where electrons *enter* the load (the − terminal) instead of the one current is pushed out of. Physics.)

- **The one sentence that fixes it:** electrons flow **− → +** (out of the negative terminal, through the external circuit, into the positive terminal); **conventional current flows the OPPOSITE way, + → −**.
  - Note: current was defined (Ben Franklin) as the flow of *positive* charge before electrons were known. Electrons are actually what move, and they're negative, so real electron motion is backwards from "current." Everything below is just bookkeeping around that one flip.

- **Electron flow (what actually moves in a wire)**
  - Inside the external circuit (wires/load), electrons travel **from the − terminal → to the + terminal**.
  - i.e. electrons *leave* the negative terminal, do work in the load, and *arrive* at the positive terminal.
  - Note: negative charge is *repelled* by the negative terminal and *attracted* to the positive one — so electrons run away from − toward +.

- **Conventional current I (what you use for every formula)**
  - Defined as the flow of **positive** charge → points **opposite** to electron motion.
  - Through the external circuit, current flows **from the + terminal → to the − terminal**.
  - Current is **"pushed out of" the + terminal** and **returns into the − terminal**.
  - Note: I = ΔQ/Δt. Every circuit rule (V=IR, right-hand rule, power) assumes *conventional* current, not electron flow. Always convert electron flow → flip the arrow → that's I.

- **How to nail the terminals from an electron-flow diagram (the Q13 method)**
  1. Find the electron loop through the external circuit (the passage/figure usually draws it).
  2. Electrons **leave** one electrode → that electrode is the **negative (−) terminal**.
  3. Electrons **enter** the other electrode → that electrode is the **positive (+) terminal**.
  4. Conventional current = flip the electron arrow: current is *pushed out of* the + terminal.
  - Q13 worked: electrons leave the bottom F:SnO₂ electrode and go up through the load ⇒ bottom = **− terminal**. They enter the top Pt/F:SnO₂ electrode ⇒ top = **+ terminal** (correct answer). Her trap: she called the electrode where electrons *exit into the load* the positive terminal — it's the negative one.
  - Note: "the terminal current comes *out of* = positive" is the fastest check. Or: "where electrons pile *in* = positive."

- **Anode vs. cathode (the reliable rule that survives batteries AND electrolysis)**
  - **Anode = where OXIDATION happens** (loses electrons). **Cathode = where REDUCTION happens** (gains electrons).
    - Mnemonic: **AN OX** (ANode = OXidation) and **RED CAT** (REDuction = CAThode).
  - **Current** always: flows *into* the anode from the external circuit and *out of* the cathode... **inside the cell**, current goes anode → cathode is reversed depending on cell type, so DON'T memorize terminal signs to anode/cathode. Use ox/red.
  - **Sign of the terminal depends on cell type** — this is the classic trap:
    - **Galvanic / voltaic cell (a battery discharging, spontaneous):** anode is **−**, cathode is **+**.
    - **Electrolytic cell (driven by external power, non-spontaneous):** anode is **+**, cathode is **−**.
  - Note: mnemonic that *always* holds regardless of cell type — **electrons always flow anode → cathode through the external wire** (oxidation releases them at the anode, reduction consumes them at the cathode). So find where ox/red happen first, then read off electron direction.

- **Putting it together for a discharging battery / this solar cell (galvanic-type)**
  - Anode (oxidation) = **− terminal** → electrons exit here → travel through load → into cathode.
  - Cathode (reduction) = **+ terminal** → electrons enter here.
  - Conventional current: out of the **+** (cathode), through the load, back into the **−** (anode).

- **Gotchas**
  - Don't map "anode = negative" as a universal fact — it flips between galvanic and electrolytic cells. **Ox/red is the invariant; terminal sign is not.**
  - A distractor electrode ("the nanowires also release electrons!") isn't a terminal if the passage explicitly names the two electrodes — read the stem's definition (Q13 choice D trap).
  - When a problem gives electron flow, **flip the arrow** before using any current formula.
  - Note: neighbor concepts — [[hydrostatic-pressure]] is unrelated; future sheets: I = ΔQ/Δt & sign conventions, capacitance (C = ε₀A/d, from Q15).
