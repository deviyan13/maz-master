from django.db import models

# Create your models here.
class EncryptedPackage(models.Model):
    package = models.CharField(max_length=123)

    def __str__(self):
        return f'Encrypted package #{self.id}'

class BasePackage(models.Model):
    package = models.OneToOneField(EncryptedPackage, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    vin = models.CharField(max_length=17)
    control_sum = models.BinaryField(max_length=1)

    class Meta:
        abstract = True

class SimplifiedPackage(models.Model):
    datetime = models.DateTimeField()
    vin = models.CharField(max_length=17)
    control_sum = models.BinaryField(max_length=1)
    latitude = models.FloatField()
    longitude = models.FloatField()
    totalMileage = models.FloatField()
    totalEngineHours = models.IntegerField()
    velocityTax = models.IntegerField()
    velocityWheel = models.IntegerField()
    velocityNavigation = models.IntegerField()
    totalFuelUsage = models.IntegerField()
    specificFuelConsumption = models.IntegerField()
    instantFuelEconomy = models.FloatField()
    totalFuelEngineUsage = models.IntegerField()
    fuelLevel = models.IntegerField() #Уровень топлива
    fuelPedalState = models.BooleanField()
    engineSpeed = models.IntegerField()
    currentProcentTorque = models.IntegerField()
    currentLoadEnginePercent = models.IntegerField()
    coolingLiquidTemperature = models.IntegerField() #температура охлаждающей жидкости
    currentModerator = models.IntegerField()
    dieselLiquidTankLevel = models.IntegerField()
    temperatureOutside = models.IntegerField() #температура снаружи
    firstMainBrakeAirPressure = models.IntegerField()
    secondMainBrakeAirPressure = models.IntegerField()
    bigLights = models.BooleanField()
    lowBeam = models.BooleanField()
    highBeam = models.BooleanField()
    turnSignal = models.BooleanField()
    emergencySignal = models.BooleanField()
    stopSignal = models.BooleanField()
    reverseGear = models.BooleanField()
    frontFogLamp = models.BooleanField()
    backFogLamp = models.BooleanField()
    brakePedal = models.BooleanField()
    clutchPedal = models.BooleanField()
    parkingBrake = models.BooleanField()
    driverDoor = models.BooleanField()
    cruiseControl = models.BooleanField()
    windowCleaner = models.BooleanField()
    conditionerDriver = models.BooleanField()  # кондиционер водителя
    conditionerSalon = models.BooleanField()  # кондиционер салона
    conditioner = models.BooleanField() # кондиционер (салона, водителя??)
    emergencyStopSignal = models.BooleanField()
    engineOverheating = models.BooleanField()
    lowEngineOilPressure = models.BooleanField()
    lowCoolingLiquidLevel = models.BooleanField()
    engineTrouble = models.BooleanField()
    batteryCharging = models.BooleanField()
    fuelFilterClogging = models.BooleanField()
    airFilterClogging = models.BooleanField()
    lowNeutralReagentLevel = models.BooleanField()
    neutralizationTrouble = models.BooleanField()
    transmissionOverheating = models.BooleanField()
    lowTransmissionOilLevel = models.BooleanField()
    absTrouble = models.BooleanField()
    steeringTrouble = models.BooleanField()
    lowSteeringOilLevel = models.BooleanField()
    lowFuelLevel = models.BooleanField()
    package = models.OneToOneField(on_delete=models.deletion.CASCADE, to='main.EncryptedPackage')

    # New fields
    cabinTemperature = models.IntegerField() # температура в кабине
    salonTemperature = models.IntegerField() # температура в салоне
    pjd1PumpSwitch = models.BooleanField() # пжд1 насос
    pjd1BurnerSwitch = models.BooleanField() # пжд1 горелка
    osPjd1Pump = models.BooleanField() # ос насос пжд1
    osPjd1Burner = models.BooleanField() # ос горелка пжд1
    pjd2Switch = models.BooleanField() # пжд2 выключатель
    cabinHeaterValve = models.BooleanField() # Клапан отопителя кабины
    salonHeaterValve1 = models.BooleanField() # Клапан отопителя салона 1
    salonHeaterValve2 = models.BooleanField() # Клапан отопителя салона 2
    salonFans = models.BooleanField() # вентиляторы салона
    automaticSalonHeatingMode = models.BooleanField() # Автоматический режим отопления салона
    salonLightingSwitch = models.BooleanField() # Выключатель освещения салона
    automaticSalonLightingMode = models.BooleanField() # Автоматический режим освещения салона
    salonHeaterFansSpeed1 = models.BooleanField() # Включение вентиляторов отопителей салона 1 скорость
    salonHeaterFansSpeed2 = models.BooleanField() # Включение вентиляторов отопителей салона 2 скорость

    def __str__(self):
        return f'SimplifiedPackage of car {self.vin} from {self.datetime}'