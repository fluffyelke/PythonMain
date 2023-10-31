#8-15
from print_module import print_models, show_completed_modles

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def run_my_program():
    print_models(unprinted_designs, completed_models)
    show_completed_modles(completed_models)
    
run_my_program()
