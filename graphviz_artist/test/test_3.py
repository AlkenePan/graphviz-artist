import graphviz_artist as ga
import graphviz_artist.attr as attr

# make a graph
g = ga.Graph(directed=True)

new = g.new

# decl nodes
false = new(attr.Label("False"))
true = new(attr.Label("True"))
not_ = new(attr.Label("not"))
and_ = new(attr.Label("and"))

unary1 = new(attr.Label("unary"))
unary2 = new(attr.Label("unary"))
binary = new(attr.Label("binary"), attr.Width(2), attr.Shape.box)
expr = new(attr.Label("expr"))

# build graph
_ = false > unary1 < not_
_ = true > unary2

_ = and_[attr.Label('Op')] > binary

# XLabel: For edges, the label will be placed near the center of the edge.
_ = unary1[attr.XLabel("Left operand")] > binary
_ = unary2[attr.XLabel('Right operand')] > binary
_ = binary > expr

g.save()

assert """digraph {
	0 [label=False]
	1 [label=True]
	2 [label=not]
	3 [label=and]
	4 [label=unary]
	5 [label=unary]
	6 [label=binary shape=box width=2]
	7 [label=expr]
	0 -> 4 [dir=forward]
	2 -> 4 [dir=forward]
	1 -> 5 [dir=forward]
	3 -> 6 [label=Op dir=forward]
	4 -> 6 [dir=forward xlabel="Left operand"]
	5 -> 6 [dir=forward xlabel="Right operand"]
	6 -> 7 [dir=forward]
}""" == str(g.g)