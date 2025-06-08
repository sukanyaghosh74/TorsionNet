import json
import networkx as nx

class ConceptGraph:
    def __init__(self, concept_path, invalid_path):
        with open(concept_path) as f:
            self.concepts = json.load(f)
        with open(invalid_path) as f:
            self.invalid_paths = json.load(f)

        self.graph = nx.Graph()
        self.build_graph()

    def build_graph(self):
        for group in self.concepts.values():
            for concept in group:
                self.graph.add_node(concept)
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    self.graph.add_edge(group[i], group[j])

    def violates_torsion(self, sentence):
        words = sentence.split()
        for path in self.invalid_paths:
            if all(p in words for p in path):
                return True
        return False
