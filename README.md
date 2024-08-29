# hackathon-demos

Install Docker
Install Crapthon

py -m venv venv
source venv/Scripts/activate 

pip install -r ollama/requirements.txt

docker run -p 11434:11434 ollama/ollama -this takes long cause its pulling the model

    To mount to save runtime
    add -v <anywhere on host>:/root/.ollama/models
    Models will persist if you specify the same place everytime you run the container

pip install -r requirements.txt

pip install tensorflow

pip install accelerate 

make huggingface account 

run dat shit it takes a minute
transformers takes longer

discord just look up how to make a discord bot 

run the ollama container 

reset bot token after creating it 
give the bot Meesage Content Intent permission (just a tick box)
generate a new oauth2 token with scope - bot and permissions - send and read messages
