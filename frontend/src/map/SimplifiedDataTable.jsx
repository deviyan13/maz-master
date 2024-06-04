import React from "react";
import style from "./SimplifiedDataTable.module.css";

// =============> Данные заголовка <==============
// datetime - дата и время

// =============> Перечень данных <==============
// latitude - широта
// lontitude - долгота
// totalMileage- общий пробег
// totalEngineHours- общее число моточасов двигателя
// velocityTax- скорость от таксографа
// velocityWheel- скорость на основе вращения колеса
// velocityNavigation- скорость на основе навигации
// totalFuelUsage- всего испольщовано топливаlatitude = models.FloatField()
// specificFuelConsumption - удельный расход топлива
// instantFuelEconomy - мгновенная экономия топлива
// totalFuelEngineUsage - всего использовано топлива двигателем
// fuelLevel - уровень топлива
// fuelPedalState - положение педали подачи топлива
// engineSpeed - обороты двигателя
// currentProcentTorque - текущий процент крутящего момента
// currentLoadEnginePercent - процент нагрузки двигателя на текущей скорости
// coolingLiquidTemperature - температура охлождающей жидкости
// currentModerator - текущий замедлитель
// dieselLiquidTankLevel - уровень резервуара жидкости дизельного выхлопа
// temperatureOutside - температура окружающего воздуха
// firstMainBrakeAirPressure - давление воздуха основного тормоза контур 1
// secondMainBrakeAirPressure - - давление воздуха основного тормоза контур 2

// =============> Перечень ошибок <==============
//bigLights - габаритные фонари
//lowBeam - ближний свет
//highBeam - дальний свет
//turnSignal - сигнализация поворотов
//emergencySignal - аварийная сигнализация
//stopSignal - стоп сигналы
//reverseGear - задний ход
//frontFogLamp - передняя противотуманная фара
//backFogLamp - задняя противотуманная фара
//brakePedal - Педаль торможения	
//clutchPedal - Педаль сцепления	
//parkingBrake - Стояночный тормоз	
//driverDoor - Открыта дверь водителя
//cruiseControl - Включен круиз-контроль	
//windowCleaner - Включен стеклоочиститель
//conditioner - Включен кондиционер	
//emergencyStopSignal - Аварийный сигнализатор «СТОП»	
//engineOverheating - Перегрев двигателя
//lowEngineOilPressure - Низкое давление масла двигателя	
//lowCoolingLiquidLevel - Низкий уровень охлаждающей жидкости
//engineTrouble - Неисправность двигателя	
//batteryCharging - Зарядка батарей	
//fuelFilterClogging - Засорённость топливного фильтра
//airFilterClogging - Засорённость воздушного фильтра
//lowNeutralReagentLevel - Низкий уровень реагента системы нейтрализации	
//neutralizationTrouble - Неисправность системы нейтрализации
//transmissionOverheating  - Перегрев трансмиссии	
//lowTransmissionOilLevel - Низкий уровень масла трансмиссии	
//absTrouble - Неисправность АБС/ EBS/СКУ	
//steeringTrouble - Неисправность рулевого управления	
//lowSteeringOilLevel - Низкий уровень масла рулевого управления	
//lowFuelLevel - Низкий уровень топлива	

const SimplifiedDataList = ({list,...props}) =>{
    return(
        <div className={style.columns}>
            <div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Машина: </div>
                    <div className={style.dataValue}>{list.vin}</div>
                </div>
                
                <div className={style.dataRow}>
                    <div className={style.dataName}>Дата/время: </div>
                    <div className={style.dataValue}>{list.datetime}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Широта/долгота:</div>
                    <div className={style.dataValue}>{list.latitude};{list.longitude}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Общий пробег:</div>
                    <div className={style.dataValue}>{list.totalMileage}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Общее число моточасов двигателя:</div>
                    <div className={style.dataValue}>{list.totalEngineHours}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Cкорость по тахографу:</div>
                    <div className={style.dataValue}>{list.velocityTax}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Скорость на основе вращения колеса:</div>
                    <div className={style.dataValue}>{list.velocityWheel}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Скорость на основе навигации:</div>
                    <div className={style.dataValue}>{list.velocityNavigation}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Всего использовано топлива:</div>
                    <div className={style.dataValue}>{list.totalFuelUsage}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Удельный расход топлива:</div>
                    <div className={style.dataValue}>{list.specificFuelConsumption}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Мгновенная экономия топлива:</div>
                    <div className={style.dataValue}>{list.instantFuelEconomy}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Всего использовано топлива двигателем:</div>
                    <div className={style.dataValue}>{list.totalFuelEngineUsage}</div>
                </div>
            </div>
            <div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Уровень топлива:</div>
                    <div className={style.dataValue}>{list.fuelLevel}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Положение педали подачи топлива:</div>
                    <div className={style.dataValue}>{list.fuelPedalState}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Обороты двигателя:</div>
                    <div className={style.dataValue}>{list.engineSpeed}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Текущий процент крутящего момента:</div>
                    <div className={style.dataValue}>{list.currentProcentTorque}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Процент нагрузки двигателя на текущей скорости:</div>
                    <div className={style.dataValue}>{list.currentLoadEnginePercent}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Температура охлождающей жидкости:</div>
                    <div className={style.dataValue}>{list.coolingLiquidTemperature}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Текущий замедлитель:</div>
                    <div className={style.dataValue}>{list.currentModerator}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Уровень резервуара жидкости дизельного выхлопа:</div>
                    <div className={style.dataValue}>{list.dieselLiquidTankLevel}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Температура окружающего воздуха:</div>
                    <div className={style.dataValue}>{list.temperatureOutside}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Давление воздуха основного тормоза контур 1:</div>
                    <div className={style.dataValue}>{list.firstMainBrakeAirPressure}</div>
                </div>
                <div className={style.dataRow}>
                    <div className={style.dataName}>Давление воздуха основного тормоза контур 2:</div>
                    <div className={style.dataValue}>{list.secondMainBrakeAirPressure}</div>
                </div>
            </div>
        </div>
        
    )
}

export default SimplifiedDataList;