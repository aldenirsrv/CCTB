import React, { useEffect, useState, useRef } from 'react';
import io from 'socket.io-client';
import axios from 'axios';
import { useDarkMode } from '../../_generic/dark-mode.js';
import { MiniIndicator } from '../widgets/index.js';

import { BarChart, PieChart, LineChart } from '../charts/index.js';
import './style.css';

// Conect to the server Flask throw WebSocket (using Socket.IO)
const socket = io('http://localhost:5000', {
  transports: ['websocket'],
});
const HomePage = () => {
  const [timeData, setTimeData] = useState([]);
  const { isDarkMode } = useDarkMode()
  // ### BTC
  const [priceBTC, setPriceBTC] = useState([]);
  const [btcData, setBTCData] = useState({});
  // ### ETH
  const [priceETH, setPriceETH] = useState([]);
  const [ethData, setETHData] = useState({});
  // ### XRP
  const [priceXRP, setPriceXRP] = useState([]);
  const [xrpData, setXRPData] = useState({});
  // ### SOL
  const [priceSOL, setPriceSOL] = useState([]);
  const [solData, setSOLData] = useState({});

  // ### TST
  const [priceMKR, setPriceMKR] = useState([]);
  const [mkrData, setMKRData] = useState({});

  const [selling, setSelling] = useState({labels: [], data: []});
  const [error, setError] = useState(null);

  const fetchPrice = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/static'); // URL do seu endpoint Flask
      const { btc, eth, xrp, sol, mkr, timestamp } = response.data;
      setTimeData((prevTimeData) => [...prevTimeData, timestamp]);
      // ### BTC
      setPriceBTC((prevPrice) => [...prevPrice, btc.price]);
      setBTCData(btc)
      // ### ETH
      setPriceETH((prevPrice) => [...prevPrice, eth.price]);
      setETHData(eth)
      // ### XRP
      setPriceXRP((prevPrice) => [...prevPrice, xrp.price]);
      setXRPData(xrp)
      // ### SOL
      setPriceSOL((prevPrice) => [...prevPrice, sol.price]);
      setSOLData(sol)
      // ### MKR
      setPriceMKR((prevPrice) => [...prevPrice, mkr.price]);
      setMKRData(mkr)


      setSelling({
        labels: [btc.crypto_id,eth.crypto_id , xrp.crypto_id, sol.crypto_id, mkr.crypto_id],
        data: [btc.data.percent, eth.data.percent, xrp.data.percent, sol.data.percent, mkr.data.percent ]
      });
    } catch (err) {
      setError('Error fetching price data');
      console.error(err)
    }
  };
  useEffect(() => {
    fetchPrice();
  }, []);
  useEffect(() => {
    socket.on('price_update', (data) => {
      const { btc, eth, xrp, sol, mkr, timestamp } = data;
      setTimeData((prevTimeData) => [...prevTimeData, timestamp]);
      setPriceBTC((prevPrice) => [...prevPrice, btc.price]);
      setPriceETH((prevPrice) => [...prevPrice, eth.price]);
      setPriceXRP((prevPrice) => [...prevPrice, xrp.price]);
      setPriceSOL((prevPrice) => [...prevPrice, sol.price]);
      setPriceMKR((prevPrice) => [...prevPrice, mkr.price]);
      setETHData((prev) => ({ ...prev, ...eth}));
      setBTCData((prev) => ({ ...prev, ...btc}));
      setXRPData((prev) => ({ ...prev, ...xrp}));
      setSOLData((prev) => ({ ...prev, ...sol}));
      setMKRData((prev) => ({ ...prev, ...mkr}));
      setSelling({
        labels: [btc.crypto_id,eth.crypto_id , xrp.crypto_id, sol.crypto_id, mkr.crypto_id],
        data: [btc.data.percent, eth.data.percent, xrp.data.percent, sol.data.percent, mkr.data.percent ]
      });
      if (timeData.length > 15) {
        setTimeData((prev) => prev.slice(1));
        setPriceBTC((prev) => prev.slice(1));
        setPriceETH((prev) => prev.slice(1));
        setPriceXRP((prev) => prev.slice(1));
        setPriceSOL((prev) => prev.slice(1));
        setPriceMKR((prev) => prev.slice(1));
      }
    });
    return () => {
      socket.off('price_update');
    };
  }, [timeData]);
  
  return (
   
    <div>
      <div  className={isDarkMode ? "hero-container dark-mode" : "hero-container"}>
          <div className="grid-item">
            <PieChart data={selling.data} labels={selling.labels} empty={true} />
          </div>
          <div className='home-mini-indicators'>
            <MiniIndicator data={btcData} />
            <MiniIndicator data={ethData} />
            <MiniIndicator data={xrpData} />
            <MiniIndicator data={solData} />
            <MiniIndicator data={mkrData} />
          </div>
          <BarChart data={selling.data} timeData={selling.labels} />
      </div>
      <div className={isDarkMode ? "grid-container dark-mode" : "grid-container"}>
        <div className="grid-item">
          <LineChart data={priceBTC} timeData={timeData} details={btcData}/>
        </div>
        <div className="grid-item">
        <LineChart data={priceETH} timeData={timeData} details={ethData} />
        </div>
        <div className="grid-item">
          <LineChart data={priceXRP} timeData={timeData} details={xrpData} />
        </div>
        <div className="grid-item">
          <LineChart data={priceSOL} timeData={timeData} details={solData} />
        </div>
        <div className="grid-item">
          <LineChart data={priceMKR} timeData={timeData} details={mkrData} />
        </div>
        <div className='sistem-status'><div className='led'></div></div>
      </div>
    </div>
  );
}
export default HomePage;