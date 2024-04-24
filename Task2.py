from graphviz import Digraph

# Sensitivity and specificity from the ML model
sensitivity = 0.8  # True positive rate
specificity = 0.9  # True negative rate

# Update the storm probabilities based on the ML model's predictions
p_storm_given_storm = sensitivity
p_no_storm_given_no_storm = specificity
p_mold_given_storm = 0.1  # Probability of mold given storm

# Original probabilities of storm and no storm
p_storm = 0.5
p_no_storm = 0.5

# Calculate the updated probabilities
p_storm_corrected = sensitivity * p_storm / (sensitivity * p_storm + (1 - specificity) * p_no_storm)
p_no_storm_corrected = specificity * p_no_storm / (specificity * p_no_storm + (1 - sensitivity) * p_storm)

# Create a Digraph for the decision tree
dot = Digraph()

# Add nodes
dot.node('A', 'Decide: Harvest Now or Wait')
dot.node('B', 'Harvest Now')
dot.node('C', 'Wait for more sugar')
dot.node('D', 'ML Predicts Storm')
dot.node('E', 'ML Predicts No Storm')
dot.node('F', 'Storm occurs')
dot.node('G', 'No Storm')
dot.node('H', 'Mold develops')
dot.node('I', 'No Mold')
dot.node('J', 'No Sugar Increase')
dot.node('K', 'Typical Sugar Increase')
dot.node('L', 'High Sugar Increase')

# Add revenue nodes with updated values
dot.node('M', 'Revenue: $960000')
dot.node('N', 'Revenue: $420000')
dot.node('O', 'Revenue: $3300000')
dot.node('P', 'Revenue: $960000')
dot.node('Q', 'Revenue: $1410000')
dot.node('R', 'Revenue: $1500000')

# Add edges for the decision-making process
dot.edge('A', 'B', label='Harvest Now')
dot.edge('A', 'C', label='Wait')

# Add edges for ML prediction outcomes
dot.edge('C', 'D', label=f'ML Predicts Storm\n({p_storm_corrected:.2f})')
dot.edge('C', 'E', label=f'ML Predicts No Storm\n({p_no_storm_corrected:.2f})')

# Add edges for the storm occurrence outcomes
dot.edge('D', 'F', label=f'Storm Occurs\n({sensitivity:.2f})')
dot.edge('D', 'G', label=f'No Storm\n({1 - sensitivity:.2f})')
dot.edge('E', 'G', label=f'No Storm\n({specificity:.2f})')

# Add edges for the mold development outcomes
dot.edge('F', 'H', label=f'Mold develops\n({p_mold_given_storm:.2f})')
dot.edge('F', 'I', label=f'No Mold\n({1 - p_mold_given_storm:.2f})')

# Add edges for the sugar level outcomes
dot.edge('G', 'J', label='60% No Sugar')
dot.edge('G', 'K', label='30% Typical Sugar')
dot.edge('G', 'L', label='10% High Sugar')

# Connect the final outcome nodes to their respective revenue
dot.edge('B', 'M', label='Revenue')
dot.edge('H', 'N', label='Revenue')
dot.edge('I', 'O', label='Revenue')
dot.edge('J', 'P', label='Revenue')
dot.edge('K', 'Q', label='Revenue')
dot.edge('L', 'R', label='Revenue')

# Save the graph to a file
dot.render('updated_decision_tree', format='png', view=True)

# The source code of the graph can be useful for debugging or manual adjustments
print(dot.source)

