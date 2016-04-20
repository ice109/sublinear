import unittest
from graph import Graph
import random
from itertools import product


class GraphTest(unittest.TestCase):
    def testbfs(self):
        num_v = 10
        vertices = list(range(0, num_v))
        edges = random.sample(list(product(vertices, vertices)), 5*num_v)
        g = Graph(vertices, edges)
        vert_order = g.bfs()
        self.assertLessEqual(len(vert_order),len(vertices))

    def testavg_degree(self):
        num_v = 10
        connectivity = 5
        prob_correct = []
        for i in range(1000):
            vertices = list(range(0, num_v))
            edges = random.sample(list(product(vertices, vertices)), connectivity*num_v)
            # enforce minimum degree 1
            for i in range(num_v):
                edges.append((i, random.choice(range(num_v))))
            g = Graph(vertices, edges)
            err = .5
            est = g.avg_deg(err, 1)
            prob_correct.append((1-err)*est <= connectivity <= (1+err)*est)

        self.assertGreaterEqual(sum(map(int,prob_correct))/len(prob_correct),.6)

if __name__ == '__main__':
    unittest.main()