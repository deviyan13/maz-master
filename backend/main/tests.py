from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from main.models import SimplifiedPackage
from main.models import EncryptedPackage


encrypted_package = EncryptedPackage.objects.create(package="10")


class SimplifiedPackageTestCase(TestCase):
    def setUp(self):
        # Создаем тестовый экземпляр SimplifiedPackage
        SimplifiedPackage.objects.create(
            vin = 1313,
            datetime = datetime.now(),
            package_id = 10,
            latitude = 51.5074,
            longitude=-0.1278,
            totalMileage=10000,
            totalEngineHours=10,
            velocityTax=60,
            velocityWheel=50,
            velocityNavigation=55,
            totalFuelUsage=100,
            specificFuelConsumption=12,
            instantFuelEconomy=8,
            totalFuelEngineUsage=120,
            fuelLevel=75,
            fuelPedalState=True,
            engineSpeed=2000,
            currentProcentTorque=80,
            currentLoadEnginePercent=70,
            coolingLiquidTemperature=90,
            currentModerator=40,
            dieselLiquidTankLevel=70,
            temperatureOutside=20,
            firstMainBrakeAirPressure=110,
            secondMainBrakeAirPressure=100,
            bigLights=True,
            lowBeam=False,
            highBeam=True,
            turnSignal=False,
            emergencySignal=False,
            stopSignal=False,
            reverseGear=False,
            frontFogLamp=False,
            backFogLamp=False,
            brakePedal=True,
            clutchPedal=False,
            parkingBrake=False,
            driverDoor=True,
            cruiseControl=False,
            windowCleaner=False,
            conditioner=True,
            emergencyStopSignal=False,
            engineOverheating=False,
            lowEngineOilPressure=False,
            lowCoolingLiquidLevel=False,
            engineTrouble=False,
            batteryCharging=True,
            fuelFilterClogging=False,
            airFilterClogging=False,
            lowNeutralReagentLevel=False,
            neutralizationTrouble=False,
            transmissionOverheating=False,
            lowTransmissionOilLevel=False,
            absTrouble=False,
            steeringTrouble=False,
            lowSteeringOilLevel=False,
            lowFuelLevel=False

            # Добавьте остальные поля с тестовыми данными
        )

    def test_simplified_package_creation(self):
        """Test that SimplifiedPackage was created successfully"""
        test_car = SimplifiedPackage.objects.get(vin="1313")
        self.assertEqual(test_car.totalMileage, 10000)  # Проверяем, что поле totalMileage имеет ожидаемое значение

    def test_api_endpoint(self):
        """Test API endpoint for getting car details"""
        response = self.client.get(reverse('car-detail'), {'vin': '1313'})
        self.assertEqual(response.status_code, 200)  # Проверяем, что запрос к API возвращает успешный статус

        data = response.json()
        self.assertEqual(data['vin'], 'YourVinNumberHere')  # Проверяем, что в ответе содержится ожидаемый vin

    # Добавьте другие тесты по мере необходимости
