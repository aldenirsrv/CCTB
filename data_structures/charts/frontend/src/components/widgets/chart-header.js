import React from 'react';
import {LastPrice,  Indicador, TradeCount } from '.';
import { useDarkMode } from '../../_generic/dark-mode';

function ChartHeader({ data }) {
   const { isDarkMode } = useDarkMode()
return<div className={isDarkMode ? 'chart-header dark-mode': 'chart-header'} >
    <img src={data.img} alt={data.crypto_id} width={30} height={30} />
    <LastPrice price={data?.price} />
    <div>
    <TradeCount trade = {data?.data?.tradeCount} />
    </div>
    <Indicador percent={data?.data?.percent} />
</div>

}

export default ChartHeader;