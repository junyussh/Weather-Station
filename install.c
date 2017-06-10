#include "stdio.h"
#include "stdlib.h"

int main(void)
{
	system("sudo mkdir /usr/Weather_service");
	system("sudo mv RPi\\ software/main_ACM0.py /usr/Weather_service");
	system("sudo mv RPi\\ software/autorun.sh /usr/Weather_service");
	system("sudo mkdir /usr/Weather_service/Data");
	system("sudo touch /usr/Weather_service/Data/data.txt");
	system("sudo mv RPi\\ software/crontab /etc");
	system("sudo chmod +x /etc/crontab");
	system("sudo crontab /etc/crontab");
	printf("Install completed\n");
	printf("Thank you\n");
}