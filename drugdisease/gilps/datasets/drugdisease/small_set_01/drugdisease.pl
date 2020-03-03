:- modeh(1, treats(+drug, -disease)).
:- modeb(*, targets(+drug, -gene)).
:- modeb(*, relatesto(+gene, -disease)).

targets('DB00143','Q03013').
targets('DB00151','Q9HA77').
targets('DB00157','Q13630').
targets('DB00227','P20701').
targets('DB00396','P05093').
targets('DB00543','P14867').
targets('DB00907','Q9UI33').
targets('DB01436','O15528').
targets('DB01593','P31151').
targets('DB02073','P09601').

relatesto('O15528','MESH:D009135').
relatesto('P05093','MESH:D003928').
relatesto('P09601','MESH:D012751').
relatesto('P14867','MESH:D016535').
relatesto('P20701','MESH:D009422').
relatesto('P31151','MESH:D009765').
relatesto('Q03013','MESH:D012206').
relatesto('Q13630','MESH:D002386').
relatesto('Q9HA77','MESH:D019048').
relatesto('Q9UI33','MESH:D011596').

example(treats('DB00143','MESH:D012206'), 1).
example(treats('DB00151','MESH:D019048'), 1).
example(treats('DB00157','MESH:D002386'), 1).
example(treats('DB00227','MESH:D009422'), 1).
example(treats('DB00396','MESH:D003928'), 1).
example(treats('DB00543','MESH:D016535'), 1).
example(treats('DB00907','MESH:D011596'), 1).
example(treats('DB01436','MESH:D009135'), 1).
example(treats('DB01593','MESH:D009765'), 1).
example(treats('DB02073','MESH:D012751'), 1).

example(treats('DB00907','MESH:D019048'), -1).
example(treats('DB00907','MESH:D002386'), -1).
example(treats('DB00907','MESH:D016535'), -1).
example(treats('DB00907','MESH:D009135'), -1).
example(treats('DB00907','MESH:D009422'), -1).
example(treats('DB00907','MESH:D009765'), -1).
example(treats('DB00907','MESH:D012751'), -1).
example(treats('DB00907','MESH:D012206'), -1).
example(treats('DB00907','MESH:D003928'), -1).
example(treats('DB00151','MESH:D011596'), -1).
