from graphviz import Digraph

# Create a new Digraph for the decision tree
dot = Digraph()

# Add nodes and edges
dot.node('A', 'Decide: Harvest Now or Wait')

dot.node('B', 'Harvest Now')
dot.node('C', 'Wait for more sugar')

dot.node('D', 'Storm occurs')
dot.node('E', 'No Storm')

dot.node('F', 'Mold develops')
dot.node('G', 'No Mold')

dot.node('H', 'No Sugar Increase')
dot.node('I', 'Typical Sugar Increase')
dot.node('J', 'High Sugar Increase')

# Revenue calculations
dot.node('K', 'Revenue: $80000')
dot.node('L', 'Revenue: $35000')
dot.node('M', 'Revenue: $275000')
dot.node('N', 'Revenue: $80000')
dot.node('O', 'Revenue: $117500')
dot.node('P', 'Revenue: $125000')

# Connect nodes with edges
dot.edge('A', 'B', label='Harvest Now')
dot.edge('A', 'C', label='Wait')

dot.edge('C', 'D', label='50% Storm')
dot.edge('C', 'E', label='50% No Storm')

dot.edge('D', 'F', label='10% Mold')
dot.edge('D', 'G', label='90% No Mold')

dot.edge('E', 'H', label='60% No Sugar')
dot.edge('E', 'I', label='30% Typical Sugar')
dot.edge('E', 'J', label='10% High Sugar')

# Connect to revenue nodes
dot.edge('B', 'K', label='Revenue')
dot.edge('F', 'L', label='Revenue')
dot.edge('G', 'M', label='Revenue')
dot.edge('H', 'N', label='Revenue')
dot.edge('I', 'O', label='Revenue')
dot.edge('J', 'P', label='Revenue')

# Render the graph to a file and view it
dot.render('decision_tree', format='png', view=True)
