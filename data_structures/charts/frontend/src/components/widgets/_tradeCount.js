import React from 'react';
import { formatNumber } from './__utils';

function TradeCount({ trade = 0 }) {
  return  <div className='trades'> 
            {formatNumber(trade)}
            <span>Number od traders</span>
        </div>;
}

export default TradeCount;