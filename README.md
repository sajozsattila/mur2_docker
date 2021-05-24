# Install for mur2 editor

Docker image for local installed [μr² editor](https://github.com/sajozsattila/mur2_editor).

# Steps
1. Install mur2_pandoc docker 
   ``` git clone https://github.com/sajozsattila/pandoc.git && cd pandoc && bash build.sh ```
1. Install mur2_docker docker images
   ``` git clone https://github.com/sajozsattila/mur2_docker.git && cd mur2_docker && bash build.sh ```
1. Run the mur2_docker images
   ``` docker run --name mur2_docker  -p 8000:8000 mur2_docker:1.7.2 ```
   
The editor should be available on the http://localhost:8000 port.

Currently the image run the editor version 1.7.2 which is *not* the stable branch. 