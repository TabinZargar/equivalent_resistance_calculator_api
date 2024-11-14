# api/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
import numpy as np

@api_view(['POST'])
def calculate_resistance(request):
    try:
        circuit_data = request.data

        # Parse circuit data
        nodes, input_node, output_node = circuit_data["nodes"], circuit_data["input_node"], circuit_data["output_node"]
        node_index = {node: i for i, node in enumerate(nodes)}
        num_nodes = len(nodes)

        # Initialize conductance matrix and current vector
        G = np.zeros((num_nodes, num_nodes))
        I = np.zeros(num_nodes)

        # Populate the conductance matrix based on connections
        for conn in circuit_data["connections"]:
            start, end, resistance = conn["start"], conn["end"], conn["resistance"]
            i, j = node_index[start], node_index[end]
            conductance = 1 / resistance
            G[i, i] += conductance
            G[j, j] += conductance
            G[i, j] -= conductance
            G[j, i] -= conductance

        input_idx = node_index[input_node]
        output_idx = node_index[output_node]

        # Inject 1A current at the input node
        I[input_idx] = 1

        # Solve for node voltages
        G_reduced = np.delete(np.delete(G, output_idx, axis=0), output_idx, axis=1)
        I_reduced = np.delete(I, output_idx)
        V_reduced = np.linalg.solve(G_reduced, I_reduced)
        V = np.insert(V_reduced, output_idx, 0)

        # Calculate equivalent resistance
        R_eq = V[input_idx]
        return Response({"equivalent_resistance": R_eq})

    except Exception as e:
        return Response({"error": str(e)}, status=400)
