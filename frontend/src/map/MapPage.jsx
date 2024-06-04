import React from "react";
import MyMap from "./MyMap";
import { useState } from "react";
import { icon, latLng } from "leaflet";
import style from "./MapPage.module.css"
import { useEffect } from "react";
import iconSrc from "./image/dot.png"
import actIconSrc from "./image/actdot.png"
import axios from "axios";
import SimplifiedDataList from "./SimplifiedDataTable";

const MapPage = () =>{
    let [carsList, setCarsList] = useState([{vin:""}]);
    let [activeCars, setActiveCars] = useState([])

    let [tableMode, setTable] = useState (1);
    let [activeMarker, setActiveMarker] = useState(null);
    let [activeMarkerPos, setActiveMarkerPos] = useState(0);

    let [data,setData] = useState([])
    let [dots,setDots] = useState([])
    let [simplifiedDataList, setSimplifiedDataList] = useState() 
    
    let Icon = icon({
        iconUrl: iconSrc,
        iconSize: [30, 30],
        iconAnchor: [15, 25]
    });
    
    let activeIcon = icon({
        iconUrl: actIconSrc,
        iconSize: [30, 30],
        iconAnchor: [15, 25]
    })


    let path = [{
        color: "#298a7e"
    },{
        color: "#a2fff3"
    },{
        color: "#ff5d5d"
    }]

    let styles = [Icon, activeIcon, path];

    const tryAddCar = (event) => { // okay
        let i = activeCars.indexOf(event.target.value);
        if(i !== -1)
        {
            let tmpArr = [];
            for(let h = 0; h<activeCars.length; h++)
            {
                if(activeCars[h]!=event.target.value)
                    tmpArr.push(activeCars[h]);
            }
            setActiveCars(tmpArr);
            event.target.className = style.option;

            console.log('deleted car ' + event.target.value);

            return;
        }
        else
        {
            if(activeCars.length !== 2) // fix of count is required
            {
                console.log('added car ' + event.target.value);

                setActiveCars([...activeCars,event.target.value]);
                event.target.className=style.activeOption;
            }
            else
            {
                console.log("max 3");
            }
        }
        
    }

    //const handleActiveMarker = (marker, way) => {
    //    if(activeMarker!==null)
    //    {
    //      activeMarker.setIcon(Icon);
    //    }
    //    marker.setIcon(activeIcon);
    //    let i = 0;
    //    way.map(way =>
    //        way.getLatLngs().map(unit =>
    //        {
    //            if (unit.equals(marker.getLatLng()))
    //            {
    //                setActiveMarkerPos(i)
    //            }
    //            else
    //            {
    //                i++
    //            }
    //        }));
    //    setActiveMarker(activeMarker=marker);
    //}

    const handleActiveMarker = (marker, carIndex) => {
        if (activeMarker !== null) {
            activeMarker.setIcon(Icon);
        }
        marker.setIcon(activeIcon);

        // Найдите индекс маркера в массиве dots для правильного извлечения данных
        let position = dots[carIndex].findIndex(dot =>
            dot[0] === marker.getLatLng().lat && dot[1] === marker.getLatLng().lng
        );

        setActiveMarkerPos({ carIndex, position });
        setActiveMarker(activeMarker = marker);
    };



    useEffect(() => {
        const apiUrl = 'http://localhost:8000/api/cars/';

        axios.get(apiUrl).then((resp) => {
            const cars = resp.data;
            setCarsList(cars);
        });

    },[]);

    

    //useEffect(() =>{
    //    let dotsTmp = [];
    //    setDots([[]]);

    //    console.log(dotsTmp);
    //    for(let i = 0; i<activeCars.length;i++)
    //    {
    //        const apiUrl = 'http://localhost:8000/api/car/?vin='+ activeCars[i];
    //        console.log(dotsTmp);
    //        setTable(1);
    //        axios.get(apiUrl).then((resp)=>{
    //        resp.data.map(unit => {dotsTmp.push([unit.latitude,unit.longitude])});
    //        if(i==0)
    //        {
    //            setDots(dotsTmp);
    //            setData(resp.data);
    //        }
    //        else if (i==1){
    //            setDots([dots[0], ...dotsTmp]);
    //            setData([data[0], ...resp.data]);
    //        }
    //        else if (i==2)
    //        {
    //            setDots([dots[0], dots[1], ...dotsTmp]);
    //            setData([data[0], data[1], ...resp.data]);
    //        }

    //        console.log(dotsTmp)
    //        dotsTmp=[[]];
    //    })    
    //    }

    //    if(activeCars.length === 0)
    //    {
    //        setDots([[]])
    //        setData([[]])
    //    }
        
    //},[activeCars])

    useEffect(() => {
        if (activeCars.length === 0) {
            setDots([]);
            setData([]);
            return;
        }

        // Формируем массив промисов для всех запросов
        const promises = activeCars.map(vin => {
            const apiUrl = 'http://localhost:8000/api/car/?vin=' + vin;
            return axios.get(apiUrl);
        });

        // Выполняем все запросы параллельно и обрабатываем результаты
        Promise.all(promises)
            .then(responses => {
                // Инициализируем временные массивы для dots и data
                let allDots = [];
                let allData = [];

                //console.log(responses)

                // Обрабатываем каждый ответ
                responses.forEach(response => {
                    const dotsForCar = response.data.map(unit => [unit.latitude, unit.longitude]);
                    const dataForCar = response.data;
                    allDots.push(dotsForCar);
                    allData.push(dataForCar);
                });

                console.log(allData);


                // Обновляем состояние dots и data
                setDots(allDots);
                setData(allData);

                console.log(allDots + ' ' + allData + ' ' + allData.length)
            })
            .catch(error => {
                console.error("Ошибка при получении данных:", error);
            });
    }, [activeCars]);


    useEffect(() => {
        if (!activeMarker || activeMarkerPos.carIndex === -1 || activeMarkerPos.position === -1) return;

        const { carIndex, position } = activeMarkerPos;

        if (carIndex < 0 || carIndex >= data.length || position < 0 || position >= data[carIndex].length) {
            console.error('Invalid activeMarkerPos:', activeMarkerPos);
            return;
        }

        let dateTime = data[carIndex][position].datetime;

        let promises = [];

        for (let i = 0; i < activeCars.length; i++) {
            const apiUrl = 'http://localhost:8000/api/car/simplified/?vin=' + activeCars[carIndex] + '&datetime=' + dateTime;
            promises.push(axios.get(apiUrl));
        }

        Promise.all(promises)
            .then((responses) => {
                //let combinedData = [];
                responses.forEach((resp) => {
                    //combinedData = combinedData.concat(resp.data);
                    setSimplifiedDataList(resp.data)
                });
                //setSimplifiedDataList(combinedData);
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    }, [activeMarker, activeMarkerPos, data, activeCars]);





    //useEffect(() => {
    //    if (activeMarkerPos < data.length) {
    //        let dateTime = data[activeMarkerPos].datetime;

    //        for (let i = 0; i < activeCars.length; i++) {
    //            const apiUrl = 'http://localhost:8000/api/car/simplified/?vin=' + activeCars[i] + '&datetime=' + dateTime;
    //            console.log(apiUrl);
    //            axios.get(apiUrl).then((resp) => {
    //                try {
    //                    setSimplifiedDataList(resp.data)
    //                }
    //                catch (e) {

    //                }
    //            })

    //        } 
    //    }
        
    //},[activeMarker])

    useEffect(()=>{
        if(activeMarker!=null){
            setTable(0);
        }
    },[simplifiedDataList])


    return(
        <div className={style.content}>

            <MyMap initStyles = {styles} activeMarker = {activeMarker} handleActiveMarker={handleActiveMarker} setTable = {setTable} dots = {dots}/>

            <div className={style.table}>
                <select multiple className={style.dropDown} >
                    {carsList.map(car => 
                        <option className = {style.option}onClick = {(event)=>tryAddCar(event)} value = {car.vin}>{car.vin}</option>
                    )}
                </select>
                <div className={style.table}>
                    <div className={style.wraper}>
                        <div className={style.title}>Выбранные машины: {activeCars.map(car=>{return(car+' ')})}</div>
                        {tableMode?
                        <div className={style.title}>
                            Ни одна точка не выбрана
                        </div>
                        :
                        <div>
                            <div className={style.title}>История точки {activeMarker.getLatLng().lat+" "+activeMarker.getLatLng().lng}</div>
                            <SimplifiedDataList list = {simplifiedDataList}/>
                        </div>
                        }
                    </div>
                </div>
            </div>
        </div>
        
    )
}

export default MapPage;