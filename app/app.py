# coding=utf-8

import typefx.typefx as _typefx

def main():
    """Print out results
    """
    LINES = [
        u"/* I am a boy named Lei Ma. I don't have a girlfriend. */",
        u"Boy i = new Boy('Lei Ma');",
        u"Girl u = null;",
        u"i.state = |Single> ⊗ |Boy>",
        u"",
        u"/* The Hamiltonian that descibes my evloution is */",
        u"/* a function of the Single state */",
        u"i.Hamiltonian = function(|Single>)",
        u"/* Obviously this Hamiltonian commutes with my state ... */",
        u"[ i.Hamiltonian, i.ρ ] = 0",
        u"",
        u"/* The dynamics of me becomes so simple and lonely ... */",
        u"∂t i.ρ = 0",
        u"",
        u"/* And I am not complete */",
        u"I ! = tensorProduct(i.gender, i.gender*)",
        u"",
        u"/* A single girl Hamiltonian added to mine makes a new Hamiltonian */",
        u"/* which will evolve both us to non-single states */",
        u"[ i.Hamiltonian + u.Hamiltonian + interaction(u, i), i.ρ + u.ρ ] != 0",
        u"u.ρ(tf) = tensorProduct(inLove, inLove*)",
        u"i.ρ(tf) = tensorProduct(inLove, inLove*)",
        u"",
        u"/* And we two will be complete */",
        u"/* |Boy > < Boy| + |Girl > < Girl| is complete */",
        u"I = tensorProduct(i.gender, i.gender) + tensorProduct(u.gender, u.gender)",
        u"",
        u"/* What's more, the following statement returns True */",
        u"i.sex + u.sex == sex",
        u"",
        u"/* So talk to me */",
        u"i.address = http://openmetric.org"
    ]

    for line in LINES:
        _typefx.dynamic(line)
        print('\n')


if __name__ == "__main__":
    main()
    print('END OF GAME')