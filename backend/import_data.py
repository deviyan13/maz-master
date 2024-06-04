import os
import django
import csv
import re
import random
from datetime import datetime


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from main.models import SimplifiedPackage, EncryptedPackage

def extract_hex_string(input_string):
    # Используем регулярное выражение для извлечения шестнадцатеричной строки
    match = re.search(r'\"([0-9a-fA-F]{16})\"', input_string)
    if match:
        return match.group(1)
    return None

def decode_hex_string(hex_string):
    # Преобразуем шестнадцатеричную строку в байты
    data_bytes = bytes.fromhex(hex_string)

    # Расшифровываем данные в соответствии с указанной схемой
    decoded_data = {}

    # Температуры (offset -40)
    decoded_data['Температура наружного воздуха'] = int(data_bytes[0] - 40)
    decoded_data['Температура в кабине'] = int(data_bytes[1] - 40)
    decoded_data['Температура в салоне'] = int(data_bytes[2] - 40)
    decoded_data['Температура охлаждающей жидкости двигателя'] = int(data_bytes[3] - 40) if data_bytes[3] != 0xFF else None

    # Битовые значения (data_4 и data_5)
    data_4 = data_bytes[4]
    decoded_data['Выключатель ПЖД1 насос'] = int((data_4 & 0b00000001) != 0)
    decoded_data['Выключатель ПЖД1 горелка'] = int((data_4 & 0b00000010) != 0)
    decoded_data['ОС насос ПЖД1'] = int((data_4 & 0b00000100) != 0)
    decoded_data['ОС горелка ПЖД1'] = int((data_4 & 0b00001000) != 0)
    decoded_data['ПЖД2 выключатель'] = int((data_4 & 0b00010000) != 0)
    decoded_data['ОС ПЖД2'] = int((data_4 & 0b00100000) != 0)
    decoded_data['ОС кондиционер водителя'] = int((data_4 & 0b01000000) != 0)
    decoded_data['ОС кондиционер салона'] = int((data_4 & 0b10000000) != 0)

    # Битовые значения (data_5)
    data_5 = data_bytes[5]
    decoded_data['Клапан отопителя кабины'] = int((data_5 & 0b00000001) != 0)
    decoded_data['Клапан отопителя салона 1'] = int((data_5 & 0b00000010) != 0)
    decoded_data['Клапан отопителя салона 2'] = int((data_5 & 0b00000100) != 0)
    decoded_data['Вентиляторы салона'] = int((data_5 & 0b00001000) != 0) if data_5 != 0xFF else None
    decoded_data['Автоматический режим отопления салона'] = int((data_5 & 0b00010000) != 0)
    decoded_data['Выключатель освещения салона'] = int((data_5 & 0b00100000) != 0)
    decoded_data['Автоматический режим освещения салона'] = int((data_5 & 0b01000000) != 0)

    # Уровень топлива
    decoded_data['Уровень топлива'] = float(data_bytes[6] * 0.4) if data_bytes[6] != 0xFF else None

    # Битовые значения (data_7)
    data_7 = data_bytes[7]
    decoded_data['Включение вентиляторов отопителей салона 1 скорость'] = int((data_7 & 0b00000001) != 0)
    decoded_data['Включение вентиляторов отопителей салона 2 скорость'] = int((data_7 & 0b00000010) != 0)

    return decoded_data

