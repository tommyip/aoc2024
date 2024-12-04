&fras "inputs/day04.txt"

R  ← ⍥(≡⇌⍉)⇡4¤
D  ← ⊡⍉⊟.⇡⊸⧻
P₁ ← ⬚@ ⧈(≡(≍"XMAS")⊂≡⊃D⊢R)4_4
P₂ ← ⧈(=2/+≡(≍"MAS"D)R)3_3
∩(/+♭)⊃P₂P₁⊜∘⊸≠@\n
