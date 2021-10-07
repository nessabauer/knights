from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
knowledge0 = And(
    # A é Knight OU Knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # A says "I am both a knight and a knave."
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
knowledge1 = And(
    # A e B são Knight OU Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # A says "We are both knaves."
    Biconditional(AKnight, And(BKnave, AKnave))
    # B says nothing.
)

# Puzzle 2
knowledge2 = And(
    # A e B são Knight OU Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # A says "We are the same kind."
    Biconditional(AKnight, Or(And(BKnave, AKnave),And(BKnight, AKnight))),

    # B says "We are of different kinds."
    Biconditional(BKnight, Not(Or(And(BKnave, AKnave),And(BKnight, AKnight)))),

)

# Puzzle 3
knowledge3 = And(
    # A, B e C são Knight OU Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # B says "A said 'I am a knave'."
    Implication(BKnight, Implication(AKnight, BKnave)),
    Implication(BKnave, Implication(AKnave, BKnight)),

    # B says "C is a knave."
    Implication(BKnight,AKnave),
    Implication(BKnave,AKnight),

    # C says "A is a knight."
    Implication(CKnight,AKnight),
    Implication(CKnave,AKnave),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
