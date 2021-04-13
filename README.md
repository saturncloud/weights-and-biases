# Use Weights and Biases on Saturn Cloud
## Welcome!

This project provides examples showing how to use  <a href="https://wandb.ai/"  target='_blank' rel='noopener'>Weights and Biases</a> in Saturn Cloud, to monitor 
the training and performance of your machine learning models. We have included single-node 
training of an image classifier, as well as a multi-node example that lets you see how nicely 
Weights and Biases can integrate with distributed training on Dask clusters. 

## [Train image classifier on single node (PyTorch)](train-pytorch-local.ipynb)

In this notebook, you'll train an image classifier with PyTorch and use Weights and Biases to
 monitor model performance.

## [Use Pytorch on a single GPU](train-pytorch-cluster.ipynb)

This notebook expands upon the image classifier training task, using a Dask cluster to accelerate
 the same task. Weights and Biases is still able to easily and clearly provide model performance monitoring.

***

## How to Use

To run these examples on Saturn Cloud, please follow these instructions.

1. **Create Account**: If you haven't already, [create a Saturn Cloud account and sign in](https://www.saturncloud.io/docs/getting-started/start_in_ten/). 
2. **Connect This Repository**: Open the Repositories tab in the left side menu, and [add this repository to your account](https://www.saturncloud.io/docs/getting-started/gitrepo/). (The SSH link will be `git@github.com:saturncloud/weights-and-biases.git`.) Mark the repo as read-only when creating it. **You do not need any SSH credentials, because this repo is public.**  
3. **Add Weights and Biases Credential**: Open the Credentials tab in the left side menu, and [add your Weights and Biases user token as an Environment Variable](https://www.saturncloud.io/docs/getting-started/credentials/). Name it `WANDB_LOGIN`. (This is the [same token you would use if you logged in to Weights and Biases](https://docs.wandb.ai/ref/cli/wandb-login) at the command line.)
4. **[Create a custom project](https://www.saturncloud.io/docs/getting-started/start_project/#create-a-custom-project)**: The specifications we recommend are:
     * T4 or V100 GPU instances
     * The `saturncloud/saturn-pytorch:2021.02.22` image
     * Keep default disk space and "Shutoff After" settings
     * Make sure to attach the Repository you created in Step 2
     * Add the following to your Advanced Settings > Start Script box.
       ```
       pip install wandb dask-pytorch-ddp
       wandb login --relogin $WANDB_LOGIN
       ```

6. **Optional: Create a Cluster**: If you plan to run the cluster based example, [create a cluster in the project](https://www.saturncloud.io/docs/getting-started/create_cluster_ui/) as well. Requesting at least 3 workers is recommended. 
7. **Start Resources**: Start the Jupyter Instance, and open the `git-repos` folder to see the scripts and run them!

***

## Next steps

Thanks for trying out these examples! To learn more about how Saturn Cloud works, check out our  <a href="https://www.saturncloud.io/docs/" target='_blank' rel='noopener'>Documentation</a>, <a href="https://www.saturncloud.io/s/blog/" target='_blank' rel='noopener'>blog</a>, or join an  <a href="https://www.saturncloud.io/s/events/" target='_blank' rel='noopener'>upcoming event</a>. 

To learn more about Weights and Biases, visit  <a href="https://wandb.ai/" target='_blank' rel='noopener'>their website</a> and <a href="https://docs.wandb.ai/"  target='_blank' rel='noopener'>documentation</a>.

If you have any questions or suggestions for example projects, reach out to us at support@saturncloud.io or open an issue on the [examples Github repo](https://github.com/saturncloud/examples). 
