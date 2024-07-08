![Logo](https://raw.githubusercontent.com/TorBox-App/torbox-tinfoil-server/main/assets/header.png)


#### About

The TorBox Tinfoil Server allows you to easily set up your own custom Tinfoil shop of curated items downloaded from TorBox. This allows you to use TorBox as a repository rather than storing your files on your own server, or relying on someone else to download them for you. 

#### Important Notice
*TorBox does not allow piracy or condone it in any way. This is meant to be used with games you own and have the rights to.*



## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file.

`TORBOX_API_KEY` *Your TorBox API key used to authenticate you with TorBox. You can find this [here](https://torbox.app/settings). This is required to use this server.*

`AUTH_USERNAME` *The login username when adding your server to Tinfoil. Default is: admin*

`AUTH_PASSWORD` *The login password when adding your server to Tinfoil. Default is: adminadmin*

`PORT` *The port that the server will run on. Usually no need to change this. If you do change this and are using Docker, change your port, such as `-p 9000:9000` Default is: 8000*



## Connection Details
Connection details will vary depending on how you want to expose your server/computer as well as access the TorBox Tinfoil Server.

**Protocol**: `http` unless you know what you are doing.

**Host**: This will be your server/computer's local IP. You can get this by checking your router, or by running `ipconfig` in a terminal. This will show all of your network interfaces. Usually it will look like `192.168.X.X` or `10.X.X.X` or `172.16.X.X`. Get this exact address. For example, `192.168.1.2`. This can also be your WAN IP or public IP, which you can find by going [here](http://ifconfig.io/)

**Port**: The `PORT` environment variable, as seen above. If you change this, make sure to update your connection details in Tinfoil. Default is `8000`.

**Path**: No need to change this. Keep blank.

**Username**: The `AUTH_USERNAME` environment variable, as seen above. If you change this, make sure to update your connection details in Tinfoil. Default is `admin`.

**Password**: The `AUTH_PASSWORD` environment variable, as seen above. If you change this, make sure to update your connection details in Tinfoil. Default is `adminadmin`.

**Title**: Anything you like. We like to keep it simple with `TorBox Tinfoil Server`.

**Enabled**: `YES`



## Running on Docker (recommended)
1. Make sure you have Docker installed on your server/computer. If on a server, you can find instructions [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04) (you can change your distribution in the guide). If on a computer, you can find instructions [here](https://docs.docker.com/desktop/install/windows-install/) (you can change your computer type on the left side).
2. Edit the below Docker command with your proper environment variables and options.
```bash
docker run -it -d \
    -p 8000:8000 \
    -e TORBOX_API_KEY=<EDIT_THIS_KEY> \
    -e AUTH_USERNAME=admin \
    -e AUTH_PASSWORD=adminadmin \
    -e PORT=8000 \
    anonymoussystems/torbox-tinfoil-server:latest
```
or if you prefer Docker compose, this is the yaml, also found [here](https://github.com/TorBox-App/torbox-tinfoil-server/blob/main/docker-compose.yml).
```yml
name: torbox-tinfoil-server
services:
    torbox-tinfoil-server:
        stdin_open: true
        tty: true
        ports:
            - 8000:8000
        environment:
            - TORBOX_API_KEY=<EDIT_THIS_KEY>
            - AUTH_USERNAME=admin
            - AUTH_PASSWORD=adminadmin
            - PORT=8000
        image: anonymoussystems/torbox-tinfoil-server:latest
```
3. Connect using the connection details found above from Tinfoil.



## Running Locally (no Docker)
1. Make sure you have Python installed. Anything from v3.6 should be okay.
2. Download or git clone this repository.
```
git clone https://github.com/TorBox-App/torbox-tinfoil-server.git
```
or download repository zip [here](https://github.com/TorBox-App/torbox-tinfoil-server/archive/refs/heads/main.zip) and extract the files.

3. Create a `.env` file or rename `.env.example` to `.env`.
4. Edit or add in your environment variables to the `.env` file.
5. If planning to run over the internet, make sure port 8000 is open. You may also edit this port using the `PORT` environment variable.
6. Run the `main.py` script.
```
python3 main.py
```
7. Connect using the connection details found above from Tinfoil.



## Support

For support, email contact@torbox.app or join our Discord server [here](https://join-discord.torbox.app). *We will not give sources or help with piracy in any way. This is for technical support only.*


