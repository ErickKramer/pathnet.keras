import os 
import random
import pickle 
from genetic_agents import GeneticAgents
from pathnet import PathNet
# import mnist_dataset
# import svhn_dataset
# import cifar_dataset
# import get_svhn_data

def main():
    num_layers = 3
    num_modules = 10
    shape = (num_modules, num_layers)
    population_size = 32
    max_num_active_paths = 3
    num_module_neurons = 10
    split_length = 20
    input_size = split_length * 6
    output_size = split_length * 3
    num_tasks = 3
    max_num_genetic_epochs = 100
    num_path_epochs = 100
    num_samples_per_epoch = 16*50 # Why these values?

    # Load PathNet class
    pathnet = PathNet(shape, population_size, input_size, output_size,
                    num_module_neurons, num_tasks)

    # Load GeneticAgents 
    genetic_agents = GeneticAgents(shape, population_size, max_num_active_paths)
    
    # Generate results folder
    if not os.path.isdir('./results'):
        os.makedirs("./results")
    
    # Generate data folder
    if not os.path.isdir('./data'):
        os.makedirs("./data")
    
    # Download mnist dataset
    if not os.path.isdir('./data/mnist'):
        os.system('./download_mnist.sh')
        print("mnist dataset downloaded successfully")
        

    # Instantiate the taskmanager
    # task_manager = TaskManager(pathnet, genetic_agents, da)



if __name__=='__main__':
    main()