
predict(has_link(+protein, -protein)).

typed_language(yes).

type(has_annotation(protein, annotation)).
type(is_a(annotation, annotation)).
type(part_of(annotation, annotation)).
type(has_part(annotation, annotation)).
type(occurs_in(annotation, annotation)).
type(regulates(annotation, annotation)).


rmode(5: has_annotation(+Protein, +-Annotation)).
rmode(5: is_a(+Annotation, +-Annotation)).
rmode(5: part_of(+Annotation, +-Annotation)).
rmode(5: has_part(+Annotation, +-Annotation)).
rmode(5: occurs_in(+Annotation, +-Annotation)).
rmode(5: regulates(+Annotation, +-Annotation)).
    