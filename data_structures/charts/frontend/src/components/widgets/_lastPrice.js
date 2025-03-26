import React from 'react';
import { formatPrice } from './__utils';

function LastPrice({ price, small=false }) {
  return   <div className={small ? 'last-price mini': 'last-price'}>{formatPrice(Number(price))}

          { !small ? <div className='label'>Last price negotiated</div>: null }
           </div> ;
}

export default LastPrice;