class BayesianNetwork:
    def __init__(self):
        self.nodes = {}
    def add(self, var, parents, cpt):
        self.nodes[var] = {"parents": parents, "cpt": cpt}
    def prob(self, var, value, evidence):
        node = self.nodes[var]
        if not node["parents"]:
            return node["cpt"][value]
        parent_values = tuple(evidence[p] for p in node["parents"])
        return node["cpt"][parent_values][value]
    def joint_prob(self, evidence):
        p = 1.0
        for var in self.nodes:
            p *= self.prob(var, evidence[var], evidence)
        return p

bn = BayesianNetwork()
bn.add("Rain", [], {True: 0.2, False: 0.8})
bn.add("Sprinkler", ["Rain"], {
    (True,): {True: 0.01, False: 0.99},
    (False,): {True: 0.4, False: 0.6}
})
bn.add("GrassWet", ["Sprinkler", "Rain"], {
    (True, True): {True: 0.99, False: 0.01},
    (True, False): {True: 0.9, False: 0.1},
    (False, True): {True: 0.9, False: 0.1},
    (False, False): {True: 0.0, False: 1.0}
})

evidence = {"Rain": True, "Sprinkler": False, "GrassWet": True}
print("Joint Probability:", bn.joint_prob(evidence))
