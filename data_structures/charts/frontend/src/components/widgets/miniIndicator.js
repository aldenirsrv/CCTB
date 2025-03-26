import React from 'react';
import { Link } from 'react-router-dom';
import {LastPrice,  Indicador, TradeCount } from '.';
import { useDarkMode } from '../../_generic/dark-mode';

function MiniIndicator({data}) {
   const { isDarkMode } = useDarkMode()
return<Link to={`/coin/${data?.crypto_id}`}>
        <div className={isDarkMode ? 'chart-header dark-mode': 'chart-header'} >
            <img src={data?.img} alt={data?.crypto_id} width={30} height={30} />
        <div>
            {data?.crypto_id}
            <div className='crypto-name mini'>{data?.crypto_name}</div>
        </div>
        <div>

        </div>
        <div>
            <LastPrice price={data?.price} small={true} />
            <Indicador percent={data?.data?.percent} small={true} />
        </div>   
  </div>  
</Link>



}

export default MiniIndicator;