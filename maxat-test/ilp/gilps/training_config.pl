:- use_module('source/gilps').
:- set(verbose, 1).

drugdisease :-
	read_problem('datasets/train_17:19'),
	set(output_theory_file, 'models/train_17:19').

drugdisease_yeast_go :-
	read_problem('datasets/yeast/train_yeast_go'),
	set(output_theory_file, 'models/train_yeast_go').

drugdisease_human_go :-
	read_problem('datasets/human/train_human_go'),
	set(output_theory_file, 'models/train_human_go').

%:- drugdisease_human_go.
:- drugdisease_yeast_go.

:-build_theory.
