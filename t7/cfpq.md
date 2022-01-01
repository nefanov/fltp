Let Σ be a finite set of edge labels. Define an edge-labeled directed graph as a tuple D = (V,E) with a set of nodes V and a directed edge relation E ⊆ V × Σ × V.
A path π is a list of labeled edges [e1,...,en] wheree i ∈ E. The concatenation of a path π1 with a path π2 we denote by π1 + π2.
For a path π in a graph D, we denote the unique word, obtained by concatenating the labels of the edges along the path π as l(π). Also, we write nπm to indicate, that the path π starts at the node n ∈ V and ends at the node m ∈ V.
A context-free grammar is a triple G = (N , Σ, P ), where N is a finite set of non-terminals, Σ is a finite set of terminals, and P is a finite set of productions of the following forms:
• A → BC,forA,B,C ∈N,
• A → x, for A ∈ N and x ∈ Σ ∪ {ε}.
∗ We use the conventional notation A⇒_{G} w to denote,that a G string w ∈ Σ∗ can be derived from a non-terminal A by some sequence of production rule applications from P in grammar G. The language of a grammar G with respect to a start non-terminal S ∈ N is defined by L(GS)={w∈Σ∗|S⇒=∗w}. G
For a given graph D = (V , E) and a context-free grammar G=(N,Σ,P),we define context-free relations R_A ⊆ V × V for every A ∈ N, such that R_A = {(n,m)|∃nπm(l(π) ∈ L(G_A))}.