# Чтение и обработка CSV файла
csv_file_path = r'data-1710234922010.csv'  # Замените на путь к вашему файлу

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    SimplifiedPackage.objects.all().delete()
    EncryptedPackage.objects.all().delete()
    for row in csv_reader:
        input_string = row[0]  # Предполагаем, что нужная строка находится в первом столбце
        hex_string = extract_hex_string(input_string)
        if hex_string:
            decoded = decode_hex_string(hex_string)
            # Создаем экземпляр модели SimplifiedPackage с помощью декодированных данных

            package_number = random.randint(1, 10000)

            encrypted_package = EncryptedPackage(package=package_number)
            encrypted_package.save()

            package = SimplifiedPackage(
                datetime=datetime.today(),  # Предполагаем, что дата и время находятся во втором столбце
                vin= 1313,  # Предполагаем, что VIN находится в третьем столбце
                control_sum= b'\x00\x01\x02\x03',  # Предполагаем, что контрольная сумма находится в четвертом столбце
                latitude=random.uniform(10.0, 20.0),  # Предполагаем, что широта находится в пятом столбце
                longitude=random.uniform(10.0, 20.0),  # Предполагаем, что долгота находится в шестом столбце
                totalMileage=decoded.get('totalMileage', 100),
                totalEngineHours=decoded.get('totalEngineHours', 100),
                velocityTax=decoded.get('velocityTax', 100),
                velocityWheel=decoded.get('velocityWheel', 100),
                velocityNavigation=decoded.get('velocityNavigation', 100),
                totalFuelUsage=decoded.get('totalFuelUsage', 100),
                specificFuelConsumption=decoded.get('specificFuelConsumption', 100),
                instantFuelEconomy=decoded.get('instantFuelEconomy', 100),
                totalFuelEngineUsage=decoded.get('totalFuelEngineUsage', 100),
                fuelLevel=decoded.get('Уровень топлива', 100),
                fuelPedalState=decoded.get('fuelPedalState', False),
                engineSpeed=decoded.get('engineSpeed', 100),
                currentProcentTorque=decoded.get('currentProcentTorque', 100),
                currentLoadEnginePercent=decoded.get('currentLoadEnginePercent', 100),
                coolingLiquidTemperature=decoded.get('Температура охлаждающей жидкости двигателя', 100),
                currentModerator=decoded.get('currentModerator', 100),
                dieselLiquidTankLevel=decoded.get('dieselLiquidTankLevel', 10),
                temperatureOutside=decoded.get('Температура наружного воздуха', 10),
                firstMainBrakeAirPressure=decoded.get('firstMainBrakeAirPressure', 10),
                secondMainBrakeAirPressure=decoded.get('secondMainBrakeAirPressure', 10),
                bigLights=decoded.get('bigLights', False),
                lowBeam=decoded.get('lowBeam', False),
                highBeam=decoded.get('highBeam', False),
                turnSignal=decoded.get('turnSignal', False),
                emergencySignal=decoded.get('emergencySignal', False),
                stopSignal=decoded.get('stopSignal', False),
                reverseGear=decoded.get('reverseGear', False),
                frontFogLamp=decoded.get('frontFogLamp', False),
                backFogLamp=decoded.get('backFogLamp', False),
                brakePedal=decoded.get('brakePedal', False),
                clutchPedal=decoded.get('clutchPedal', False),
                parkingBrake=decoded.get('parkingBrake', False),
                driverDoor=decoded.get('driverDoor', False),
                cruiseControl=decoded.get('cruiseControl', False),
                windowCleaner=decoded.get('windowCleaner', False),
                conditionerDriver=decoded.get('ОС кондиционер водителя', False),
                conditionerSalon=decoded.get('ОС кондиционер салона', False),
                conditioner=decoded.get('conditioner', False),
                emergencyStopSignal=decoded.get('emergencyStopSignal', False),
                engineOverheating=decoded.get('engineOverheating', False),
                lowEngineOilPressure=decoded.get('lowEngineOilPressure', False),
                lowCoolingLiquidLevel=decoded.get('lowCoolingLiquidLevel', False),
                engineTrouble=decoded.get('engineTrouble', False),
                batteryCharging=decoded.get('batteryCharging', False),
                fuelFilterClogging=decoded.get('fuelFilterClogging', False),
                airFilterClogging=decoded.get('airFilterClogging', False),
                lowNeutralReagentLevel=decoded.get('lowNeutralReagentLevel', False),
                neutralizationTrouble=decoded.get('neutralizationTrouble', False),
                transmissionOverheating=decoded.get('transmissionOverheating', False),
                lowTransmissionOilLevel=decoded.get('lowTransmissionOilLevel', False),
                absTrouble=decoded.get('absTrouble', False),
                steeringTrouble=decoded.get('steeringTrouble', False),
                lowSteeringOilLevel=decoded.get('lowSteeringOilLevel', False),
                lowFuelLevel=decoded.get('lowFuelLevel', False),
                cabinTemperature=decoded.get('Температура в кабине', 100),
                salonTemperature=decoded.get('Температура в салоне', 100),
                pjd1PumpSwitch=decoded.get('Выключатель ПЖД1 насос', False),
                pjd1BurnerSwitch=decoded.get('Выключатель ПЖД1 горелка', False),
                osPjd1Pump=decoded.get('ОС насос ПЖД1', False),
                osPjd1Burner=decoded.get('ОС горелка ПЖД1', False),
                pjd2Switch=decoded.get('ПЖД2 выключатель', False),
                cabinHeaterValve=decoded.get('Клапан отопителя кабины', False),
                salonHeaterValve1=decoded.get('Клапан отопителя салона 1', False),
                salonHeaterValve2=decoded.get('Клапан отопителя салона 2', False),
                salonFans=decoded.get('Вентиляторы салона', False),
                automaticSalonHeatingMode=decoded.get('Автоматический режим отопления салона', False),
                salonLightingSwitch=decoded.get('Выключатель освещения салона', False),
                automaticSalonLightingMode=decoded.get('Автоматический режим освещения салона', False),
                salonHeaterFansSpeed1=decoded.get('Включение вентиляторов отопителей салона 1 скорость', False),
                salonHeaterFansSpeed2=decoded.get('Включение вентиляторов отопителей салона 2 скорость', False),
                package=encrypted_package
            )
            # Сохраняем экземпляр модели в базе данных
            package.save()
            print(f'Данные успешно сохранены: {package}')
        else:
            print(f'Шестнадцатеричная строка не найдена в строке: {input_string}')
