## Auxiliary functions for simulated evolution

# alpabet
alphabet <- c("A","G","U","C")

# target matrices if fixed target is used
target_R <- matrix(c(1,0,0,0,1,0,0,0,1),3,3)
target_S <- matrix(c(1,0,0,0,1,0,0,0,1),3,3)
target_agent = list(R=target_R, S=target_S)

CAC_count <- function(population) {
  # fitness function based on number of
  # occurences of substring CAC
  fitness <- rep(0,population_size)
  for (i in 1:population_size) {
    population_member <- paste(population[i,], collapse='')
    fitness[i] <- str_count(population_member, "CAC")
  }
  return(fitness)
}

# Mutation function

mutation_matrix <- matrix(rep(1/3,16),4,4)
diag(mutation_matrix) <- 0

mutate_population_fast <- function(population) {
  # choose number of elements to change
  N_change <- rbinom(1, genome_size*population_size, prob=mu)
  
  # generate indices of elements to change
  indices <- sample(genome_size*population_size, size=N_change)
  
  # change elements
  for (index in indices) {
    row <- ceiling(index/genome_size)
    column <- index %% genome_size + 1
    distr <- mutation_matrix[match(population[row, column], alphabet),]
    population[row, column] <- sample(alphabet, size=1, prob=distr)
  }
  
  return(population)
}

population <- c(rep(1,10))
for (i in 1:10) {
  population[i] <- paste(sample(c("A","G","C","U"),size=18, replace=TRUE), collapse="")
}


## Auxiliary functions for phylogenetic trees

compute_diversity <- function(population) {
  return(nrow(unique(population)))
}

# construct a tree from a population using a parent matrix
reconstruct_tree <- function(parent_matrix) {
  D <- nrow(parent_matrix)    # maximum depth tree
  N <- ncol(parent_matrix)    # population size
  N_cur <- N                  # cur population size
  cur_depth <- 0              # cur depth tree
  
  children_indices <- seq(1,N,1)
  children <- as.character(seq(1,N,1))
  
  while (N_cur > 1 && cur_depth < D) {
    # while (cur_depth < D) {
    # create an empty list of population size to group children
    # under the right parent (index)
    parents <- vector("list",N)
    has_children <- rep(0,N)
    
    # loop over the children by looping over their indices
    child_index <- 1
    for (child in children_indices) {
      parent <- parent_matrix[D-cur_depth,child]  # find index of parent in prev generation
      child <- children[[child_index]]            # get child from array
      cur_children_parent <- parents[[parent]]    # check if parent already is assigned children
      cur_number_children <- has_children[parent] # check number of children for parent
      
      # assign child to parent
      if (cur_number_children == 0 && cur_depth > 0) {        # first child, child is already a tree
        parents[[parent]] <- children[[child_index]]
      } else if (cur_number_children == 0) {                  # first child, child is leaf node
        parents[[parent]] <- list(children[child_index])
      } else if (cur_depth == 0) {                            # not first child, child is leaf node
        parents[[parent]][[cur_number_children+1]] <- child
      } else if (cur_number_children == 1) {                  # second child, child is already a tree, children is not yet a list
        parents[[parent]] <- list(cur_children_parent, child)
      } else {                                                # third or more child
        parents[[parent]][[cur_number_children+1]] <- child
      }
      
      has_children[parent] <- has_children[parent] + 1        # increase children for parent
      
      child_index <- child_index + 1
    }
    nulls <- sapply(parents, FUN=is.null)       # check which prev population members didn't have children
    children_indices <- seq(1,N,1)[!nulls]   # get the indices of the parents, set children to them
    children <- parents[!nulls]
    N_cur <- length(children_indices)
    cur_depth <- cur_depth + 1
  }
  if (N_cur > 1) {
    print("Disconnected tree")
  } else {
    return(children)
  }
}

# print a nested_list in newick-format
print_tree <- function(nested_list) {
  str_repr <- paste(capture.output(dput(nested_list)),collapse='')
  str_repr <- gsub("[\r\n]","",str_repr)
  str_repr <- gsub('\"',"",str_repr)
  str_repr <- gsub('list',"",str_repr)
  str_repr <- paste(str_repr, ";")
  str_repr <- gsub(' ',"",str_repr)
  return(str_repr)
}

# plot the phylogenetic tree (rectangular cladogram)
plot_tree <- function(nested_list) {
  tree_str <- print_tree(nested_list)
  tree_file <- file("tree.nwk")
  writeLines(tree_str, tree_file)
  close(tree_file)
  tree <- read.tree("tree.nwk")
  ggtree(tree, layout="rectangular") + geom_tiplab(size=2)
}

# print connections in the parent matrix
print_parent_matrix <- function(parent_matrix) {
  height <- nrow(parent_matrix); width <- ncol(parent_matrix)
  N <- (height)*width
  x_from <- rep(seq(1,width,1),times=height)
  y_from <- rep(seq(1,height,1),each=width)
  y_to <- rep(seq(2,height+1,1),each=width)
  x_to <- rep(0,N)
  counter <- 1;
  for (population in height:1) {
    for (individual in 1:width) {
      x_to[counter] <- parent_matrix[population,individual] 
      counter <- counter+1
    }
  }
  par(mfrow=c(1,1))
  plot(width, height+2, xlim=c(1,width), ylim=c(0,height+2), type="n", yaxt="n", xaxt="n", 
       xlab="population member", ylab="generation")
  axis(1, at=c(1:10))
  segments(x_from, y_from, x_to, y_to)
  points(c(x_from, x_to), c(y_from, y_to))
}

# compute distance matrix
compute_distance_matrix <- function(population) {
  N <- nrow(population)
  dm <- matrix(rep(0,N*N),N,N)
  for (i in 1:(N-1)) {
    for (j in (i+1):N) {
      agent1 <- population[i,]
      agent2 <- population[j,]
      dm[j,i] <- compute_distance(agent1, agent2)
    }
  }
  colnames(dm) <- as.character(seq(1,N))
  rownames(dm) <- as.character(seq(1,N))
  dm <- as.dist(dm,diag=FALSE,upper=FALSE)
  return(dm)
}

# compute normalised hamming distance between two strings
compute_distance <- function(agent1, agent2) {
  l <- length(agent1)
  helper <- rep(0,l)
  d <- length(helper[!agent1 == agent2])/l
  return(d)
}