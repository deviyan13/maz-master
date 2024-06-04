import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { useEffect, useRef } from 'react';
import React from 'react';
import style from '../map/MyMap.module.css';
import yandexLogo from "./image/yndex_logo_ru.png";

const MyMap = ({ activeMarker, handleActiveMarker, handleActiveWay, currentCar, ...props }) => {
    const mapRef = useRef(null);
    const markersRef = useRef([]);
    const wayRef = useRef([]);

    //const setActiveMarker = (dot) => {
    //    handleActiveMarker(dot, wayRef.current);
    //};

    const setActiveMarker = (dot, carIndex) => {
        handleActiveMarker(dot, carIndex);
    };

    const centerCalc = (dots) => {
        let lat = 0,
            lng = 0,
            num = 0;
        dots.forEach((dotGroup) => {
            dotGroup.forEach(([latDot, lngDot]) => {
                lat += latDot;
                lng += lngDot;
                num++;
            });
        });
        return (num !== 0) ? [lat / num, lng / num] : [53.9, 27.56];
    };

    const initializeMap = () => {
        if (mapRef.current !== null) {
            mapRef.current.remove();
        }

        const container = L.DomUtil.get('map');
        if (container != null) {
            container._leaflet_id = null;
        }

        try {
            mapRef.current = L.map('map', { attributionControl: false }).setView(centerCalc(props.dots), 5);
        } catch (InvalidLatLngObject) {
            mapRef.current = L.map('map', { attributionControl: false }).setView([0, 0], 5);
        }

        //var myAttrControl = L.control.attribution().addTo(mapRef.current);
        //myAttrControl.setPrefix('<a href="https://leafletjs.com/">Leaflet</a>');



        L.tileLayer(
            'https://core-renderer-tiles.maps.yandex.net/tiles?l=map&x={x}&y={y}&z={z}&scale=1&lang=ru_RU',
            //'https://tiles.api-maps.yandex.ru/v1/tiles/?x={x}&y={y}&z={z}&lang=ru_RU&l=map&apikey=9dc81119-2169-4382-a8a2-7137a513f231',
            { foo: 'bar', attribution: '&copy; <a href="https://yandex.by/maps/">YandexMaps</a> contributors' }
            //'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        ).addTo(mapRef.current);

        // Добавляем логотип Яндекса с гиперссылкой
        const yandexLogoControl = L.control({ position: 'bottomright' });

        yandexLogoControl.onAdd = function (map) {
            const div = L.DomUtil.create('div', 'yandex-logo-control');
            div.innerHTML = `<a href="https://yandex.by/maps/" target="_blank"><img src="${yandexLogo}" alt="Yandex Maps" style="width: 132px; height: 72px;" /></a>`;
            return div;
        };

        yandexLogoControl.addTo(mapRef.current);

    };

    const addWaysToMap = () => {
        wayRef.current = props.dots.map((dotGroup) => {
            //console.log('Creating polyline for dotGroup:', dotGroup);
            return L.polyline(dotGroup);
        });

        wayRef.current.forEach((way, i) => {
            way.setStyle(props.initStyles[2][i]);
            way.addTo(mapRef.current);
        });
    };

    const addMarkersToMap = () => {
        markersRef.current = [];
        props.dots.forEach((dotGroup, carIndex) => {
            dotGroup.forEach(([lat, lng]) => {
                const marker = L.marker([lat, lng], { icon: props.initStyles[0] });
                marker.on('click', function (event) {
                    setActiveMarker(event.target, carIndex);
                    //handleActiveMarker(event.target, carIndex);
                });
                marker.addTo(mapRef.current);
                markersRef.current.push(marker);
            });
        });
    };



    //const addMarkersToMap = () => {
    //    markersRef.current = [];
    //    props.dots.forEach((dotGroup) => {
    //        dotGroup.forEach(([lat, lng]) => {
    //            const marker = L.marker([lat, lng], { icon: props.initStyles[0] });
    //            marker.on('click', function (event) {
    //                setActiveMarker(event.target);
    //            });
    //            marker.addTo(mapRef.current);
    //            markersRef.current.push(marker);
    //        });
    //    });
    //};

    useEffect(() => {
        initializeMap();
        addWaysToMap();
        addMarkersToMap();
    }, [props.dots]);

    return <div id='map' className={style.map} />;
};

export default MyMap;
