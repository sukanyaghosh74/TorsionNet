from .concept_graph import ConceptGraph

graph = ConceptGraph('data/concepts.json', 'data/invalid_paths.json')

def check_torsion_violation(text):
    return graph.violates_torsion(text)
