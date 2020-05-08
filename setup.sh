sudo apt-get install python3-pip
pip3 install Adafruit_SSD1306
sudo cp ./fan.py /usr/local/bin/
sudo cp ./oled.py /usr/local/bin/
sudo cp ./fan.sh /usr/local/bin/
sudo cp ./oled.sh /usr/local/bin/
sudo cp ./fan.service /etc/systemd/system/
sudo cp ./fan.service /etc/systemd/system/
sudo systemctl enable fan.service
sudo systemctl enable fan.service
sudo systemctl start fan.service
sudo systemctl start oled.service