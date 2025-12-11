# young-weather-station-testing
A python project to field test the Young Weather station

### Initialization
When setting up the script, run the following command to set up the virtual environment:
```bash
make setup
```

To run the script, run the following command:
```bash
make run
```


### Systemd Service Initialization
To set up this script as a Systemd service, do the following steps:
1. Navigate to `/etc/systemd/system/`
2. Create a new file titled: `weather-station.service`
3. Paste the following contents into the file:
```
[Unit]
Description=Young Weather Station Service
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/admin/Documents/young-weather-station-testing
ExecStart=/usr/bin/make run
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
4. Run `sudo systemctl daemon-reload` to reload systemd services
5. To enable the service to restart automatically, run `sudo systemctl enable weather-station.service`
6. To start the service and begin parsing and saving data, run `sudo systemctl start weather-station.service`
7. To check logs and output of the script, run `sudo journalctl -u weather-station.service`
