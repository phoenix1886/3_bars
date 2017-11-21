# The closest bars

This script shows the biggest, the smallest and the closest to user bar in Moscow.

# How to run this script

Script should be interpreted by python3.5 and requires installed packages 'requests' and 'geopy'. 

Quick installation of required packages is possible due requirements.txt.
```
pip install -r requirements.txt
```

To run the script in Linux terminal, it is necessary to pass GPS coordinates of user as arguments.
```bash
$ python bars.py <user_longitude> <user_latitude>
```

## Example
```
python bars.py 37.6242342 55.763443453
* The smallest bar in Moscow is "Сушистор":
	Михалковская улица, дом 8
	Тел.: +7(495) 230-00-00

* The biggest bar in Moscow is "Спорт бар «Красная машина»":
	Автозаводская улица, дом 23, строение 1
	Тел.: +7(905) 795-15-84

* The closest bar for you is "Bubo Tutor Club and Gastropub":
	улица Рождественка, дом 12/1, строение 1
	Тел.: +7(499) 707-88-69
```
# Targets of a project

The project is created for educational purposes for [DEVMAN.org](https://devman.org)
